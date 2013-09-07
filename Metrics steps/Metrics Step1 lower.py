# Metrics Method - Quinn Keaveney

# Step 1
# spaced n and o visually ex.noonnon

f = CurrentFont()

# Optically set sides
righto = f["o"].rightMargin
lefto = f["o"].leftMargin
rightn = f["n"].rightMargin
leftn = f["n"].leftMargin

# Automate for simular sides
f["c"].leftMargin = lefto
f["d"].leftMargin = lefto
f["r"].leftMargin = lefto
f["q"].leftMargin = lefto
f["e"].leftMargin = lefto

f["p"].rightMargin = righto
f["b"].rightMargin = righto

f["m"].rightMargin = rightn
f["u"].leftMargin = rightn
f["i"].rightMargin = rightn
f["j"].rightMargin = rightn
f["h"].rightMargin = rightn
f["a"].rightMargin = rightn

f["m"].leftMargin = leftn
f["u"].rightMargin = leftn
f["p"].leftMargin = leftn
f["i"].leftMargin = leftn
f["j"].leftMargin = leftn
f["r"].leftMargin = leftn

f.update() 