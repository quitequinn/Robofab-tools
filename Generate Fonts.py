# Generate Folder of Fonts - Quinn Keaveney

o = OpenFont()

for f in o: 
    f.generate(f.path[:-4]+'.otf', 'otf', decompose=False, checkOutlines=False, autohint=True, releaseMode=True, glyphOrder=None, progressBar=None)
    
print ''
print 'Digested by Python.'