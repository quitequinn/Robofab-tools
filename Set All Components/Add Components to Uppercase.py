# Generate Uppercase Components - Quinn Keaveney

f = CurrentFont()

secondAccentHeight = 300

normglyphs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Thorn', 'Ezh', 'AE']

accentglyphs = ["Aacute", "Abreve", "Acaron", "Acircumflex", "Adieresis", "Adieresismacron", "Adotaccent", "Adoublegrave", "Agrave", "Ainvertedbreve", "Amacron", "Aogonek", "Aring", "Aringacute", "Atilde", "AE", "AEacute", "AEmacron", "Cacute", "Ccaron", "Ccedilla", "Ccircumflex", "Cdotaccent", "Dcaron", "Dcedilla", "Dcroat", "Ddotbelow", "Eacute", "Eacutedotbelow", "Ebreve", "Ecaron", "Ecircumflex", "Edieresis", "Edotaccent", "Edoublegrave", "Egrave", "Egravedotbelow", "Einvertedbreve", "Emacron", "Eogonek", "Gacute", "Gbreve", "Gcaron", "Gcircumflex", "Gcommaaccent", "Gdotaccent", "Gstroke", "Hbar", "Hcaron", "Hcircumflex", "Hdotbelow", "Hmacronbelow", "Iacute", "Ibreve", "Icaron", "Icircumflex", "Idieresis", "Idotaccent", "Idotbelow", "Idoublegrave", "Igrave", "Iinvertedbreve", "Imacron", "Iogonek", "Itilde", "Jcaron", "Jcircumflex", "Kcaron", "Kcedilla", "Kcommaaccent", "Khook", "Lacute", "Lcaron", "Lcedilla", "Lcommaaccent", "Ldot", "Ldotbelow", "Ldotbelowmacron", "Lslash", "Mcedilla", "Mdotbelow", "Mmacron", "Nacute", "Ncaron", "Ncedilla", "Ncommaaccent", "Ndescender", "Ndieresis", "Ndotaccent", "Ndotbelow", "Ngrave", "Nmacron", "Ntilde", "Oacute", "Obreve", "Ocaron", "Ocedilla", "Ocircumflex", "Ocommaturnedabove", "Odieresis", "Odotaccent", "Odotabovemacron", "Odotbelow", "Odoublegrave", "Ograve", "Ohungarumlaut", "Oinvertedbreve", "Omacron", "Oogonek", "Oogonekmacron", "Oslash", "Oslashacute", "Otilde", "Otildemacron", "Olinebelow", "Obar", "OE", "Pmacron", "Racute", "Rcaron", "Rcedilla", "Rcommaaccent", "Rdotbelow", "Rdotbelowmacron", "Rdoublegrave", "Rinvertedbreve", "Sacute", "Scaron", "Scedilla", "Scircumflex", "Scommaaccent", "Sdotbelow", "Germandbls", "Tbar", "Tcaron", "Tcedilla", "Tcommaaccent", "Tdotbelow", "Uacute", "Ubreve", "Ucaron", "Ucircumflex", "Udieresis", "Udotbelow", "Udoublegrave", "Ugrave", "Uhungarumlaut", "Uinvertedbreve", "Umacron", "Umacronbelow", "Uogonek", "Uring", "Utilde", "Wacute", "Wcircumflex", "Wdieresis", "Wgrave", "Yacute", "Ycircumflex", "Ydieresis", "Ygrave", "Ytilde", "Zacute", "Zcaron", "Zdotaccent", "Thorn", "Ezh", "Ezhcaron", "Schwa", "Ocommaaccent", "Odotaccentmacron"]

accents = ['acute.cap', 'grave.cap', 'hungarumlaut.cap', 'doublegrave.cap', 'circumflex.cap', 'caron.cap', 'dieresis.cap', 'tilde.cap', 'ring.cap', 'macron.cap', 'macronbelow.cap', 'breve.cap', 'invertedbreve.cap', 'dotaccent.cap', 'dotaccent.cap', 'dotbelow.cap', 'dotabove.cap', 'linebelow.cap', 'commaaccent.cap', 'cedilla.cap', 'altcedilla.cap', 'ogonek.cap', 'altogonek.cap', 'commaturnedabove.cap', 'croat.cap', 'stroke.cap', 'slashaccent.cap', 'descender.cap', 'bar.cap']


for i in CurrentFont().glyphOrder:
    # Remove marks
    CurrentFont()[i].mark = 0
for i in accentglyphs:
    for accent in accents:
        # strips .cap
        sintaxless = accent.replace('.cap','')
        if sintaxless in i:
            if sintaxless is 'bar':
                sintaxless = 'baraccent'            
            accentless = i.replace(sintaxless,'')
            if accentless in normglyphs:
                f.newGlyph(i)
                f[i].appendComponent(accentless)

                # centers first component to left shoulder
                w = f[i].width
                f[i].move((-(w/2), 0))
                
                f[i].appendComponent(accent)
                f[i].width = f[accentless].width

                # recenters components         
                f[i].move(((w/2), 0))

                print i + ' = ' + accentless + ' with ' + accent
                f[i].mark = 1

            else:
                for accent2 in accents:
                    sintaxless2 = accent2.replace('.cap','')
                    if sintaxless2 in accentless:
                        accentless2 = accentless.replace(sintaxless2,'')
                        if accentless2 in normglyphs:
                            f.newGlyph(i)
                            f[i].appendComponent(accentless2)
                            w = f[i].width
                            f[i].move((-(w/2), 0))
                            f[i].appendComponent(accent)
                            f[i].appendComponent(accent2)               
                            if (accent or accent2) is not ('dotbelow.cap' or 'macron.cap'):
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
    if i is 'Khook':
        f[i].width = f['K'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50
    if i is 'Oslash':
        f[i].width = f['O'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50 
    if i is 'Lslash':
        f[i].width = f['L'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50 
    if i is 'Obar':
        f[i].width = f['L'].width
        print i + ' = just' + i + ', you should add the rest'
        f[i].mark = 50 
                
    # Exceptions that will work out in the end          
    if i is 'Oslashacute':
        f.newGlyph(i)
        f[i].appendComponent('Oslash')
        w = f[i].width
        f[i].move((-(w/2), 0))
        f[i].appendComponent('acute.cap')
        f[i].width = f['O'].width
        f[i].move(((w/2), 0))            
        f[i].mark = 25
    if i is 'Ldot':
        f.newGlyph(i)
        f[i].appendComponent('L')
        w = f[i].width
        f[i].move((-(w/2), 0))
        f[i].appendComponent('dotaccent.cap')
        f[i].width = f['L'].width
        f[i].move(((w/2), 0))
        f[i].mark = 25 

                            
f.update()
print ''
print 'Changes marked in red.'
print 'Digested by Python.'