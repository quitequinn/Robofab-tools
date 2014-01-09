# Debugging Space - Quinn Keaveney

from robofab.world import CurrentFont
f = CurrentFont()

for i in f:
    if i.selected == 0:
        continue
    print i
    print i.components
    for c in i.components:
        print c
        i.components[1].move((0, 100))
    if 'dotbelow' in i.components:
        print 'Found it...'
        print 'KILL IT WITH FIRE!'
    else:
        print '...only so I know I\'m wrong.'
    
# Usefull to display what your targeting - i.move((0, 100)) - and FIRE
