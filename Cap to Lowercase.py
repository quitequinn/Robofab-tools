# Caps to lowercase
# ex. You have a just uppercase font

f = CurrentFont()

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in characters:
    f[i] = f[i.lower()]
    #or to caps
    #f[i] = f[i.capatalize()]

f.update() 