# Skew Glyphs - Quinn Keaveney

from robofab.world import CurrentFont
f = CurrentFont()

for i in f:
    if i.selected == 0:
        continue
    print i
    i.skew(6.9)
    
# Usefull to display what your targeting - i.move((0, 100)) - and FIRE
