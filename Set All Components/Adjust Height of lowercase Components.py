#adjust height of top resting lowercase accents - Quinn Keaveney
height = -50

f = CurrentFont()
moveThese=['acute', 'grave', 'hungarumlaut', 'doublegrave', 'circumflex', 'caron', 'dieresis', 'tilde', 'ring', 'macron', 'breve', 'invertedbreve', 'dotaccent', 'commaabovecmb', 'slashaccent']

for i in f:
    i.mark = 0
for i in moveThese:
    f[i].move((0, height))
    f[i].mark = 1

f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'