# Generate Lowercase Components - Quinn Keaveney

f = CurrentFont()

normglyphs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Eng', 'Thorn', 'Eth', 'Ezh', 'ae']

accentglyphs = ['aacute', 'agrave', 'acircumflex', 'adieresis', 'atilde', 'aring', 'acaron', 'amacron', 'abreve', 'ainvertedbreve', 'adoublegrave', 'adotaccent', 'aringacute', 'adieresismacron', 'aogonek', 'ae', 'aeacute', 'aemacron', 'cacute', 'ccircumflex', 'ccaron', 'cdotaccent', 'ccedilla', 'dcaron', 'dcedilla', 'ddotbelow', 'dcroat', 'eacute', 'egrave', 'ecircumflex', 'edieresis', 'ecaron', 'emacron', 'ebreve', 'einvertedbreve', 'edoublegrave', 'edotaccent', 'eacutedotbelow', 'egravedotbelow', 'eogonek', 'gacute', 'gcircumflex', 'gcaron', 'gbreve', 'gdotaccent', 'gcommaaccent', 'gstroke', 'hcircumflex', 'hcaron', 'hdotbelow', 'hmacronbelow', 'hbar', 'dotlessi', 'iacute', 'igrave', 'icircumflex', 'idieresis', 'itilde', 'icaron', 'imacron', 'ibreve', 'iinvertedbreve', 'idoublegrave', 'idotaccent', 'idotbelow', 'iogonek', 'dotlessj', 'jcircumflex', 'jcaron', 'kcaron', 'kcommaaccent', 'kcedilla', 'khook', 'kgreenlandic', 'lacute', 'lcaron', 'lcommaaccent', 'lcedilla', 'ldotbelow', 'ldotbelowmacron', 'ldot', 'lslash', 'mmacron', 'mcedilla', 'mdotbelow', 'nacute', 'ngrave', 'ndieresis', 'ntilde', 'ncaron', 'nmacron', 'ndotaccent', 'ncommaaccent', 'ncedilla', 'ndotbelow', 'ndescender', 'oacute', 'ograve', 'ocircumflex', 'odieresis', 'otilde', 'ocaron', 'omacron', 'obreve', 'oinvertedbreve', 'ohungarumlaut', 'odoublegrave', 'ocommaturnedabove', 'otildemacron', 'odotabove', 'odotabovemacron', 'ocedilla', 'odotbelow', 'ounderlineaccent', 'oogonek', 'oogonekmacron', 'oslash', 'oslashacute', 'obar', 'oe', 'pmacron', 'racute', 'rcaron', 'rinvertedbreve', 'rdoublegrave', 'rcommaaccent', 'rcedilla', 'rdotbelow', 'rdotbelowmacron', 'sacute', 'scircumflex', 'scaron', 'scommaaccent', 'scedilla', 'sdotbelow', 'germandbls', 'tcaron', 'tcommaaccent', 'tcedilla', 'tdotbelow', 'tbar', 'uacute', 'ugrave', 'ucircumflex', 'udieresis', 'utilde', 'uring', 'ucaron', 'umacron', 'ubreve', 'uinvertedbreve', 'uhungarumlaut', 'udoublegrave', 'uogonek', 'udotbelow', 'umacronbelow', 'wacute', 'wgrave', 'wcircumflex', 'wdieresis', 'yacute', 'ygrave', 'ycircumflex', 'ydieresis', 'ytilde', 'zacute', 'zcaron', 'zdotaccent', 'eng', 'thorn', 'eth', 'ezh', 'ezhcaron', 'schwa']

accents = ['acute', 'grave', 'hungarumlaut', 'doublegrave', 'circumflex', 'caron', 'dieresis', 'tilde', 'ring', 'macron', 'macronbelow', 'breve', 'invertedbreve', 'dotaccent', 'dotaccent', 'dotbelow', 'dotabove', 'linebelow', 'commaaccent', 'cedilla', 'altcedilla', 'ogonek', 'altogonek', 'commaabovecmb', 'croat', 'stroke', 'slashaccent', 'descender', 'bar']


for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in accentglyphs:
    for accent in accents:
        sintaxless = accent.replace('','')
        if sintaxless in i:
            if sintaxless is 'bar':
                sintaxless = 'baraccent'  
            accentless = i.replace(sintaxless,'')
            if accentless in normglyphs:
                f.newGlyph(i)
                if 'i' in accentless and (accent is 'dotbelow' or accent is 'ogonek'):
                    f[i].appendComponent('i')
                elif 'i' in accentless:
                    print 'this happened'
                    f[i].appendComponent('dotlessi')
                elif 'j' in accentless:
                    f[i].appendComponent('dotlessj')
                else:
                    f[i].appendComponent(accentless)
                f[i].appendComponent(accent)
                f[i].width = f[accentless].width
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
                            f[i].appendComponent(accent)
                            f[i].appendComponent(accent2)
                            f[i].width = f[accentless2].width
                            print i + ' = ' + accentless + ' with ' + accent + ' and ' + accent2
                            f[i].mark = 1

                        else:
                            error = ('> There is a problem with ' + i + ' <').upper()
                            print error
                            print len(error) * '^'
                            
                            
    # Exceptions                        
    if i is 'khook':
        f.newGlyph(i)
        f[i].appendComponent('k')
        f[i].width = f['k'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50
    if i is 'oslash':
        f.newGlyph(i)
        f[i].appendComponent('o')
        f[i].width = f['o'].width
        f[i].mark = 50 
    if i is 'oslashacute':
        f.newGlyph(i)
        f[i].appendComponent('oslash')
        f[i].appendComponent('acute.cap')
        f[i].width = f['o'].width
        f[i].mark = 1 
    if i is 'lslash':
        f.newGlyph(i)
        f[i].appendComponent('l')
        f[i].width = f['l'].width
        f[i].mark = 50 
    if i is 'ocommaaccent':
        f.newGlyph(i)
        f[i].appendComponent('o')
        f[i].appendComponent('commaaccentturned.cap')
        f[i].width = f['o'].width
        f[i].mark = 1   
    if i is 'gcommaaccent':
        f.newGlyph(i)
        f[i].appendComponent('g')
        f[i].appendComponent('commaaccentturned.cap')
        f[i].width = f['g'].width
        f[i].mark = 1   
    if i is 'ldot':
        f.newGlyph(i)
        f[i].appendComponent('l')
        f[i].appendComponent('dotaccent')
        f[i].width = f['l'].width
        f[i].mark = 1  

                            
f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'