#add components to their .cap versions - Quinn Keaveney
height = 400


f = CurrentFont()
lowercase = ['acute', 'grave', 'hungarumlaut', 'doublegrave', 'circumflex', 'caron', 'dieresis', 'tilde', 'ring', 'macron', 'breve', 'invertedbreve', 'dotaccent', 'linebelow', 'dotbelow', 'dotabove', 'underlineaccent', 'commaaccent', 'cedilla', 'altcedilla', 'ogonek', 'altogonek', 'commaabovecmb','commaaccent', 'croat']
cap = ['acute.cap', 'grave.cap', 'hungarumlaut.cap', 'doublegrave.cap', 'circumflex.cap', 'caron.cap', 'dieresis.cap', 'tilde.cap', 'ring.cap', 'macron.cap', 'breve.cap', 'invertedbreve.cap', 'dotaccent.cap', 'dotbelow.cap', 'dotabove.cap', 'linebelow.cap',  'cedilla.cap', 'altcedilla.cap', 'ogonek.cap', 'altogonek.cap', 'commaabovecmb.cap', 'commaaccent.cap', 'croat.cap']
moveup=['acute.cap', 'grave.cap', 'hungarumlaut.cap', 'doublegrave.cap', 'circumflex.cap', 'caron.cap', 'dieresis.cap', 'tilde.cap', 'ring.cap', 'macron.cap', 'breve.cap', 'invertedbreve.cap', 'dotaccent.cap', 'dotabove.cap', 'commaabovecmb.cap']

for i in cap:
    low = i[:-4]
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