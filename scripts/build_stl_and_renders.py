#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
import trimesh

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAD_FILE = os.path.join(PROJECT_DIR, "scad", "gimas_co2_holder.scad")
STL_DIR = os.path.join(PROJECT_DIR, "stl")
RENDERS_DIR = os.path.join(PROJECT_DIR, "renders")
POBRANE_DIR = "/home/qba/Pobrane"

# OpenSCAD executable path check
OPENSCAD_BIN = shutil.which("openscad")
if not OPENSCAD_BIN:
    APPIMAGE = "/home/qba/.gemini/antigravity/scratch/stl_view/OpenSCAD.AppImage"
    if os.path.exists(APPIMAGE):
        OPENSCAD_BIN = APPIMAGE
    else:
        raise RuntimeError("OpenSCAD not found in PATH or AppImage!")

print(f"Using OpenSCAD binary: {OPENSCAD_BIN}")

SIZES = ["8g", "12g"]
STYLES = [
    (1, "styl1_modern"),
    (2, "styl2_knurled"),
    (3, "styl3_hexagon"),
    (4, "styl4_fluted"),
    (5, "styl5_spiral"),
]

os.makedirs(STL_DIR, exist_ok=True)
os.makedirs(RENDERS_DIR, exist_ok=True)

success_count = 0

for size in SIZES:
    for style_num, style_name in STYLES:
        base_name = f"gimas_co2_{size}_{style_name}"
        stl_path = os.path.join(STL_DIR, f"{base_name}.stl")
        render_path = os.path.join(RENDERS_DIR, f"{base_name}.png")
        pobrane_path = os.path.join(POBRANE_DIR, f"{base_name}.stl")

        print(f"===> Compiling {base_name}.stl ...")
        cmd_stl = [
            OPENSCAD_BIN,
            "-D", f'size="{size}"',
            "-D", f"style={style_num}",
            "-o", stl_path,
            SCAD_FILE
        ]
        subprocess.run(cmd_stl, check=True)

        print(f"     Rendering {base_name}.png ...")
        cmd_render = [
            OPENSCAD_BIN,
            "--imgsize=1024,1024",
            "--colorscheme=Sunset",
            "--camera=0,0,45,60,0,220,180",
            "-D", f'size="{size}"',
            "-D", f"style={style_num}",
            "-o", render_path,
            SCAD_FILE
        ]
        subprocess.run(cmd_render, check=True)

        # Copy to Pobrane
        shutil.copy2(stl_path, pobrane_path)
        print(f"     Copied to {pobrane_path}")

        # Validate with trimesh
        mesh = trimesh.load(stl_path)
        is_watertight = mesh.is_watertight
        print(f"     Watertight Validation: {is_watertight} (Faces: {len(mesh.faces)}, Vertices: {len(mesh.vertices)})")
        if is_watertight:
            success_count += 1

print("\n=======================================================")
print(f"Build Complete! {success_count} / {len(SIZES) * len(STYLES)} models verified watertight.")
print("=======================================================")
