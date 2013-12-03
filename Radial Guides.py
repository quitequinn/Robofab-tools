# Add Radial Guides - Quinn Keaveney
g = CurrentGlyph()
ancs = []
gd = []

for angle in range(0, 180, 15):
    gd.append("Radial {0}deg".format(angle))

for a in g.anchors:
    b = a.name
    ancs.append(b)
    
if 'Radial Guide' not in ancs:
    g.appendAnchor("Radial Guide", (500, 500))

for a in g.guides:
    if a.name in gd:
        g.removeGuide(a)

for a in g.anchors:
    if a.name == 'Radial Guide':
        x = a.x
        y = a.y
        for angle in range(0, 180, 15):
            g.addGuide((x, y), angle, name=("Radial {0}deg".format(angle)))
            guide = g.addGuide((x, y), angle, name=("Radial {0}deg".format(angle)))
            guide.naked().showMeasurements = True

CurrentFont().update() 


print ''
print 'Digested by Python.'