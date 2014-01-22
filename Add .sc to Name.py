# add on .sc - Quinn Keaveney

from robofab.world import CurrentFont
f = CurrentFont()

for i in f:
    if i.selected == 0:
        continue
    i.name = i.name + '.sc'
    print i.name
    
