# Metrics Method - Quinn Keaveney

# Step 2
# spaced l visually ex.nlololnlnloln

f = CurrentFont()

# Optically set sides
rightl = f["l"].rightMargin
leftl = f["l"].leftMargin

# Automate for simular sides
f["b"].leftMargin = leftl
f["h"].leftMargin = leftl
f["k"].leftMargin = leftl

f["d"].rightMargin = rightl

f.update()