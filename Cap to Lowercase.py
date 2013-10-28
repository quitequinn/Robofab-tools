# Caps to lowercase - Quinn Keaveney
# ex. You have a just uppercase font

f = CurrentFont()

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in characters:
    char = i.lower()
    f[char].appendComponent(i)
    f[char].width = f[i].width

    f[char].mark = 1

f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'