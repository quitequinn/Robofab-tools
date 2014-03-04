# swap glyphs - Quinn Keaveney's edit of Mark Simonson 

from robofab.world import CurrentFont
f = CurrentFont()

listOne = ['zero', 'zero.pzero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
listTwo = ['zero.tnum', 'zero.tzero', 'one.tnum', 'two.tnum', 'three.tnum', 'four.tnum', 'five.tnum', 'six.tnum', 'seven.tnum', 'eight.tnum', 'nine.tnum']
	
listTemp = [] 
for i in listOne:
	listTemp.append(i + ".temp")

l = len(listOne)

def setGlyphNames(listA, listB):
	i = 0
	while i < l:
		g = f[listA[i]]
		g.name = listB[i]
		g.update()
		g.autoUnicodes()
		g.update()
		i = i+1
		
if len(listOne) == len(listTwo):
	setGlyphNames(listOne, listTemp) # a -> a.temp
	setGlyphNames(listTwo, listOne)  # A -> a
	setGlyphNames(listTemp, listTwo) # a.temp -> A
	f.update
	print 'Done! %d pairs of glyphs swapped.' % l
else:
	print "Can't run. Lists are not equal."

print ''
print 'Digested by Python.'
#exemption = 'zero.tzero'