# Align Middle of Glyph to Left Shoulder - Quinn Keaveney

from robofab.world import CurrentFont
f = CurrentFont()

for i in f:
    if i.selected == 0:
        continue
    w = f[i.name].width
    f[i.name].move((-(w/2), 0))

f.update() 
print ''
print 'Digested by Python.'
