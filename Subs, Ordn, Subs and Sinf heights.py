# Generate Small Cap Components - Quinn Keaveney
sups = 800
ordn = 400
subs = 0
sinf = -200
baseType = '.sups'

f = CurrentFont()
baseGlyphs = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'parenleft', 'parenright', 'plus', 'minus', 'multiply', 'divide', 'equal', 'period', 'comma', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
output = ['.sups', '.ordn', '.subs', '.sinf']

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in baseGlyphs:
    for type in output:
        theGlyph = i+type
        if theGlyph != (i+baseType):
            f.newGlyph(theGlyph)
            f[theGlyph].appendComponent((i+baseType))
            f[theGlyph].width = f[i+baseType].width
            f[theGlyph].move((0, eval(type[1:])))
            f[theGlyph].mark = 1
            print i + type + ' generated from ' + i + baseType

f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'