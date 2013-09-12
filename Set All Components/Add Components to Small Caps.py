# Generate Small Cap Components - Quinn Keaveney
secondAccentHeight = 400

f = CurrentFont()

normglyphs = ['A.sc', 'B.sc', 'C.sc', 'D.sc', 'E.sc', 'F.sc', 'G.sc', 'H.sc', 'I.sc', 'J.sc', 'K.sc', 'L.sc', 'M.sc', 'N.sc', 'O.sc', 'P.sc', 'Q.sc', 'R.sc', 'S.sc', 'T.sc', 'U.sc', 'V.sc', 'W.sc', 'X.sc', 'Y.sc', 'Z.sc', 'a.sc', 'b.sc', 'c.sc', 'd.sc', 'e.sc', 'f.sc', 'g.sc', 'h.sc', 'i.sc', 'j.sc', 'k.sc', 'l.sc', 'm.sc', 'n.sc', 'o.sc', 'p.sc', 'q.sc', 'r.sc', 's.sc', 't.sc', 'u.sc', 'v.sc', 'w.sc', 'x.sc', 'y.sc', 'z.sc', 'Eng.sc', 'Thorn.sc', 'Eth.sc', 'Ezh.sc']

accentglyphs = ['Aacute.sc', 'Agrave.sc', 'Adoublegrave.sc', 'Abreve.sc', 'Ainvertedbreve.sc', 'Acaron.sc', 'Acircumflex.sc', 'Adieresis.sc', 'Adieresismacron.sc', 'Adotabove.sc', 'Amacron.sc', 'Atilde.sc', 'Aogonek.sc', 'Aring.sc', 'Aringacute.sc', 'AE.sc', 'AEacute.sc', 'AEmacron.sc', 'Cacute.sc', 'Ccaron.sc', 'Ccircumflex.sc', 'Cdotaccent.sc', 'Ccedilla.sc', 'Dcaron.sc', 'Dcroat.sc', 'Dcedilla.sc', 'Ddotbelow.sc', 'Eacute.sc', 'Eacutedotbelow.sc', 'Egrave.sc', 'Egravedotbelow.sc', 'Edoublegrave.sc', 'Ebreve.sc', 'Einvertedbreve.sc', 'Ecaron.sc', 'Ecircumflex.sc', 'Edieresis.sc', 'Edotaccent.sc', 'Emacron.sc', 'Eogonek.sc', 'Gacute.sc', 'Gbreve.sc', 'Gcaron.sc', 'Gcircumflex.sc', 'Gcommaaccent.sc', 'Gdotaccent.sc', 'Gstroke.sc', 'Hbar.sc', 'Hcaron.sc', 'Hcircumflex.sc', 'Hdotbelow.sc', 'Hmacronbelow.sc', 'Iacute.sc', 'Igrave.sc', 'Idoublegrave.sc', 'Ibreve.sc', 'Icaron.sc', 'Icircumflex.sc', 'Idieresis.sc', 'Idotaccent.sc', 'Idotbelow.sc', 'Iinvertedbreve.sc', 'Imacron.sc', 'Itilde.sc', 'Iogonek.sc', 'Jcaron.sc', 'Jcircumflex.sc', 'Kcaron.sc', 'Kcedilla.sc', 'Kcommaaccent.sc', 'Khook.sc', 'Lacute.sc', 'Lcaron.sc', 'Lcedilla.sc', 'Lcommaaccent.sc', 'Ldot.sc', 'Ldotbelow.sc', 'Ldotbelowmacron.sc', 'Lslash.sc', 'Mdotbelow.sc', 'Mmacron.sc', 'Mcedilla.sc', 'Nacute.sc', 'Ngrave.sc', 'Ncaron.sc', 'Ncommaaccent.sc', 'Ndescender.sc', 'Ndieresis.sc', 'Ndotaccent.sc', 'Ndotbelow.sc', 'Nmacron.sc', 'Ntilde.sc', 'Ncedilla.sc', 'Oacute.sc', 'Ograve.sc', 'Ohungarumlaut.sc', 'Odoublegrave.sc', 'Obreve.sc', 'Oinvertedbreve.sc', 'Ocaron.sc', 'Ocedilla.sc', 'Ocircumflex.sc', 'Ocommaturnedabove.sc', 'Odieresis.sc', 'Odotabove.sc', 'Odotabovemacron.sc', 'Odotbelow.sc', 'Omacron.sc', 'Otilde.sc', 'Otildemacron.sc', 'Ounderlineaccent.sc', 'Oogonek.sc', 'Oogonekmacron.sc', 'Oslash.sc', 'Oslashacute.sc', 'barredO.sc', 'OE.sc', 'Pmacron.sc', 'Racute.sc', 'Rdoublegrave.sc', 'Rcaron.sc', 'Rcedilla.sc', 'Rcommaaccent.sc', 'Rdotbelow.sc', 'Rdotbelowmacron.sc', 'Rinvertedbreve.sc', 'Sacute.sc', 'Scaron.sc', 'Scedilla.sc', 'Scircumflex.sc', 'Scommaaccent.sc', 'Sdotbelow.sc', 'germandbls.sc', 'Tbar.sc', 'Tcaron.sc', 'Tcommaaccent.sc', 'Tcedilla.sc', 'Tdotbelow.sc', 'Uacute.sc', 'Ugrave.sc', 'Uhungarumlaut.sc', 'Udoublegrave.sc', 'Ubreve.sc', 'Uinvertedbreve.sc', 'Ucaron.sc', 'Ucircumflex.sc', 'Udieresis.sc', 'Udotbelow.sc', 'Umacron.sc', 'Umacronbelow.sc', 'Uogonek.sc', 'Uring.sc', 'Utilde.sc', 'Wacute.sc', 'Wcircumflex.sc', 'Wdieresis.sc', 'Wgrave.sc', 'Yacute.sc', 'Ycircumflex.sc', 'Ydieresis.sc', 'Ygrave.sc', 'Ytilde.sc', 'Zacute.sc', 'Zcaron.sc', 'Zdotaccent.sc', 'Eth.sc', 'Thorn.sc', 'Eng.sc', 'Ezh.sc', 'Ezhcaron.sc']

accents = ['acute.sc', 'grave.sc', 'hungarumlaut.sc', 'doublegrave.sc', 'circumflex.sc', 'caron.sc', 'dieresis.sc', 'tilde.sc', 'ring.sc', 'macron.sc', 'breve.sc', 'invertedbreve.sc', 'dotaccent.sc', 'dotbelow.sc', 'dotabove.sc', 'linebelow.sc',  'cedilla.sc', 'altcedilla.sc', 'ogonek.sc', 'altogonek.sc', 'commaabovecmb.sc', 'commaaccent.sc']

for i in CurrentFont().glyphOrder:
    CurrentFont()[i].mark = 0
for i in accentglyphs:
    for accent in accents:
        sintaxless = accent.replace('.sc','')
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
                    sintaxless2 = accent2.replace('.sc','')
                    if sintaxless2 in accentless:
                        accentless2 = accentless.replace(sintaxless2,'')
                        if accentless2 in normglyphs:
                            f.newGlyph(i)
                            f[i].appendComponent(accent2)
                            f[i].move((0, secondAccentHeight))
                            f[i].appendComponent(accentless2)
                            f[i].appendComponent(accent)
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