# Print Glyph Names with Unicode - Quinn Keaveney

from robofab.world import CurrentFont
f = CurrentFont()
g = ''
selected = []
og = ''
ordered = f.glyphOrder

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in f:
    if i.selected == 0:
        continue
    if i.unicode == None:
        g += "'" + i.name + "', "
    else:
        g += "'" + i.name + "|" + unichr(i.unicode) + "', "
for i in f:
    if i.selected == 0:
        continue
    selected += [i.name]

for i in ordered:
    if i in selected:
        og += "'" + i+ "', "
        f[i].mark = 1

print 'This is the selected unicode list'
print g[:-2]
print 'This is the selected ordered list'
print og[:-2]


f.update() 
print ''
print 'Selected glyphs marked in red.'
print 'Digested by Python.'