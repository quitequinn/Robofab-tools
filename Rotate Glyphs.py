# Rotate Glyphs - Quinn Keaveney

from robofab.world import CurrentFont
f = CurrentFont()

for i in f:
    w = f[i.name].width
    f[i.name].move((-(w/2), 0))
    f[i.name].rotate(-14)
    f[i.name].move(((w/2), 0))


f.update() 
print ''
print 'Digested by Python.'