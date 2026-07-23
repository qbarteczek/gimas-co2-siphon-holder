// ==============================================================================
// GIMAS Siphon CO2 Cartridge Holder Generator
// Parametric OpenSCAD design for 8g and 12g CO2 Seltzer Siphon Holders
// 100% Watertight Manifold Geometry with M20.7 Female Thread
// ==============================================================================

// Default parameters (can be overridden via command line -D)
size = "12g"; // "8g" or "12g"
style = 1;     // 1: Modern Minimalist, 2: Knurled, 3: Tactical Hex, 4: Fluted, 5: Spiral
$fn = 60;

// Dimensions calculation based on size
total_length = (size == "8g") ? 73 : 90;
cav_depth    = (size == "8g") ? 53 : 70;
label_text   = (size == "8g") ? "8g" : "12g";

module thread_2d_female(d=20.7, pitch=2.0) {
    circle(r=d/2 + 0.5, $fn=48);
    for (i=[0:11]) {
        rotate([0, 0, i*30])
        translate([d/2 + 0.2, 0])
        square([1.6, 1.3], center=true);
    }
}

// -------------------------------------------------------------
// STYL 1: Modern Minimalist (Opływowy z 2 łopatkami)
// -------------------------------------------------------------
module style_modern(len) {
    union() {
        cylinder(r=15, h=len);
        translate([0, 0, len-3]) cylinder(r1=15, r2=13, h=3);
        for (i=[0, 180]) {
            rotate([0, 0, i]) translate([13, 0, 0])
            hull() {
                translate([0, -4, 0]) cylinder(r=1, h=len);
                translate([0, 4, 0]) cylinder(r=1, h=len);
                translate([8, -1.5, 4]) sphere(r=2.5, $fn=30);
                translate([8, 1.5, 4]) sphere(r=2.5, $fn=30);
                translate([8, -1.5, len-4]) sphere(r=2.5, $fn=30);
                translate([8, 1.5, len-4]) sphere(r=2.5, $fn=30);
            }
        }
    }
}

// -------------------------------------------------------------
// STYL 2: Industrial Knurled (Radełkowany chwyt techniczny)
// -------------------------------------------------------------
module style_knurled(len) {
    union() {
        cylinder(r=15, h=len);
        translate([0, 0, len-3]) cylinder(r1=15, r2=13, h=3);
        for (a=[0:15:345]) {
            rotate([0, 0, a]) translate([14.8, 0, 8]) cylinder(r=1.2, h=len-16, $fn=24);
        }
        // Flat plaque for debossed text
        rotate([0, 0, 0]) translate([13.5, -7, 8]) cube([3, 14, len-16]);
    }
}

// -------------------------------------------------------------
// STYL 3: Tactical Hexagon (Pancerna sześciokątna forma)
// -------------------------------------------------------------
module style_hexagon(len) {
    union() {
        cylinder(r=16, h=len, $fn=6);
        translate([0, 0, len-3]) cylinder(r1=16, r2=13, h=3, $fn=6);
        for (i=[0, 180]) {
            rotate([0, 0, i+30]) translate([14, 0, 0])
            hull() {
                translate([0, -3, 0]) cylinder(r=1, h=len);
                translate([0, 3, 0]) cylinder(r=3, h=len);
                translate([6, 0, 4]) sphere(r=2, $fn=24);
                translate([6, 0, len-4]) sphere(r=2, $fn=24);
            }
        }
    }
}

// -------------------------------------------------------------
// STYL 4: Retro Fluted (Klasyczne bruzdy w stylu vintage)
// -------------------------------------------------------------
module style_fluted(len) {
    difference() {
        union() {
            cylinder(r=15, h=len);
            translate([0, 0, len-3]) cylinder(r1=15, r2=13, h=3);
        }
        for (a=[0:30:330]) {
            if (a != 0 && a != 180) {
                rotate([0, 0, a]) translate([15, 0, 8]) cylinder(r=2.5, h=len-16, $fn=24);
            }
        }
    }
}

// -------------------------------------------------------------
// STYL 5: Ergonomic Spiral (Futurystyczny świder chwytny)
// -------------------------------------------------------------
module style_spiral(len) {
    union() {
        cylinder(r=15, h=len);
        translate([0, 0, len-3]) cylinder(r1=15, r2=13, h=3);
        intersection() {
            cylinder(r=16.8, h=len);
            translate([0, 0, 8])
            linear_extrude(height=len-16, twist=160, $fn=48) {
                circle(r=15, $fn=48);
                for (a=[0:45:315]) {
                    rotate([0, 0, a]) translate([15, 0]) circle(r=2.2, $fn=20);
                }
            }
        }
    }
}

// -------------------------------------------------------------
// MASTER MODULE
// -------------------------------------------------------------
module gimas_co2_holder(total_len, depth, stl_style, text_str) {
    difference() {
        // Outer aesthetic shell
        if (stl_style == 1) style_modern(total_len);
        else if (stl_style == 2) style_knurled(total_len);
        else if (stl_style == 3) style_hexagon(total_len);
        else if (stl_style == 4) style_fluted(total_len);
        else if (stl_style == 5) style_spiral(total_len);
        else style_modern(total_len);

        // 1. M20.7x2 female thread at bottom for GIMAS siphon (height 16mm)
        translate([0, 0, -0.5])
        linear_extrude(height=16, twist=-360*(16/2.0), $fn=48)
            thread_2d_female(20.7, 2.0);
            
        // Bottom mouth lead-in chamfer
        translate([0, 0, -1]) 
            cylinder(r1=15.0, r2=12.2, h=3.0);
            
        // 2. Internal Cartridge Cavity (19.2mm diameter = 9.6mm radius)
        translate([0, 0, 15]) 
            cylinder(r=9.6, h=depth);
            
        // Internal top dome (pushes cartridge neck into siphon needle)
        translate([0, 0, 15 + depth]) 
            sphere(r=9.6, $fn=40);
            
        // 3. Debossed Vertical Text
        text_r = (stl_style == 1 || stl_style == 2 || stl_style == 4 || stl_style == 5) ? 14.6 : 13.8;
        text_angle = (stl_style == 3) ? 90 : 0;
        
        rotate([0, 0, text_angle])
        translate([text_r, 0, total_len/2])
        rotate([90, 0, 90])
        rotate([0, 0, -90])
        linear_extrude(height=5)
        text(text_str, size=8, font="Liberation Sans:style=Bold", halign="center", valign="center");
    }
}

// Generate current configuration
gimas_co2_holder(total_length, cav_depth, style, label_text);
