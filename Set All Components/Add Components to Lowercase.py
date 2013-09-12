# Generate Lowercase Components - Quinn Keaveney

f = CurrentFont()

normglyphs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Eng', 'Thorn', 'Eth', 'Ezh']

accentglyphs = ['aacute', 'agrave', 'acircumflex', 'adieresis', 'atilde', 'aring', 'acaron', 'amacron', 'abreve', 'ainvertedbreve', 'adoublegrave', 'adotabove', 'aringacute', 'adieresismacron', 'aogonek', 'ae', 'aeacute', 'aemacron', 'cacute', 'ccircumflex', 'ccaron', 'cdotaccent', 'ccedilla', 'dcaron', 'dcedilla', 'ddotbelow', 'dcroat', 'eacute', 'egrave', 'ecircumflex', 'edieresis', 'ecaron', 'emacron', 'ebreve', 'einvertedbreve', 'edoublegrave', 'edotaccent', 'eacutedotbelow', 'egravedotbelow', 'eogonek', 'gacute', 'gcircumflex', 'gcaron', 'gbreve', 'gdotaccent', 'gcommaaccent', 'gstroke', 'hcircumflex', 'hcaron', 'hdotbelow', 'hmacronbelow', 'hbar', 'dotlessi', 'iacute', 'igrave', 'icircumflex', 'idieresis', 'itilde', 'icaron', 'imacron', 'ibreve', 'iinvertedbreve', 'idoublegrave', 'idotaccent', 'idotbelow', 'iogonek', 'dotlessj', 'jcircumflex', 'jcaron', 'kcaron', 'kcommaaccent', 'kcedilla', 'khook', 'kgreenlandic', 'lacute', 'lcaron', 'lcommaaccent', 'lcedilla', 'ldotbelow', 'ldotbelowmacron', 'ldot', 'lslash', 'mmacron', 'mcedilla', 'mdotbelow', 'nacute', 'ngrave', 'ndieresis', 'ntilde', 'ncaron', 'nmacron', 'ndotaccent', 'ncommaaccent', 'ncedilla', 'ndotbelow', 'ndescender', 'oacute', 'ograve', 'ocircumflex', 'odieresis', 'otilde', 'ocaron', 'omacron', 'obreve', 'oinvertedbreve', 'ohungarumlaut', 'odoublegrave', 'ocommaturnedabove', 'otildemacron', 'odotabove', 'odotabovemacron', 'ocedilla', 'odotbelow', 'ounderlineaccent', 'oogonek', 'oogonekmacron', 'oslash', 'oslashacute', 'barredo', 'oe', 'pmacron', 'racute', 'rcaron', 'rinvertedbreve', 'rdoublegrave', 'rcommaaccent', 'rcedilla', 'rdotbelow', 'rdotbelowmacron', 'sacute', 'scircumflex', 'scaron', 'scommaaccent', 'scedilla', 'sdotbelow', 'germandbls', 'tcaron', 'tcommaaccent', 'tcedilla', 'tdotbelow', 'tbar', 'uacute', 'ugrave', 'ucircumflex', 'udieresis', 'utilde', 'uring', 'ucaron', 'umacron', 'ubreve', 'uinvertedbreve', 'uhungarumlaut', 'udoublegrave', 'uogonek', 'udotbelow', 'umacronbelow', 'wacute', 'wgrave', 'wcircumflex', 'wdieresis', 'yacute', 'ygrave', 'ycircumflex', 'ydieresis', 'ytilde', 'zacute', 'zcaron', 'zdotaccent', 'eng', 'thorn', 'eth', 'ezh', 'ezhcaron', 'schwa']

accents = ['acute', 'grave', 'hungarumlaut', 'doublegrave', 'circumflex', 'caron', 'dieresis', 'tilde', 'ring', 'macron', 'breve', 'invertedbreve', 'dotaccent', 'dotbelow', 'dotabove', 'linebelow', 'commaaccent', 'cedilla', 'altcedilla', 'ogonek', 'altogonek', 'commaabovecmb']

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in accentglyphs:
    for accent in accents:
        sintaxless = accent.replace('','')
        if sintaxless in i:
            accentless = i.replace(sintaxless,'')
            if accentless in normglyphs:
                f.newGlyph(i)
                if (accentless == 'i') and (accent == 'dotbelow' or accent == 'ogonek'):
                    f[i].appendComponent('i')
                if (accentless == 'i'):
                    f[i].appendComponent('dotlessi')
                if (accentless == 'j'):
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
                            
f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'