#encoding: UTF-8

# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals
from .lang_EU import Num2Word_EU

class Num2Word_ptBR(Num2Word_EU):

    #//CHECK: Is this sufficient??
    def set_high_numwords(self, high):
        max = 3 + 6*len(high)

        for word, n in zip(high, range(max, 3, -6)):
            self.cards[10**(n-3)] = word + "illón"


    def setup(self):
        lows = ["quatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menos "
        self.pointword = "ponto"
        self.errmsg_nonnum = u"Apenas números podem ser convertidos em palavras."
        self.errmsg_toobig = "Número muito grande para ser convertido em palavras."
        self.gender_stem = "o"
        self.exclude_title = ["e", "menos", "ponto"]
        self.mid_numwords = [(1000, "mil"), (100, "cem"), (90, "noventa"),
                             (80, "oitenta"), (70, "setenta"), (60, "sessenta"),
                             (50, "cinquenta"), (40, "quarenta"), (30, "trinta")]
        self.low_numwords = ["vinte", "dezeonove", "dezoito", "dezessete",
                             "dezesseis", "quinze", "catorze", "treze", "doze",
                             "onze", "dez", "nove", "oito", "sete", "seis",
                             "cinco", "quatro", "tres", "dois", "um", "zero"]
        self.ords = { 1 : "primeir",
                      2 : "segund",
                      3 : "terceir",
                      4 : "quart",
                      5 : "quint",
                      6 : "sext",
                      7 : "sétim",
                      8 : "oitav",
                      9 : "non",
                     10 : "décim",
                     20 : "vigésim",
                     30 : "trigésim",
                     40 : "quadragésim",
                     50 : "quincuagésim",
                     60 : "sexagésim",
                     70 : "septuagésim",
                     80 : "octogésim",
                     90 : "nonagésim",
                    100 : "centésim",
                    200 : "ducentésim",
                    300 : "tricentésim",
                    400 : "cuadrigentésim",
                    500 : "quingentésim",
                    600 : "sexcentésim",
                    700 : "septigentésim",
                    800 : "octigentésim",
                    900 : "noningentésim",
                    1e3 : "milésim",
                    1e6 : "millonésim",
                    1e9 : "billonésim",
                   1e12 : "trillonésim",
                   1e15 : "cuadrillonésim" }


    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
            ctext = "un"
        elif cnum == 100 and not nnum == 1000:
            ctext += "t" + self.gender_stem

        if nnum < cnum:
            if cnum < 100:
                return ("%s y %s"%(ctext, ntext), cnum + nnum)
            return ("%s %s"%(ctext, ntext), cnum + nnum)
        elif (not nnum % 1000000) and cnum > 1:
            ntext = ntext[:-3] + u"ões"

        if nnum == 100:
            if cnum == 5:
                ctext = "quinhen"
                ntext = ""
            elif cnum == 7:
                ctext = "sete"
            elif cnum == 9:
                ctext = "nove"
            ntext += "t" + self.gender_stem + "s"
        else:
            ntext = " " + ntext

        return (ctext + ntext, cnum * nnum)


    def to_ordinal(self, value):
        self.verify_ordinal(value)
        text = ""
        try:
            if value == 0:
                text = ""
            elif value <= 10:
                text = "%s%s" % (self.ords[value], self.gender_stem)
            elif value <= 12:
                text = "%s%s%s" % (self.ords[10], self.gender_stem, self.to_ordinal(value - 10))
            elif value <= 100:
                dec = (value / 10) * 10
                text = "%s%s %s" % (self.ords[dec], self.gender_stem, self.to_ordinal(value - dec))
            elif value <= 1e3:
                cen = (value / 100) * 100
                text = "%s%s %s" % (self.ords[cen], self.gender_stem, self.to_ordinal(value - cen))
            elif value < 1e18:
                # dec contains the following:
                # [ 1e3,  1e6): 1e3
                # [ 1e6,  1e9): 1e6
                # [ 1e9, 1e12): 1e9
                # [1e12, 1e15): 1e12
                # [1e15, 1e18): 1e15
                dec = 10 ** ((((len(str(int(value))) - 1) / 3 - 1) + 1) * 3)
                part = int(float(value / dec) * dec)
                cardinal = self.to_cardinal(part / dec) if part / dec != 1 else ""
                text = "%s%s%s %s" % (cardinal, self.ords[dec], self.gender_stem, self.to_ordinal(value - part))
            else:
                text = self.to_cardinal(value)
        except KeyError:
            text = self.to_cardinal(value)
        return text.strip()

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, "º" if self.gender_stem == 'o' else "ª")


    def to_currency(self, val, longval=True, old=False):
        if old:
            return self.to_splitnum(val, hightxt="real/is", lowtxt="centavo/s",
                                    divisor=1000, jointxt="y", longval=longval)
        return super(Num2Word_ES, self).to_currency(val, jointxt="y",
                                                    longval=longval)


n2w = Num2Word_ptBR()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num

def main():
    for val in [ 1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
             180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
             8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
             -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)

    n2w.test(1325325436067876801768700107601001012212132143210473207540327057320957032975032975093275093275093270957329057320975093272950730)
    print n2w.to_currency(1222)
    print n2w.to_currency(1222, old=True)
    print n2w.to_year(1222)

if __name__ == "__main__":
    main()
