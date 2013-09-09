#add components to their .cap versions
f = CurrentFont()

lowercase = ['acute', 'grave', 'hungarumlaut', 'doublegrave', 'circumflex', 'caron', 'dieresis', 'tilde', 'ring', 'macron', 'breve', 'invertedbreve', 'dotaccent', 'linebelow', 'dotbelow', 'underlineaccent', 'commaaccent', 'cedilla', 'altcedilla', 'ogonek', 'altogonek', 'commaabovecmb','commaaccent']
cap = ['acute.cap', 'grave.cap', 'hungarumlaut.cap', 'doublegrave.cap', 'circumflex.cap', 'caron.cap', 'dieresis.cap', 'tilde.cap', 'ring.cap', 'macron.cap', 'breve.cap', 'invertedbreve.cap', 'dotaccent.cap', 'dotbelow.cap', 'linebelow.cap',  'cedilla.cap', 'altcedilla.cap', 'ogonek.cap', 'altogonek.cap', 'commaabovecmb.cap', 'commaaccent.cap']
moveup=['acute.cap', 'grave.cap', 'hungarumlaut.cap', 'doublegrave.cap', 'circumflex.cap', 'caron.cap', 'dieresis.cap', 'tilde.cap', 'ring.cap', 'macron.cap', 'breve.cap', 'invertedbreve.cap', 'dotaccent.cap', 'commaabovecmb.cap']
height = 400

for i in cap:
    low = i[:-4]
    f.newGlyph(i)
    f[i].appendComponent(low)
    if i == moveup:
        f[i].move((0, height))
        f[i].width = f[low].width

f.update() 
print 'Digested by Python.'