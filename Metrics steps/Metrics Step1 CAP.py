# Metrics Method - Quinn Keaveney

# Step 1 CAP
# spaced H and O visually ex.HOOHHOH

f = CurrentFont()

# Optically set sides
rightO = f["O"].rightMargin
leftO = f["O"].leftMargin
rightH = f["H"].rightMargin
leftH = f["H"].leftMargin

# Automate for simular sides
f["G"].leftMargin = leftO
f["Q"].leftMargin = leftO
f["C"].leftMargin = leftO

f["D"].rightMargin = rightO
f["Q"].rightMargin = rightO

f["I"].rightMargin = rightH
f["M"].rightMargin = rightH
f["N"].rightMargin = rightH
f["J"].rightMargin = rightH
f["U"].rightMargin = rightH

f["I"].leftMargin = leftH
f["M"].leftMargin = leftH
f["N"].leftMargin = leftH
f["L"].leftMargin = leftH
f["J"].leftMargin = leftH
f["K"].leftMargin = leftH
f["F"].leftMargin = leftH
f["E"].leftMargin = leftH
f["B"].leftMargin = leftH
f["D"].leftMargin = leftH
f["P"].leftMargin = leftH
f["R"].leftMargin = leftH
f["U"].leftMargin = leftH
