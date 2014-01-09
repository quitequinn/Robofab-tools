# Generate Lowercase Components - Quinn Keaveney

f = CurrentFont()

secondAccentHeight = 300
ascenderHeight = 500

normglyphs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Eng', 'Thorn', 'Eth', 'Ezh', 'ae']

accentglyphs = ['aacute', 'agrave', 'acircumflex', 'adieresis', 'atilde', 'aring', 'acaron', 'amacron', 'abreve', 'ainvertedbreve', 'adoublegrave', 'adotaccent', 'aringacute', 'adieresismacron', 'aogonek', 'ae', 'aeacute', 'aemacron', 'cacute', 'ccircumflex', 'ccaron', 'cdotaccent', 'ccedilla', 'dcaron', 'dcedilla', 'ddotbelow', 'dcroat', 'eacute', 'egrave', 'ecircumflex', 'edieresis', 'ecaron', 'emacron', 'ebreve', 'einvertedbreve', 'edoublegrave', 'edotaccent', 'eacutedotbelow', 'egravedotbelow', 'eogonek', 'gacute', 'gcircumflex', 'gcaron', 'gbreve', 'gdotaccent', 'gcommaaccent', 'gstroke', 'hcircumflex', 'hcaron', 'hdotbelow', 'hmacronbelow', 'hbar', 'dotlessi', 'iacute', 'igrave', 'icircumflex', 'idieresis', 'itilde', 'icaron', 'imacron', 'ibreve', 'iinvertedbreve', 'idoublegrave', 'idotaccent', 'idotbelow', 'iogonek', 'dotlessj', 'jcircumflex', 'jcaron', 'kcaron', 'kcommaaccent', 'kcedilla', 'khook', 'kgreenlandic', 'lacute', 'lcaron', 'lcommaaccent', 'lcedilla', 'ldotbelow', 'ldotbelowmacron', 'ldot', 'lslash', 'mmacron', 'mcedilla', 'mdotbelow', 'nacute', 'ngrave', 'ndieresis', 'ntilde', 'ncaron', 'nmacron', 'ndotaccent', 'ncommaaccent', 'ncedilla', 'ndotbelow', 'ndescender', 'oacute', 'ograve', 'ocircumflex', 'odieresis', 'otilde', 'ocaron', 'omacron', 'obreve', 'oinvertedbreve', 'ohungarumlaut', 'odoublegrave', 'ocommaabovecmb', 'otildemacron', 'odotaccent', 'odotaccentmacron', 'ocedilla', 'odotbelow', 'olinebelow', 'oogonek', 'oogonekmacron', 'oslash', 'oslashacute', 'obar', 'oe', 'pmacron', 'racute', 'rcaron', 'rinvertedbreve', 'rdoublegrave', 'rcommaaccent', 'rcedilla', 'rdotbelow', 'rdotbelowmacron', 'sacute', 'scircumflex', 'scaron', 'scommaaccent', 'scedilla', 'sdotbelow', 'germandbls', 'tcaron', 'tcommaaccent', 'tcedilla', 'tdotbelow', 'tbar', 'uacute', 'ugrave', 'ucircumflex', 'udieresis', 'utilde', 'uring', 'ucaron', 'umacron', 'ubreve', 'uinvertedbreve', 'uhungarumlaut', 'udoublegrave', 'uogonek', 'udotbelow', 'umacronbelow', 'wacute', 'wgrave', 'wcircumflex', 'wdieresis', 'yacute', 'ygrave', 'ycircumflex', 'ydieresis', 'ytilde', 'zacute', 'zcaron', 'zdotaccent', 'eng', 'thorn', 'eth', 'ezh', 'ezhcaron', 'schwa']

accents = ['acute', 'grave', 'hungarumlaut', 'doublegrave', 'circumflex', 'caron', 'dieresis', 'tilde', 'ring', 'macron', 'macronbelow', 'breve', 'invertedbreve', 'dotaccent', 'dotaccent', 'dotbelow', 'dotabove', 'linebelow', 'commaaccent', 'cedilla', 'altcedilla', 'ogonek', 'altogonek', 'commaabovecmb', 'croat', 'stroke', 'slashaccent', 'descender', 'bar']


for i in CurrentFont().glyphOrder:
    # Remove marks
    CurrentFont()[i].mark = 0
for i in accentglyphs:
    for accent in accents:
        # I wanted to keep the same system with .cap and .sc
        sintaxless = accent
        if sintaxless in i:
            if sintaxless is 'bar':
                sintaxless = 'baraccent'  
            accentless = i.replace(sintaxless,'')
            if accentless in normglyphs:
                f.newGlyph(i)
                if 'i' in accentless and (accent is 'dotbelow' or accent is 'ogonek'):
                    f[i].appendComponent('i')
                elif 'i' in accentless:
                    f[i].appendComponent('dotlessi')
                elif 'j' in accentless:
                    f[i].appendComponent('dotlessj')
                elif 'g' in accentless:
                    f[i].appendComponent('g_alt')
                else:
                    f[i].appendComponent(accentless)
                
                # centers first component to left shoulder
                w = f[i].width
                f[i].move((-(w/2), 0))
                
                f[i].appendComponent(accent)
                f[i].width = f[accentless].width   
                if ('l' in accentless) or ('h' in accentless) or ('k' in accentless) :                    
                    # or operator isnt working for some reason
                    if 'dotbelow' is not accent:
                        if 'commaaccent' is not accent:
                            if 'cedilla' is not accent:
                                f[i].components[1].move((0, ascenderHeight))
    
                # recenters components         
                f[i].move(((w/2), 0))
                
                print i + ' = ' + accentless + ' with ' + accent
                f[i].mark = 1

            else:
                for accent2 in accents:
                    sintaxless2 = accent2.replace('','')
                    if sintaxless2 in accentless:
                        accentless2 = accentless.replace(sintaxless2,'')
                        if accentless2 in normglyphs:
                            f.newGlyph(i)
                            f[i].appendComponent(accentless2)
                            w = f[i].width
                            f[i].move((-(w/2), 0))
                            f[i].appendComponent(accent)
                            f[i].appendComponent(accent2) 
                            if accentless2 is ('l' or 'h' or 'k'):
                                if accent2 is not ('dotbelow' or 'commaaccent' or 'cedilla'):
                                    f[i].components[2].move((0, ascenderHeight))                 
                                if accent is not ('dotbelow' or 'commaaccent' or 'cedilla'):
                                    f[i].components[1].move((0, ascenderHeight))                 
                            if (accent or accent2) is not ('dotbelow' or 'macron'):
                                f[i].components[2].move((0, secondAccentHeight))
                                f[i].width = f[accentless2].width
    
                            f[i].move(((w/2), 0))            
                            f[i].mark = 10
                            print i + ' = ' + accentless + ' with ' + accent + ' and ' + accent2
                            
                        else:
                            error = ('> There is a problem with ' + i + ' <').upper()
                            print error
                            print len(error) * '^'
                            
    # Exceptions that you need to fix                    
    if i is 'khook':

        f[i].width = f['k'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50 
    if i is 'oslash':

        f[i].width = f['o'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50 
    if i is 'lslash':

        f[i].width = f['l'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50 
    if i is 'gstroke':

        f[i].width = f['g'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50 
                
    # Exceptions that will work out in the end  
    if i is 'dcaron':
        f.newGlyph(i)
        f[i].appendComponent('d')
        w = f[i].width
        f[i].move((-(w/2), 0))
        f[i].appendComponent('caron_alt')
        f[i].width = f['d'].width
        f[i].move(((w/2), 0))
        f[i].mark = 25   
    if i is 'tcaron':
        f.newGlyph(i)
        f[i].appendComponent('t')
        w = f[i].width
        f[i].move((-(w/2), 0))
        f[i].appendComponent('caron_alt')
        f[i].width = f['t'].width
        f[i].move(((w/2), 0))
        f[i].mark = 25     
    if i is 'oslashacute':
        f.newGlyph(i)
        f[i].appendComponent('oslash')
        w = f[i].width
        f[i].move((-(w/2), 0))
        f[i].appendComponent('acute')
        f[i].width = f['o'].width
        f[i].move(((w/2), 0))
        f[i].mark = 25
    if i is 'gcommaaccent':
        f.newGlyph(i)
        f[i].appendComponent('g_alt')
        w = f[i].width
        f[i].move((-(w/2), 0))
        f[i].appendComponent('commaabovecmb')
        f[i].width = f['g'].width
        f[i].move(((w/2), 0))
        f[i].mark = 25  
    if i is 'ldot':
        f.newGlyph(i)
        f[i].appendComponent('l')
        w = f[i].width
        f[i].move((-(w/2), 0))
        f[i].appendComponent('dotaccent')
        f[i].width = f['l'].width
        f[i].move(((w/2), 0))
        f[i].mark = 25  

                            
f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'