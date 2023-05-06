"""Testy pro vymazávací systém.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje testy pro ověření správnosti implementace vymazávacího systému.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: erasing_system_test.py
"""

import unittest

from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.formal_models.erasing_system.erasing_system import ErasingSystem


class ErasingSystemTest(unittest.TestCase):
    """Třída obsahující jednotkové testy pro vymazávací systém.

    Tato třída obsahuje jednotkové testy pro ověření správnosti implementace vymazávacího systému. Samotné testy uvažují
    správné přijetí či odmítnutí vstupního řetězce a zpracování chybových stavů. Jednotlivé typy kvantifikátorů
    (chmativý nebo líný) nejsou testovány. V případě nutnosti dle struktury regulárního jazyka a vstupního řetězce
    je explicitně povoleno testování všech pozic vymazávacích řetězců.
    """

    def test_start_with_string(self):
        """Testování případu, kdy všechny řetězce náležející regulárnímu jazyku musí začínat specifickým prefixem."""
        erasing_strings = {"ab", "cd"}
        regular_language = "(ab)(cd)*"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("ab"))
        self.assertTrue(erasing_system.run("abcd"))
        self.assertTrue(erasing_system.run("abcdcd"))
        self.assertTrue(erasing_system.run("cdabcd"))
        self.assertTrue(erasing_system.run("ccabdd"))

        self.assertFalse(erasing_system.run(""))
        self.assertFalse(erasing_system.run("cd"))
        self.assertFalse(erasing_system.run("a"))
        self.assertFalse(erasing_system.run("ah"))
        self.assertFalse(erasing_system.run("abf"))
        self.assertFalse(erasing_system.run("aecd"))
        self.assertTrue(erasing_system.run("cdabcd"))
        self.assertFalse(erasing_system.run("abcde"))

    def test_end_with_string(self):
        """Testování případu, kdy všechny řetězce náležející regulárnímu jazyku musí končit specifickým sufixem."""
        erasing_strings = {"a", "b", "c", "d"}
        regular_language = "(cd)+ab"

        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("abcd"))
        self.assertTrue(erasing_system.run("cabd"))
        self.assertTrue(erasing_system.run("cdab"))
        self.assertTrue(erasing_system.run("abcdcd"))
        self.assertTrue(erasing_system.run("cdabcd"))
        self.assertTrue(erasing_system.run("ccabdd"))

        self.assertFalse(erasing_system.run(""))
        self.assertFalse(erasing_system.run("ab"))
        self.assertFalse(erasing_system.run("cd"))
        self.assertFalse(erasing_system.run("adccb"))
        self.assertFalse(erasing_system.run("abcdab"))
        self.assertFalse(erasing_system.run("ecdab"))

        erasing_strings = {"ab", "cd"}
        regular_language = "(ab)*(cd)"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("abcdabab"))
        self.assertTrue(erasing_system.run("abcabdab"))
        self.assertTrue(erasing_system.run("cd"))

        self.assertFalse(erasing_system.run("abdcabab"))
        self.assertFalse(erasing_system.run("abcbadab"))
        self.assertFalse(erasing_system.run("dc"))

        erasing_strings = {"ab", "cd"}
        regular_language = "(ab)+(cd)"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("abcdabab"))
        self.assertTrue(erasing_system.run("abcabdab"))
        self.assertTrue(erasing_system.run("cabd"))

        self.assertFalse(erasing_system.run("abdcabab"))
        self.assertFalse(erasing_system.run("abcbadab"))
        self.assertFalse(erasing_system.run("cd"))
        self.assertFalse(erasing_system.run("dc"))

    def test_contains_string(self):
        """Testování případu, kdy všechny řetězce náležející regulárnímu jazyku musí obsahovat specifický
        podřetězec."""
        erasing_strings = {"ab", "c", "d"}
        regular_language = "(ab)*cd(ab)*"

        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("cd"))
        self.assertTrue(erasing_system.run("dc"))
        self.assertTrue(erasing_system.run("abdc"))
        self.assertTrue(erasing_system.run("abcdab"))
        self.assertTrue(erasing_system.run("aacdbb"))

        self.assertFalse(erasing_system.run("ab"))
        self.assertFalse(erasing_system.run("aabb"))
        self.assertFalse(erasing_system.run("aacdfbb"))
        self.assertFalse(erasing_system.run("abcdcd"))
        self.assertFalse(erasing_system.run("ccabdd"))

    def test_equal_number_of_symbols(self):
        """Testování případu, kdy všechny řetězce náležející regulárnímu jazyku obsahují totožný počet příslušných skupin
        symbolů."""
        erasing_strings = {"a", "b", "c"}
        regular_language = "(abc)*"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("cab"))
        self.assertTrue(erasing_system.run("cabbacacbabc"))
        self.assertFalse(erasing_system.run("cabbacacbac"))

        erasing_strings = {"a", "b", "c", "e", "f"}
        regular_language = "(abc)+(ef)"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("afbec"))
        self.assertFalse(erasing_system.run("ef"))
        self.assertFalse(erasing_system.run("cab"))

    def test_union(self):
        """Testování případu, kdy regulární jazyk obsahuje sjednocení (je obsažena operace sjednocení v regulárním
        výrazu pro definici regulárního jazyka)."""
        erasing_strings = {"ab", "cd", "ef"}
        regular_language = "(ab)*(cd|ef)+(ab)*"

        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("cd"))
        self.assertTrue(erasing_system.run("ef"))
        self.assertTrue(erasing_system.run("efcd"))
        self.assertTrue(erasing_system.run("abecdfab"))

        self.assertFalse(erasing_system.run(""))
        self.assertFalse(erasing_system.run("ab"))
        self.assertFalse(erasing_system.run("abfe"))
        self.assertFalse(erasing_system.run("abdcef"))

        erasing_strings = {"a", "b", "c", "d", "e", "f"}
        regular_language = "(aa|bb)[cd]*"

        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("cbdcdcbd"))
        self.assertTrue(erasing_system.run("aa"))

        self.assertFalse(erasing_system.run("cadcdcbd"))
        self.assertFalse(erasing_system.run("cd"))

        erasing_strings = {"a", "b", "c", "d", "e", "f"}
        regular_language = "(aa|bb|cc|dd|ee|ff)[abcdef]*"

        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("acbdcbfbdecbd"))
        self.assertTrue(erasing_system.run("ee"))

        self.assertFalse(erasing_system.run("acbdef"))
        self.assertFalse(erasing_system.run("ef"))

    def test_set_of_characters_range(self):
        """Testování případu, kdy regulární jazyk obsahuje sjednocení pro specifický rozsah symbolů."""
        erasing_strings = {"a", "b", "c", "e", "f"}
        regular_language = "(ab)+[a-f]+"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("aab"))
        self.assertTrue(erasing_system.run("abe"))
        self.assertTrue(erasing_system.run("afbec"))
        self.assertFalse(erasing_system.run("f"))
        self.assertFalse(erasing_system.run("ab"))

    def test_erasing_strings_longer_than_regular_language_groups(self):
        """Testování případu, kdy při porovnávání vymazávacích řetězců s regulárním jazykem každý vymazávací řetězec
        se bude párovat s více jak jedním podvýrazem regulárního výrazu pro definici regulárního jazyka."""
        erasing_strings = {"abcd", "ababcd"}
        regular_language = "(ab)*(cd)(ab)*(cd)"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("abcdababcd"))
        self.assertTrue(erasing_system.run("abababcdcd"))

        self.assertFalse(erasing_system.run("cdabababcd"))
        self.assertFalse(erasing_system.run("ababcd"))

        erasing_strings = {"ab", "abcd"}
        regular_language = "(ab)*(cd)"
        erasing_system = ErasingSystem(erasing_strings, regular_language, True)

        self.assertTrue(erasing_system.run("abcdabab"))
        self.assertTrue(erasing_system.run("abcababd"))

        self.assertFalse(erasing_system.run("cabd"))
        self.assertFalse(erasing_system.run("cd"))

        erasing_strings = {"ababcd", "abcdcd"}
        regular_language = "(ab)*(cd)*(ab)*(cd)*"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("ababcdabcdcd"))
        self.assertTrue(erasing_system.run("abcababcddcd"))

        self.assertFalse(erasing_system.run("cdababcdabcd"))
        self.assertFalse(erasing_system.run("ababcdababcdcdcd"))

        erasing_strings = {"abababcd", "ababcdcdcdcd"}
        regular_language = "(ab)*(cd)*(ab)*(cd)*"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run("abababcdababcdcdcdcd"))
        self.assertTrue(erasing_system.run("abababcdabababcd"))

        self.assertFalse(erasing_system.run("abcdabab"))
        self.assertFalse(erasing_system.run("abcdabcd"))

    def test_empty_erasing_strings_set(self):
        """Testování případu, kdy množina vymazávacích řetězců je prázdná množina."""
        erasing_strings = set()
        regular_language = "a*"

        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run(""))
        self.assertFalse(erasing_system.run("a"))

        erasing_strings = set()
        regular_language = "(abc)+(ef)"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertFalse(erasing_system.run("ef"))
        self.assertFalse(erasing_system.run(""))

        erasing_strings = set()
        regular_language = "(abc)*"
        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run(""))
        self.assertFalse(erasing_system.run("ef"))

    # The erasing system that also accepts an empty string.
    def test_accept_empty_string(self):
        """Testování případu, kdy vymazávací systém přijímá prázdný řetězec (epsilon)."""
        erasing_strings = {"a", "b"}
        regular_language = "(ab)*"

        erasing_system = ErasingSystem(erasing_strings, regular_language)

        self.assertTrue(erasing_system.run(""))
        self.assertTrue(erasing_system.run("ab"))
        self.assertTrue(erasing_system.run("abab"))

        self.assertFalse(erasing_system.run("a"))
        self.assertFalse(erasing_system.run("cd"))
        self.assertFalse(erasing_system.run("cab"))

    def test_valid_regular_language_pattern(self):
        """Testování validních tvarů regulárních výrazů pro regulární jazyky."""
        erasing_strings = set()

        # Forma následujícího kódu je založena na kódu, který je převzat:
        #
        # Zdrojový web: Stack Overflow.
        # Odkaz na původní otázku: https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises
        # Autor otázky: glaucon (https://stackoverflow.com/users/364088/glaucon).
        # Autor odpovědi: DGH (https://stackoverflow.com/users/309472/dgh).
        # Odpověď upravena: Stevoisiak (https://stackoverflow.com/users/3357935/stevoisiak).
        #
        # *** Začátek převzatého kódu. ***
        try:
            regular_language = "(ab)*[abc](cd)*"
            ErasingSystem(erasing_strings, regular_language)
        except InvalidRegularLanguagePatternException:
            self.fail("ErasingSystem() raised InvalidRegularLanguagePattern unexpectedly!")

        try:
            regular_language = "(ab)*[a-z0-9](cd)+"
            ErasingSystem(erasing_strings, regular_language)
        except InvalidRegularLanguagePatternException:
            self.fail("ErasingSystem() raised InvalidRegularLanguagePattern unexpectedly!")
        # *** Konec převzatého kódu. ***

    def test_invalid_regular_language_pattern(self):
        """Testování nevalidních tvarů regulárních výrazů pro regulární jazyky."""
        erasing_strings = set()

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = "(ab)*cd{1-5}"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = "(?<=abc)def"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = "(?=abc)"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = "(?#abc)"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = "(?!abc)"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = "*abc+"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = r".*"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = r"^abc$"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = ""
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = r"(ab)*(\( | \) | \[ | \] | \{ | \} | < | > | \\)"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = r"(ab)*(\$ | \# | \| | \:)"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = r"(a\Db)*"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = r"(ab)*+"
            ErasingSystem(erasing_strings, regular_language)

        with self.assertRaises(InvalidRegularLanguagePatternException):
            regular_language = r"(ab)++"
            ErasingSystem(erasing_strings, regular_language)


if __name__ == "__main__":
    unittest.main()
