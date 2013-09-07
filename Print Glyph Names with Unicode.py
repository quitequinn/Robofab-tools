# Print Glyph Names with Unicode
from robofab.world import CurrentFont
f = CurrentFont()
g = ''
selected = []
og = ''
ordered = f.glyphOrder

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

print 'This is the unicode selected list'
print g[:-2]
print 'This is your ordered selected list'
print og[:-2]
print 'Digested by Python.'