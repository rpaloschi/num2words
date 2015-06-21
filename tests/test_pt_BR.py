# -*- encoding: utf-8 -*-
# Copyright (c) 2015, Savoir-faire Linux inc.  All Rights Reserved.

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

from unittest import TestCase

from num2words import num2words

class Num2WordsPTBRTest(TestCase):

    def test_units(self):
        self.assertEqual('um', num2words(1, ordinal=False, lang='pt_BR'))
        self.assertEqual('nove', num2words(9, ordinal=False, lang='pt_BR'))

    def test_tens(self):
        self.assertEqual('onze', num2words(11, ordinal=False, lang='pt_BR'))
        self.assertEqual('doze', num2words(12, ordinal=False, lang='pt_BR'))
        self.assertEqual('treze', num2words(13, ordinal=False, lang='pt_BR'))
        self.assertEqual('quatorze',
                         num2words(14, ordinal=False, lang='pt_BR'))
        self.assertEqual('quinze', num2words(15, ordinal=False, lang='pt_BR'))
        self.assertEqual('dezesseis',
                         num2words(16, ordinal=False, lang='pt_BR'))
        self.assertEqual('dezessete',
                         num2words(17, ordinal=False, lang='pt_BR'))
        self.assertEqual('dezoito', num2words(18, ordinal=False, lang='pt_BR'))
        self.assertEqual('dezenove',
                         num2words(19, ordinal=False, lang='pt_BR'))

    def test_twenties(self):
        self.assertEqual('vinte', num2words(20, ordinal=False, lang='pt_BR'))
        self.assertEqual('vinte e nove',
                         num2words(29, ordinal=False, lang='pt_BR'))

    def test_thirties(self):
        self.assertEqual('trinta e cinco',
                         num2words(35, ordinal=False, lang='pt_BR'))
        self.assertEqual('trinta e oito',
                         num2words(38, ordinal=False, lang='pt_BR'))

    def test_hundreds(self):
        self.assertEqual('cem', num2words(100, ordinal=False, lang='pt_BR'))
        self.assertEqual('cento e um',
                         num2words(101, ordinal=False, lang='pt_BR'))
        self.assertEqual('cento e onze',
                         num2words(111, ordinal=False, lang='pt_BR'))
        self.assertEqual('cento e cinquenta e quatro',
                         num2words(154, ordinal=False, lang='pt_BR'))
        self.assertEqual('cento e noventa e nove',
                         num2words(199, ordinal=False, lang='pt_BR'))

        self.assertEqual('duzentos',
                         num2words(200, ordinal=False, lang='pt_BR'))
        self.assertEqual('trezentos',
                         num2words(300, ordinal=False, lang='pt_BR'))
        self.assertEqual('quatrocentos',
                         num2words(400, ordinal=False, lang='pt_BR'))
        self.assertEqual('quinhentos',
                         num2words(500, ordinal=False, lang='pt_BR'))
        self.assertEqual('seiscentos',
                         num2words(600, ordinal=False, lang='pt_BR'))
        self.assertEqual('setecentos',
                         num2words(700, ordinal=False, lang='pt_BR'))
        self.assertEqual('oitocentos',
                         num2words(800, ordinal=False, lang='pt_BR'))
        self.assertEqual('novecentos',
                         num2words(900, ordinal=False, lang='pt_BR'))

    def test_thousands(self):
        self.assertEqual('mil', num2words(1000, ordinal=False, lang='pt_BR'))
        self.assertEqual('mil e cinco',
                         num2words(1005, ordinal=False, lang='pt_BR'))
        self.assertEqual('mil e noventa e três',
                         num2words(1093, ordinal=False, lang='pt_BR'))
        self.assertEqual('mil e cem',
                         num2words(1100, ordinal=False, lang='pt_BR'))
        self.assertEqual('mil cento e dez',
                         num2words(1110, ordinal=False, lang='pt_BR'))
        self.assertEqual('mil e duzentos',
                         num2words(1200, ordinal=False, lang='pt_BR'))
        self.assertEqual('mil duzentos e doze',
                         num2words(1212, ordinal=False, lang='pt_BR'))
        self.assertEqual('mil e setecentos',
                         num2words(1700, ordinal=False, lang='pt_BR'))
        self.assertEqual('dois mil',
                         num2words(2000, ordinal=False, lang='pt_BR'))
        self.assertEqual('dois mil e dois',
                         num2words(2002, ordinal=False, lang='pt_BR'))
        self.assertEqual('dez mil e cem',
                         num2words(10100, ordinal=False, lang='pt_BR'))
        self.assertEqual('doze mil cento e vinte e sete',
                         num2words(12127, ordinal=False, lang='pt_BR'))
        self.assertEqual('noventa e oito mil trezentos e quatro',
                         num2words(98304, ordinal=False, lang='pt_BR'))
        self.assertEqual('noventa mil e quinhentos',
                         num2words(90500, ordinal=False, lang='pt_BR'))

    def test_hundred_thousands(self):
        self.assertEqual('cem mil',
                         num2words(100000, ordinal=False, lang='pt_BR'))
        self.assertEqual('oitocentos mil',
                         num2words(800000, ordinal=False, lang='pt_BR'))
        self.assertEqual('oitocentos mil e seis',
                         num2words(800006, ordinal=False, lang='pt_BR'))

    def test_millions(self):
        self.assertEqual('um milhão',
                         num2words(1000000, ordinal=False, lang='pt_BR'))
        self.assertEqual('dois milhões',
                         num2words(2000000, ordinal=False, lang='pt_BR'))
        self.assertEqual('nove milhões e um',
                         num2words(9000001, ordinal=False, lang='pt_BR'))
        self.assertEqual('oito milhões e vinte e três',
                         num2words(8000023, ordinal=False, lang='pt_BR'))
        self.assertEqual('oito milhões quatrocentos e vinte e três',
                         num2words(8000423, ordinal=False, lang='pt_BR'))
        self.assertEqual('oito milhões mil quatrocentos e vinte e três',
                         num2words(8001423, ordinal=False, lang='pt_BR'))
        self.assertEqual('oito milhões trinta e um mil quatrocentos e vinte e '
                         'três',
                         num2words(8031423, ordinal=False, lang='pt_BR'))
        self.assertEqual('oito milhões trezentos e trinta e um mil '
                         'quatrocentos e vinte e três',
                         num2words(8331423, ordinal=False, lang='pt_BR'))
        self.assertEqual('oito milhões e trezentos mil',
                         num2words(8300000, ordinal=False, lang='pt_BR'))

