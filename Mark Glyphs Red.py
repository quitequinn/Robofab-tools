# Print Glyph Names with Unicode - Quinn Keaveney

from robofab.world import CurrentFont
f = CurrentFont()

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in f:
    if i.selected == 0:
        continue
    f[i.name].mark = 1

f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'