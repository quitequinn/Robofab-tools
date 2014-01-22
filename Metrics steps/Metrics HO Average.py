# Find "typical" Shoulder Widths - Quinn Keaveney

# Counter Width of H
cw = 248 

f = CurrentFont()

f["O"].leftMargin = (cw * 0.18)/2
f["O"].rightMargin = (cw * 0.18)/2

f["H"].leftMargin = (cw * 0.46)/2
f["H"].rightMargin = (cw * 0.46)/2

f.update() 