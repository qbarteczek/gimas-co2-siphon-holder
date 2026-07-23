// ==============================================================================
// GIMAS Siphon CO2 Cartridge Holder Generator
// Parametric OpenSCAD design for 8g and 12g CO2 Seltzer Siphon Holders
// Genuine GIMAS M20.7 Female Thread & Solid Top Cap
// ==============================================================================

size = "12g"; // "8g" or "12g"
style = 1;     // 1: Modern Minimalist, 2: Knurled, 3: Fluted, 4: Spiral
$fn = 60;

// Dimensions calculation based on size
total_length = (size == "8g") ? 73 : 90;
label_text   = (size == "8g") ? "8g" : "12g";

// Helper module: main cylinder with smooth hemispherical dome top cap ("półokrągła czapeczka")
module base_body_with_dome(len) {
    union() {
        cylinder(r1=13, r2=15, h=3);
        translate([0, 0, 3]) cylinder(r=15, h=max(0, len - 3 - 15));
        translate([0, 0, len - 15]) sphere(r=15, $fn=60);
    }
}

// -------------------------------------------------------------
// STYL 1: Modern Minimalist (Opływowy z 2 łopatkami i półokrągłą czapeczką)
// -------------------------------------------------------------
module style_modern(len) {
    union() {
        base_body_with_dome(len);
        for (i=[0, 180]) {
            rotate([0, 0, i]) translate([13, 0, 0])
            hull() {
                translate([0, -4, 20]) cylinder(r=1, h=max(0, len-36));
                translate([0, 4, 20]) cylinder(r=1, h=max(0, len-36));
                translate([8, -1.5, 22]) sphere(r=2.5, $fn=24);
                translate([8, 1.5, 22]) sphere(r=2.5, $fn=24);
                translate([8, -1.5, len-16]) sphere(r=2.5, $fn=24);
                translate([8, 1.5, len-16]) sphere(r=2.5, $fn=24);
            }
        }
    }
}

// -------------------------------------------------------------
// STYL 2: Industrial Knurled (Radełkowany z półokrągłą czapeczką)
// -------------------------------------------------------------
module style_knurled(len) {
    union() {
        base_body_with_dome(len);
        for (a=[0:15:345]) {
            rotate([0, 0, a]) translate([14.8, 0, 10]) cylinder(r=1.2, h=len-25, $fn=20);
        }
        rotate([0, 0, 0]) translate([13.5, -7, len/2 - 20]) cube([3, 14, 40]);
    }
}

// -------------------------------------------------------------
// STYL 3: Retro Fluted (Klasyczne bruzdy z półokrągłą czapeczką)
// -------------------------------------------------------------
module style_fluted(len) {
    difference() {
        base_body_with_dome(len);
        for (a=[0:30:330]) {
            if (a != 0 && a != 180) {
                rotate([0, 0, a]) translate([15, 0, 10]) cylinder(r=2.5, h=len-25, $fn=20);
            }
        }
    }
}

// -------------------------------------------------------------
// STYL 4: Ergonomic Spiral (Futurystyczny świder z półokrągłą czapeczką)
// -------------------------------------------------------------
module style_spiral(len) {
    union() {
        base_body_with_dome(len);
        intersection() {
            cylinder(r=16.8, h=len);
            translate([0, 0, 10])
            linear_extrude(height=len-25, twist=160, $fn=36) {
                circle(r=15, $fn=36);
                for (a=[0:45:315]) {
                    rotate([0, 0, a]) translate([15, 0]) circle(r=2.2, $fn=16);
                }
            }
        }
    }
}

module sleeve_shell(len, stl_style, text_str) {
    difference() {
        if (stl_style == 1) style_modern(len);
        else if (stl_style == 2) style_knurled(len);
        else if (stl_style == 3) style_fluted(len);
        else if (stl_style == 4) style_spiral(len);
        else style_modern(len);
        
        // Hollow core to wrap genuine base
        translate([0, 0, -1]) cylinder(r=12.5, h=len+2);
        
        // Debossed vertical text
        rotate([0, 0, 0]) translate([14.6, 0, len/2]) rotate([90, 0, 90]) rotate([0, 0, -90])
        linear_extrude(height=5) text(text_str, size=8, font="Liberation Sans:style=Bold", halign="center", valign="center");
    }
}

// Master module combining genuine GIMAS siphon base (with M20.7 thread & solid top) and aesthetic sleeve
module gimas_co2_holder(total_len, stl_style, text_str) {
    union() {
        // Genuine GIMAS Siphon Base with M20.7 Female Thread & Internal Cavity
        if (size == "8g") {
            import("base_8g.stl");
        } else {
            import("base_12g.stl");
        }
        
        // Outer aesthetic sleeve aligned to base
        translate([0, 0, 13.5]) 
        rotate([-90, 0, 0]) 
        translate([0, 0, (size == "8g") ? -41.24 : -58.24]) 
        sleeve_shell(total_len, stl_style, text_str);
    }
}

gimas_co2_holder(total_length, style, label_text);
