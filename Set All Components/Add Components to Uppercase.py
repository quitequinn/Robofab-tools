# Generate Uppercase Components - Quinn Keaveney

f = CurrentFont()

normglyphs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Eng', 'Thorn', 'Eth', 'Ezh']

accentglyphs = ["Aacute", "Abreve", "Acaron", "Acircumflex", "Adieresis", "Adieresismacron", "Adotabove", "Adoublegrave", "Agrave", "Ainvertedbreve", "Amacron", "Aogonek", "Aring", "Aringacute", "Atilde", "AE", "AEacute", "AEmacron", "Cacute", "Ccaron", "Ccedilla", "Ccircumflex", "Cdotaccent", "Dcaron", "Dcedilla", "Dcroat", "Ddotbelow", "Eacute", "Eacutedotbelow", "Ebreve", "Ecaron", "Ecircumflex", "Edieresis", "Edotaccent", "Edoublegrave", "Egrave", "Egravedotbelow", "Einvertedbreve", "Emacron", "Eogonek", "Gacute", "Gbreve", "Gcaron", "Gcircumflex", "Gcommaaccent", "Gdotaccent", "Gstroke", "Hbar", "Hcaron", "Hcircumflex", "Hdotbelow", "Hmacronbelow", "Iacute", "Ibreve", "Icaron", "Icircumflex", "Idieresis", "Idotaccent", "Idotbelow", "Idoublegrave", "Igrave", "Iinvertedbreve", "Imacron", "Iogonek", "Itilde", "Jcaron", "Jcircumflex", "Kcaron", "Kcedilla", "Kcommaaccent", "Khook", "Lacute", "Lcaron", "Lcedilla", "Lcommaaccent", "Ldot", "Ldotbelow", "Ldotbelowmacron", "Lslash", "Mcedilla", "Mdotbelow", "Mmacron", "Nacute", "Ncaron", "Ncedilla", "Ncommaaccent", "Ndescender", "Ndieresis", "Ndotaccent", "Ndotbelow", "Ngrave", "Nmacron", "Ntilde", "Oacute", "Obreve", "Ocaron", "Ocedilla", "Ocircumflex", "Ocommaturnedabove", "Odieresis", "Odotabove", "Odotabovemacron", "Odotbelow", "Odoublegrave", "Ograve", "Ohungarumlaut", "Oinvertedbreve", "Omacron", "Oogonek", "Oogonekmacron", "Oslash", "Oslashacute", "Otilde", "Otildemacron", "Ounderlineaccent", "barredO", "OE", "Pmacron", "Racute", "Rcaron", "Rcedilla", "Rcommaaccent", "Rdotbelow", "Rdotbelowmacron", "Rdoublegrave", "Rinvertedbreve", "Sacute", "Scaron", "Scedilla", "Scircumflex", "Scommaaccent", "Sdotbelow", "Germandbls", "Tbar", "Tcaron", "Tcedilla", "Tcommaaccent", "Tdotbelow", "Uacute", "Ubreve", "Ucaron", "Ucircumflex", "Udieresis", "Udotbelow", "Udoublegrave", "Ugrave", "Uhungarumlaut", "Uinvertedbreve", "Umacron", "Umacronbelow", "Uogonek", "Uring", "Utilde", "Wacute", "Wcircumflex", "Wdieresis", "Wgrave", "Yacute", "Ycircumflex", "Ydieresis", "Ygrave", "Ytilde", "Zacute", "Zcaron", "Zdotaccent", "Eng", "Thorn", "Eth", "Ezh", "Ezhcaron", "Schwa"]

accents = ['acute.cap', 'grave.cap', 'hungarumlaut.cap', 'doublegrave.cap', 'circumflex.cap', 'caron.cap', 'dieresis.cap', 'tilde.cap', 'ring.cap', 'macron.cap', 'breve.cap', 'invertedbreve.cap', 'dotaccent.cap', 'dotbelow.cap', 'dotabove.cap', 'linebelow.cap', 'commaaccent.cap', 'cedilla.cap', 'altcedilla.cap', 'ogonek.cap', 'altogonek.cap', 'commaabovecmb.cap']

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in accentglyphs:
    for accent in accents:
        sintaxless = accent.replace('.cap','')
        if sintaxless in i:
            accentless = i.replace(sintaxless,'')
            if accentless in normglyphs:
                f.newGlyph(i)
                f[i].appendComponent(accentless)
                f[i].appendComponent(accent)
                f[i].width = f[accentless].width
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