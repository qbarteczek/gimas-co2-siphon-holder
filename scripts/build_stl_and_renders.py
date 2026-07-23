#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STL_DIR = os.path.join(PROJECT_DIR, "stl")
RENDERS_DIR = os.path.join(PROJECT_DIR, "renders")
POBRANE_DIR = "/home/qba/Pobrane"
BASE_12G_PATH = os.path.join(PROJECT_DIR, "scad", "base_12g.stl")
BASE_8G_PATH = os.path.join(PROJECT_DIR, "scad", "base_8g.stl")

# Auto-detect python venv if pymeshlab is not in default sys.path
try:
    import pymeshlab
    import trimesh
    import numpy as np
except ImportError:
    venv_python = "/home/qba/.gemini/antigravity/scratch/stl_view/venv/bin/python"
    if os.path.exists(venv_python) and sys.executable != venv_python:
        os.execv(venv_python, [venv_python] + sys.argv)
    else:
        raise RuntimeError("Missing required dependencies: pymeshlab, trimesh, numpy")

OPENSCAD_BIN = shutil.which("openscad")
if not OPENSCAD_BIN:
    APPIMAGE = "/home/qba/.gemini/antigravity/scratch/stl_view/OpenSCAD.AppImage"
    if os.path.exists(APPIMAGE):
        OPENSCAD_BIN = APPIMAGE
    else:
        raise RuntimeError("OpenSCAD binary not found!")

os.makedirs(STL_DIR, exist_ok=True)
os.makedirs(RENDERS_DIR, exist_ok=True)

# 4 Aesthetic styles
STYLES = [
    (1, "styl1_modern"),
    (2, "styl2_knurled"),
    (3, "styl3_fluted"),
    (4, "styl4_spiral"),
]

SIZES = {
    "12g": {"length": 90, "offset": -58.24, "base": BASE_12G_PATH},
    "8g":  {"length": 90, "offset": -58.24, "base": BASE_8G_PATH}
}

sleeve_scad_template = """
$fn = 60;

module base_body_with_dome(len) {{
    union() {{
        cylinder(r1=13, r2=15, h=3);
        translate([0, 0, 3]) cylinder(r=15, h=max(0, len - 3 - 15));
        translate([0, 0, len - 15]) sphere(r=15, $fn=60);
    }}
}}

// -------------------------------------------------------------
// STYL 1: Modern Minimalist
// -------------------------------------------------------------
module style_modern(len) {{
    union() {{
        base_body_with_dome(len);
        for (i=[0, 180]) {{
            rotate([0, 0, i]) translate([13, 0, 0])
            hull() {{
                translate([0, -4, 20]) cylinder(r=1, h=max(0, len-36));
                translate([0, 4, 20]) cylinder(r=1, h=max(0, len-36));
                translate([8, -1.5, 22]) sphere(r=2.5, $fn=24);
                translate([8, 1.5, 22]) sphere(r=2.5, $fn=24);
                translate([8, -1.5, len-16]) sphere(r=2.5, $fn=24);
                translate([8, 1.5, len-16]) sphere(r=2.5, $fn=24);
            }}
        }}
    }}
}}

// -------------------------------------------------------------
// STYL 2: Industrial Knurled
// -------------------------------------------------------------
module style_knurled(len) {{
    union() {{
        base_body_with_dome(len);
        for (a=[0:15:345]) {{
            rotate([0, 0, a]) translate([14.8, 0, 10]) cylinder(r=1.2, h=len-25, $fn=20);
        }}
        rotate([0, 0, 0]) translate([13.5, -7, len/2 - 20]) cube([3, 14, 40]);
    }}
}}

// -------------------------------------------------------------
// STYL 3: Retro Fluted
// -------------------------------------------------------------
module style_fluted(len) {{
    difference() {{
        base_body_with_dome(len);
        for (a=[0:30:330]) {{
            if (a != 0 && a != 180) {{
                rotate([0, 0, a]) translate([15, 0, 10]) cylinder(r=2.5, h=len-25, $fn=20);
            }}
        }}
    }}
}}

// -------------------------------------------------------------
// STYL 4: Ergonomic Spiral
// -------------------------------------------------------------
module style_spiral(len) {{
    union() {{
        base_body_with_dome(len);
        intersection() {{
            cylinder(r=16.8, h=len);
            translate([0, 0, 10])
            linear_extrude(height=len-25, twist=160, $fn=36) {{
                circle(r=15, $fn=36);
                for (a=[0:45:315]) {{
                    rotate([0, 0, a]) translate([15, 0]) circle(r=2.2, $fn=16);
                }}
            }}
        }}
    }}
}}

module sleeve_style(num, len, text_str) {{
    difference() {{
        if (num == 1) style_modern(len);
        else if (num == 2) style_knurled(len);
        else if (num == 3) style_fluted(len);
        else if (num == 4) style_spiral(len);
        
        translate([0, 0, -10]) cylinder(r=12.5, h=len+20);
        
        rotate([0, 0, 0]) translate([14.6, 0, len/2]) rotate([90, 0, 90]) rotate([0, 0, -90])
        linear_extrude(height=5) text(text_str, size=8, font="Liberation Sans:style=Bold", halign="center", valign="center");
    }}
}}

translate([0, 0, 13.5]) 
rotate([-90, 0, 0]) 
translate([0, 0, {offset}]) 
sleeve_style({style_num}, {length}, "{label_text}");
"""

# Template for rendering 3 distinct viewing angles in a single 1200x800 composite PNG image
render_3view_template = """
module item() {{
    import("{stl_path}");
}}

// 1. Widok Główny 3D (Środek - perspektywa izometryczna)
translate([0, 0, 0])
rotate([15, 0, 30])
item();

// 2. Widok Boczny / Profil (Po lewej stronie)
translate([-50, 0, 0])
rotate([90, 0, 0])
item();

// 3. Widok Gwintu M20.7 od spodu (Po prawej stronie)
translate([50, 0, 15])
rotate([145, 25, -45])
item();
"""

def render_3view(stl_path, render_path):
    scad_render_tmp = os.path.join(STL_DIR, f"render_3view_{os.path.basename(stl_path)}.scad")
    with open(scad_render_tmp, "w") as f:
        f.write(render_3view_template.format(stl_path=stl_path))

    cmd_render = [
        OPENSCAD_BIN,
        "--imgsize=1200,800",
        "--colorscheme=Sunset",
        "--camera=0,0,25,60,0,25,320",
        "-o", render_path,
        scad_render_tmp
    ]
    subprocess.run(cmd_render, check=True)
    os.remove(scad_render_tmp)

def main():
    print(f"Using OpenSCAD binary: {OPENSCAD_BIN}")
    print("Generating exact GIMAS siphon holders with 3-view composite PNG renders...")

    success_count = 0
    total_models = len(SIZES) * len(STYLES)

    for size, params in SIZES.items():
        for style_num, style_name in STYLES:
            base_name = f"gimas_co2_{size}_{style_name}"
            stl_path = os.path.join(STL_DIR, f"{base_name}.stl")
            render_path = os.path.join(RENDERS_DIR, f"{base_name}.png")

            if not os.path.exists(stl_path):
                print(f"===> Building {base_name}.stl with genuine M20.7 thread...")
                temp_scad_path = os.path.join(STL_DIR, f"temp_sleeve_{base_name}.scad")
                temp_sleeve_stl = os.path.join(STL_DIR, f"temp_sleeve_{base_name}.stl")
                
                scad_code = sleeve_scad_template.format(
                    offset=params["offset"],
                    style_num=style_num,
                    length=params["length"],
                    label_text=size
                )
                
                with open(temp_scad_path, "w") as f:
                    f.write(scad_code)

                subprocess.run([OPENSCAD_BIN, "-o", temp_sleeve_stl, temp_scad_path], check=True)
                os.remove(temp_scad_path)

                ms = pymeshlab.MeshSet()
                ms.load_new_mesh(params["base"])
                ms.load_new_mesh(temp_sleeve_stl)
                ms.generate_boolean_union(first_mesh=0, second_mesh=1)
                ms.save_current_mesh(stl_path)
                os.remove(temp_sleeve_stl)

                mesh = trimesh.load(stl_path)

                if mesh.extents[1] > mesh.extents[2]:
                    matrix = trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0])
                    mesh.apply_transform(matrix)

                z_min = mesh.bounds[0][2]
                mesh.apply_translation([0, 0, -z_min])

                center_xy = (mesh.bounds[0][:2] + mesh.bounds[1][:2]) / 2.0
                mesh.apply_translation([-center_xy[0], -center_xy[1], 0])

                mesh.export(stl_path)
                if os.path.exists(POBRANE_DIR):
                    shutil.copy2(stl_path, os.path.join(POBRANE_DIR, f"{base_name}.stl"))

            print(f"===> Rendering 3-view PNG for {base_name}.png ...")
            render_3view(stl_path, render_path)

    print("\n=======================================================")
    print(f"Build & 3-View Rendering Complete for all {total_models} models.")
    print("=======================================================")

if __name__ == "__main__":
    main()
