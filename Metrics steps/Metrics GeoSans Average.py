# Find "typical" GeoSans Shoulder Widths - Quinn Keaveney

# Counter Width of H
cw = 248 

f = CurrentFont()

f["O"].leftMargin = (cw * 0.18)/2
f["O"].rightMargin = (cw * 0.18)/2

f["H"].leftMargin = (cw * 0.46)/2
f["H"].rightMargin = (cw * 0.46)/2

f["A"].leftMargin = 0
f["J"].leftMargin = (cw * 0.02)/2
f["S"].leftMargin = (cw * 0.12)/2
f["T"].leftMargin = (cw * 0.05)/2
f["V"].leftMargin = 0
f["W"].leftMargin = (cw * 0.02)/2
f["X"].leftMargin = (cw * 0.01)/2
f["Y"].leftMargin = -(cw * 0.02)/2
f["Z"].leftMargin = (cw * 0.25)/2

f["A"].rightMargin = 0
f["B"].rightMargin = (cw * 0.08)/2
f["C"].rightMargin = 0
f["E"].rightMargin = (cw * 0.2)/2
f["F"].rightMargin = (cw * 0.15)/2
f["G"].rightMargin = (cw * 0.18)/2
f["K"].rightMargin = 0
f["L"].rightMargin = (cw * 0.1)/2
f["P"].rightMargin = (cw * 0.05)/2
f["Q"].rightMargin = (cw * 0.08)/2
f["R"].rightMargin = 0
f["S"].rightMargin = (cw * 0.15)/2
f["T"].rightMargin = (cw * 0.05)/2
f["V"].rightMargin = 0
f["W"].rightMargin = (cw * 0.02)/2
f["X"].rightMargin = (cw * 0.01)/2
f["Y"].rightMargin = -(cw * 0.02)/2
f["Z"].rightMargin = (cw * 0.25)/2


f.update() 