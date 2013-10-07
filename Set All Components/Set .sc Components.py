#add components to their .sc versions - Quinn Keaveney
height = 20


f = CurrentFont()
lowercase = ['acute', 'grave', 'hungarumlaut', 'doublegrave', 'circumflex', 'caron', 'dieresis', 'tilde', 'ring', 'macron', 'breve', 'invertedbreve', 'dotaccent', 'linebelow', 'dotbelow', 'dotabove', 'underlineaccent', 'commaaccent', 'cedilla', 'altcedilla', 'ogonek', 'altogonek', 'commaabovecmb', 'commaaccent', 'croat.cap']
cap = ['acute.sc', 'grave.sc', 'hungarumlaut.sc', 'doublegrave.sc', 'circumflex.sc', 'caron.sc', 'dieresis.sc', 'tilde.sc', 'ring.sc', 'macron.sc', 'breve.sc', 'invertedbreve.sc', 'dotaccent.sc', 'dotbelow.sc', 'dotabove.sc', 'linebelow.sc',  'cedilla.sc', 'altcedilla.sc', 'ogonek.sc', 'altogonek.sc', 'commaabovecmb.sc', 'croat.cap', 'commaaccent.sc']
moveup=['acute.sc', 'grave.sc', 'hungarumlaut.sc', 'doublegrave.sc', 'circumflex.sc', 'caron.sc', 'dieresis.sc', 'tilde.sc', 'ring.sc', 'macron.sc', 'breve.sc', 'invertedbreve.sc', 'dotaccent.sc', 'dotabove.sc', 'commaabovecmb.sc']

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in cap:
    low = i[:-3]
    f.newGlyph(i)
    f[i].appendComponent(low)
    if i == moveup:
        f[i].move((0, height))
        f[i].width = f[low].width
    f[i].mark = 1

f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'