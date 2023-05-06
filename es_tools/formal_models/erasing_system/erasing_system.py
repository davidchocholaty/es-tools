"""Implementace vymazávacího systému.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci formálního systému nazývaného vymazávací systém, přičemž obsahuje implementaci jeho
hlavního algoritmu, který je v textu zachycen v příloze E. Celkově je vymazávací systém implementován pomocí metod
třídy ErasingSystem a pomocných funkcí.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: erasing_system.py
"""


import re

from random import choice
from typing import List, Set, Tuple

from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception \
    import MaximumInputStringLengthExceededException
from es_tools.formal_models.erasing_system.custom_utils.custom_constants import DEFAULT_MATCH_LEVEL, \
    ERASING_STRING_TUPLE_INDEX, MATCH_LEVEL_TUPLE_INDEX
from es_tools.formal_models.erasing_system.custom_utils.filter_tools import filter_applicable_erasing_strings, \
    filter_quantifier_levels
from es_tools.formal_models.erasing_system.custom_utils.match_language_tools \
    import calculate_levels, match_transformed_language
from es_tools.formal_models.erasing_system.custom_utils.maximum_recursion_depth import MAXIMUM_RECURSION_DEPTH
from es_tools.formal_models.erasing_system.custom_utils.not_allowed_erasing_string_symbols \
    import not_allowed_erasing_string_symbols
from es_tools.formal_models.erasing_system.custom_utils.regular_language_checking_tools import is_valid_regular_language
from es_tools.formal_models.formal_model import FormalModel


class ErasingSystem(FormalModel):
    """Implementace vymazávacího systému.

    Tato třída poskytuje metody, které implementují hlavní funkcionalitu vymazávacího systému. Kromě konstruktoru, metod
    pro získání či nastavení hodnot, hlavní algoritmus činnosti vymazávacího systému, který je v textu zachycen
    v příloze E, představuje metoda _is_accepted().

    Třida je zděděna od abstraktní třídy FormalModel, která slouží jako bázová třída pro všechny formální modely
    implementované v celém projektu.
    """
    def __init__(self, erasing_strings: Set[str],
                 regular_language: str,
                 test_all_overlapping_positions: bool = False,
                 quantifier_type_greedy: bool = True,
                 verbose: bool = False) -> None:
        """**Konstruktor třídy ErasingSystem**

        Konstruktor slouží především pro nastavení základních entit konečného převodníku, jako je například množina
        vymazávacích řetězců či regulární jazyk. Zároveň konstruktor zajišťuje nastavení parametrů pro samotnou činnost
        vymazávacího systému, a to typ použitého kvantifikátoru, určení, zda mají být ověřovány všechny pozice
        vymazávacích řetězců nebo jestli se mají vypisovat dodatečné podrobnější informace o zpracování vstupního
        řetězce na standarní výstup.

        :param erasing_strings: množina vymazávacích řetězců.
        :type erasing_strings: Set[str]
        :param regular_language: řetězec obsahující regulární výraz reprezentující regulární jazyk.
        :type regular_language: str
        :param test_all_overlapping_positions: pravdivostní hodnota, zda mají být ověřovány všechny pozice vymazávacích
                                               řetězců, přičemž přirozeně platí vztahy: True — Ano, False — Ne.
        :type test_all_overlapping_positions: bool
        :param quantifier_type_greedy: typ kvantifikátoru. Pokud je hodnota True, je použit chamtivý kvantifikátor
                                       (greedy quantifier). V opačném případě se použije takzvaný líný kvantifikátor
                                       (lazy quantifier).
        :type quantifier_type_greedy: bool
        :param verbose: definování, zdá mají být při provádění algoritmu vypisovány na standardní výstup dodatečné
                        podrobné informace (aktuální stav vstupní pásky, použitý vymazávací řetězec, řetězec vzniklý
                        konkatenací dříve využitých vymazávacích řetězců). Pokud obsahuje hodnotu True, informace
                        jsou vypisovány.
        :type verbose: bool
        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního výrazu
                                                        pro regulární jazyk.
        """
        self.__alphabet = set()
        self.__erasing_strings = set()
        self.__regular_language = list()
        self.__test_all_overlapping_positions = test_all_overlapping_positions
        self.__quantifier_type_greedy = quantifier_type_greedy
        self.__verbose = verbose

        try:
            self._set_erasing_strings(erasing_strings)
        except IllegalSymbolOccurrenceException:
            raise

        try:
            self._set_regular_language(regular_language)
        except InvalidRegularLanguagePatternException:
            raise

    @property
    def alphabet(self) -> Set[str]:
        """Abeceda vymazávacího systému.

        :getter: získání abecedy definovaného vymazávacího systému.
        :type: Set[str]
        """
        return self.__alphabet

    @property
    def erasing_strings(self) -> Set[str]:
        """Vymazávací řetězce vymazávacího systému.

        :getter: získání množiny vymazávacích řetězců vymazávacího systému.
        :type: Set[str]
        """
        return self.__erasing_strings

    @property
    def regular_language(self) -> List[str]:
        """Regulární jazyk vymazávacího systému.

        :getter: získání regulárního výrazu pro regulární jazyk vymazávacího systému.
        :type: List[str]
        """
        return self.__regular_language

    @property
    def test_all_overlapping_positions(self) -> bool:
        """Testování všech překrývajících se pozic vymazávacích řetězců.

        Nastavení, zda mají být při vykonávání algoritmu ověřovány všechny pozice vymazávacích řetězců ve vstupním
        řetězci.

        :getter: získání pravdivostní hodnoty pro nastavení ověřování všech pozic vymazávacích řetězců.
        :setter: nastavení ověřování všech pozic vymazávacích řetězců (zda se mají ověřovat či nikoliv).
        :type: bool
        """
        return self.__test_all_overlapping_positions

    @test_all_overlapping_positions.setter
    def test_all_overlapping_positions(self, test_all_overlapping_positions: bool) -> None:
        self.__test_all_overlapping_positions = test_all_overlapping_positions

    @property
    def quantifier_type_greedy(self) -> bool:
        """Nastavení typu kvantifikátoru.

        Nastavení typu kvantifikátoru, přičemž se uvažuje pravdivostní hodnota, která určuje, zdá má být použit
        chamtivý kvantifikátor. V opačném případě algoritmus využívá takzvaný líný kvantifikátor.

        :getter: získání typu kvantifikátoru (True — chamtivý, False — líný).
        :setter: nastavení typu kvantifikátoru (True — chamtivý, False — líný).
        :type: bool
        """
        return self.__quantifier_type_greedy

    @quantifier_type_greedy.setter
    def quantifier_type_greedy(self, quantifier_type_greedy: bool) -> None:
        self.__quantifier_type_greedy = quantifier_type_greedy

    def _set_erasing_strings(self, erasing_strings: Set[str]) -> None:
        """Nastavení množiny vymazávacích řetězců vymazávacího systému.

        Tato metoda zajišťuje nastavení množiny vymazávacích řetězců, přičemž jako privátní metodu ji využívá pouze
        konstruktor třídy ErasingSystem.

        :param erasing_strings: množina vymazávacích řetězců, která má být nastavena.
        :type erasing_strings: Set[str]
        :raises IllegalSymbolOccurrenceException: minimálně jeden z vymazávacích řetězců množiny obsahuje nepovolený
                                                  symbol.
        """
        for erasing_string in erasing_strings:
            if any(symbol in erasing_string for symbol in not_allowed_erasing_string_symbols):
                raise IllegalSymbolOccurrenceException

            self.__alphabet.update(set(erasing_string))

        self.__erasing_strings = erasing_strings

    def _set_regular_language(self, regular_language: str) -> None:
        """Nastavení regulárního výrazu pro regulární jazyk vymazávacího systému.

        Tato metoda zajišťuje nastavení regulárního výrazu pro regulární jazyk vymazávacího systému, přičemž jako
        privátní metodu ji využívá pouze konstruktor třídy ErasingSystem. Nutno zdůraznit, že samotný regulární jazyk
        je rozdělen na seznam obsahující jednotlivé podvýrazy regulárního výrazu pro regulární jazyk za účelem
        pozdějšího porovnávání vstupních řetězců s jednotlivými prefixy regulárního výrazu. Například regulární výraz
        "(ab)*(c|de)+fg*[hij]*" je rozdělen na seznam ["(ab)", "*", "(c|de)", "+", "f", "g", "*", "[hij]", "*"].

        :param regular_language: regulární výraz pro regulární jazyk právě definovaného vymazávacího systému.
        :type regular_language: str
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního výrazu pro regulární
                                                        jazyk.
        """
        if not is_valid_regular_language(regular_language):
            raise InvalidRegularLanguagePatternException

        self.__regular_language = re.findall(r"(\(.+?\)|\[.+?]|.+?)", regular_language)

    def _match_using_greedy_approach(self, input_string: str) -> Tuple[bool, int, List[int]]:
        """Oveření, zda řetězec může náležet do regulárního jazyka s využitím chamtivého kvantifikátoru.

        Tato metoda slouží pro ověření, zda řetězec vzniklý konkatenací použitých vymazávacích řetězců by po libovolném
        počtu jednoho a více vymazávacích kroků mohl náležet do reguláního jazyka s využitím přístupu chamtivého
        kvantifikátoru.

        :param input_string: vstupní řetězec vzniklý konkatenací použitých vymazávacích řetězců.
        :type input_string: str
        :return: trojice hodnot, které po řadě reprezentují:
                 1. zda řetězec může náležet do regulárního jazyka,
                 2. úroveň shody řetězce s regulárním výrazem
                 3. seznam obsahující počty opakování jednotlivých podvýrazů regulárního výrazu ve vstupním řetězci.
        :rtype: Tuple[bool, int, List[int]]
        """
        # Nastavení výchozích hodnot pro zaznamenávané parametry porovnání.
        match = False
        match_level = DEFAULT_MATCH_LEVEL
        quantifiers_levels = list()

        # Nastavení počátečního tvaru porovnávaného regulárního výrazu (regulárního jazyku), přičemž porovnávaný jazyk
        # (compared_language) je nastaven jako první prvek seznamu podvýrazů regulárního výrazu.
        regular_language_list = self.__regular_language.copy()
        compared_language = [regular_language_list[0]]
        regular_language_list.pop(0)

        while match_level == DEFAULT_MATCH_LEVEL:
            # Kontrola, zda vstupní řetězec náleží do regulárního jazyka bez potřebných úprav porovnávaného regulárního
            # výrazu.
            match_result = re.fullmatch("".join(compared_language), input_string)

            if match_result:
                # Pokud ano, jsou nastaveny parametry pro provedené porovnání.
                match = True
                match_level, quantifiers_levels = calculate_levels(match_result.groups(),
                                                                   compared_language,
                                                                   input_string)
            else:
                # V opačném případě je zapotřebí provést určité úpravy porovnávaného regulárního jazyka pro ověření
                # všech možností porovnání. Pokud ani po modifikaci zmíněného výrazu nenáleží vstupní řetězec
                # do podčásti regulárního jazyka, poté, pokud je to možné, je přidána k porovnávanému regulárnímu
                # výrazu další podčást regulárního jazyka.
                match, match_level, quantifiers_levels = match_transformed_language(compared_language, input_string)

                if not match:
                    if len(regular_language_list) > 0:
                        compared_language.append(regular_language_list[0])
                        regular_language_list.pop(0)
                    else:
                        match_level = 0

        return match, match_level, quantifiers_levels

    def _match_using_lazy_approach(self, input_string: str) -> Tuple[bool, int, List[int]]:
        """Oveření, zda řetězec může náležet do regulárního jazyka s využitím líného kvantifikátoru.

        Tato metoda slouží pro ověření, zda řetězec vzniklý konkatenací použitých vymazávacích řetězců by po libovolném
        počtu jednoho a více vymazávacích kroků mohl náležet do reguláního jazyka s využitím přístupu líného
        kvantifikátoru.

        :param input_string: vstupní řetězec vzniklý konkatenací použitých vymazávacích řetězců.
        :type input_string: str
        :return: trojice hodnot, které po řadě reprezentují:
                 1. zda řetězec může náležet do regulárního jazyka,
                 2. úroveň shody řetězce s regulárním výrazem
                 3. seznam obsahující počty opakování jednotlivých podvýrazů regulárního výrazu ve vstupním řetězci.
        :rtype: Tuple[bool, int, List[int]]
        """
        # Nastavení výchozích hodnot pro zaznamenávané parametry porovnání.
        saved_tuple = (False, DEFAULT_MATCH_LEVEL, list())

        # Nastavení počátečního tvaru porovnávaného regulárního výrazu (regulárního jazyku), přičemž se začíná
        # od původního tvaru regulárního výrazu a postupně jsou od jeho konce odebírány jednotlivé podčásti
        # regulárního jazyka.
        regular_language_list = self.__regular_language.copy()

        while len(regular_language_list) > 0:
            # Kontrola, zda vstupní řetězec náleží do regulárního jazyka bez potřebných úprav porovnávaného regulárního
            # výrazu.
            match_result = re.fullmatch("".join(regular_language_list), input_string)

            if match_result:
                # Pokud ano, jsou nastaveny parametry pro provedené porovnání.
                match = True
                match_level, quantifiers_levels = calculate_levels(match_result.groups(),
                                                                   regular_language_list,
                                                                   input_string)
            else:
                # V opačném případě je zapotřebí provést určité úpravy porovnávaného regulárního jazyka pro ověření
                # všech možností porovnání. Pokud ani po modifikaci zmíněného výrazu nenáleží vstupní řetězec
                # do podčásti regulárního jazyka.
                match, match_level, quantifiers_levels = match_transformed_language(regular_language_list,
                                                                                    input_string)

            # Pokud řetězec může náležet do regulárního jazyka, jsou uloženy aktuální parametry porovnání.
            # Pokud v následujícím bude opět moci náležet řetězec do regulárního jazyka s využitím menšího počtu
            # podvýrazů regulárního výrazu, bude aktulně uložená hodnota nahrazena novou hodnotou.
            if match:
                saved_tuple = (match, match_level, quantifiers_levels)

            # Od porovnávaného regulárního jazyka je odebrána jeho další podčást. Pokud posledním elementem je operátor
            # „*“ nebo „+“, může být odstraněn i předcházející podvýraz regulárního výrazu pro regulární jazyk.
            # Zároveň dle prováděných kontrol regulárního výrazu při inicializaci vymazávacího systému nemůže regulární
            # výraz začínat jedním z uvedených operátoru. Z toho vyplývá, že délka seznamu, který končí uvedeným
            # operátorem, je větší nebo rovna dvěma prvkům. Tudíž pro minimalizaci kontrol při iteraci není prováděna
            # kontrola délky seznamu.
            if regular_language_list[-1] in ["*", "+"]:
                regular_language_list = regular_language_list[:len(regular_language_list) - 2]
            else:
                regular_language_list.pop()

        return saved_tuple

    def _match_regular_language(self, input_string: str,
                                full_match: bool = False) -> Tuple[bool, int, List[int]]:
        """Ověření, zda řetězec může náležet do regulárního jazyka.

        Tato metoda slouží pro ověření, zda řetězec vzniklý konkatenací použitých vymazávacích řetězců by po libovolném
        počtu vymazávacích kroků mohl náležet do reguláního jazyka. Samotná tato metoda provádí ověření pouze tehdy,
        jestli vstupní řetězec má náležet do regulárního jazyka právě v aktuálním kroku (tedy po počtu nula kroků)
        — full_match. V opačném případě, pokud se neprovádí celkové porovnání, metoda na základě nastavení volá metody
        zpracování pro příslušné typy kvantifikátorů (chamtivý nebo líný).

        :param input_string: vstupní řetězec vzniklý konkatenací použitých vymazávacích řetězců.
        :type input_string: str
        :param full_match: nastavení, zdá řetězec má náležet do regulárního jazyka v aktuálním kroku.
        :type full_match: bool
        :return: trojice hodnot, které po řadě reprezentují:
                 1. zda řetězec může náležet do regulárního jazyka,
                 2. úroveň shody řetězce s regulárním výrazem
                 3. seznam obsahující počty opakování jednotlivých podvýrazů regulárního výrazu ve vstupním řetězci.
        :rtype: Tuple[bool, int, List[int]]
        """
        if full_match and re.fullmatch("".join(self.__regular_language), input_string) is None:
            return False, 0, list()

        if self.__quantifier_type_greedy:
            match, match_level, quantifiers_levels = self._match_using_greedy_approach(input_string)
        else:
            match, match_level, quantifiers_levels = self._match_using_lazy_approach(input_string)

        return match, match_level, quantifiers_levels

    def _is_accepted(self, input_tape: str, erased_strings_concatenation: str) -> bool:
        """Hlavní algoritmus činnosti vymazávacího systému.

        Tato metoda implementuje hlavní algoritmus vymazávacího systému, který je v textu představen v sekci 7.1 a
        zapsán pomocí výpisu a pseudokódu v příloze E.

        :param input_tape: vstupní páska v aktuálním stavu přijímání.
        :type input_tape: str
        :param erased_strings_concatenation: řetězec vzniklý konkatenací použitých vymazávacích řetězců v aktuálním
                                             stavu přijímání.
        :type erased_strings_concatenation: str
        :return: pravdivostní hodnota, zda vstupní řetězec je přijat vymazávacím systémem (True) či nikoliv (False)
                 pro daný tvar vstupní pásky a řetězce vzniklého konkatenací použitých vymazávacích řetězců.
                 Tato navrácená hodnota je využívána při rekurzivních volání metody.
        :rtype: bool
        """
        # Pokud je v aktuálním stavu přijímání vstupního řetězce vstupní páska prázdná, je ověřeno, zda řetězec vzniklý
        # konkatenací vymazávacích řetězců náleží do regulárního jazyka.
        if input_tape == "":
            match, match_level, quantifiers_levels = self._match_regular_language(erased_strings_concatenation, True)

            return match

        # Uchování aplikovatelných vymazávacích řetězců v aktuálním stavu přijímání vstupního řetězce.
        applicable_erasing_strings = list()

        # 1. Nalezení všech vymazávacích řetězců, které jsou podřetězci řetězce definovaného na vstupní pásce.
        # 2. Zároveň všechny vymazávací řetězce musí být aplikovatelné na základě řídícího regulárního jazyka.
        for erasing_string in self.__erasing_strings:
            if erasing_string in input_tape:
                match, match_level, quantifiers_levels = self._match_regular_language(
                    erased_strings_concatenation + erasing_string)

                if match:
                    applicable_erasing_strings.append((erasing_string, match_level, quantifiers_levels))

        while len(applicable_erasing_strings) != 0:
            if self.__quantifier_type_greedy:
                # Výběr příslušných hodnot pro chamtivý kvantifikátor.
                chosen_match_level = min([erasing_string_tuple[MATCH_LEVEL_TUPLE_INDEX]
                                          for erasing_string_tuple in applicable_erasing_strings])
                chosen_quantifiers_levels = filter_quantifier_levels(applicable_erasing_strings,
                                                                     chosen_match_level,
                                                                     True)
            else:
                # Výběr příslušných hodnot pro líný kvantifikátor.
                chosen_match_level = max([erasing_string_tuple[MATCH_LEVEL_TUPLE_INDEX]
                                          for erasing_string_tuple in applicable_erasing_strings])

                chosen_quantifiers_levels = filter_quantifier_levels(applicable_erasing_strings,
                                                                     chosen_match_level,
                                                                     False)

            # 3. Nedeterministický výběr jednoho vymazávacího řetězce.
            quantifier_based_applicable_strings = filter_applicable_erasing_strings(applicable_erasing_strings,
                                                                                    chosen_quantifiers_levels,
                                                                                    chosen_match_level)
            erasing_string_to_application_tuple = choice(quantifier_based_applicable_strings)

            erasing_string_to_application = erasing_string_to_application_tuple[ERASING_STRING_TUPLE_INDEX]

            # 4. Nalezení všech i překrývajících se výskytů zvoleného vymazávacího řetězce na vstupní pásce.

            # Následující řádek kódu je převzat:
            #
            # Zdrojový web: Stack Overflow.
            # Odkaz na původní otázku: https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
            # Autor otázky: nukl (https://stackoverflow.com/users/277262/nukl).
            # Otázka upravena: Karl Knechtel (https://stackoverflow.com/users/523612/karl-knechtel).
            # Autor odpovědi: moinudin (https://stackoverflow.com/users/89806/moinudin).
            # Odpověď upravena: David Leon (https://stackoverflow.com/users/3941704/david-leon).
            #
            # *** Začátek převzatého kódu. ***
            all_overlapping_positions = [m.start() for m in re.finditer("(?=" + erasing_string_to_application + ")",
                                                                        input_tape)]
            # *** Konec převzatého kódu. ***

            while len(all_overlapping_positions) != 0:
                # 5. Nedeterministický výběr jedné pozice výskytu zvoleného vymazávacího řetězce.
                selected_position = choice(all_overlapping_positions)

                if self.__verbose:
                    if erased_strings_concatenation == "":
                        print_erased_strings_concatenation = "\"epsilon\""
                    else:
                        print_erased_strings_concatenation = erased_strings_concatenation

                    if self.__verbose:
                        print("----------------------")
                        print("Chosen erasing string: " +
                              erasing_string_to_application_tuple[ERASING_STRING_TUPLE_INDEX])
                        print("Input tape: " + input_tape[:selected_position] + "#" + input_tape[selected_position:])
                        print("Erased strings concatenation: " + print_erased_strings_concatenation)
                        print("----------------------\n")

                # 6. Vymazání zvoleného vymazávacího řetězce z určené pozice na vstupní pásce.
                input_tape_after_erasing = input_tape[:selected_position] + \
                                           input_tape[selected_position + len(erasing_string_to_application):]  # noqa: E127

                # Rekurzivní volání metody s novými hodnotami pro aktuální tvar vstupní pásky a řetězce vzniklého
                # konkatenací použitých vymazávacích řetězců.
                if self._is_accepted(input_tape_after_erasing,
                                     erased_strings_concatenation + erasing_string_to_application):
                    return True
                elif self.__test_all_overlapping_positions:
                    # Algoritmus pracuje v režimu testování všech pozic vymazávacích řetězců. Pokud tedy pro daný
                    # vymazávací řetězec odstraněný z určené pozice na vstupní pásce není možné přimout vstupní
                    # řetězec, bude z množiny všech aplikovatelných pozic odstraněna zvolená pozice. Dále pro totožný
                    # vymazávací řetězec se následně v další iteraci nedeterministicky zvolí jiná pozice.
                    all_overlapping_positions.remove(selected_position)
                else:
                    # Pokud algoritmus nepracuje v režimu testování všech pozic, je množina všech aplikovatelných pozic
                    # nastavena jako prázdná množina a v další iteraci bude ověrován jiný vymazávací řetězec.
                    all_overlapping_positions.clear()

            # V daném kroku přijímání vstupního řetězce zvolení ověřovaného vymazávací řetězec nevedlo k přijetí
            # vstupního řetězce. Daný řetězec tedy bude odstraněn z množiny všech aplikovatelných vymazávacích řetězců.
            # Následně se v další iteraci zvolí pro aktuální tvar vstupní pásky jiný vymazávací řetězec.
            applicable_erasing_strings.remove(erasing_string_to_application_tuple)

        return False

    def run(self, input_string: str) -> bool:
        """Spuštění hlavního algoritmu činnosti vymazávacího systému.

        Tato metoda slouží především pro spuštění hlavního algoritmu činnosti vymazávacího systému, který využívá
        rekurzivních volání metody _is_accepted(). Dále před spuštěním samotné funkcionality vymazávacího systému
        metoda ověřuje, zda délka vstupní řetězec nepřesahuje maximální povolenou délku.

        :param input_string: vstupní řetězec, přičemž se jedná o počáteční tvar vstupní pásky.
        :return: pravdivostní hodnota, zda vstupní řetězec je přijat vymazávacím systémem (True) či nikoliv (False).
        :rtype: bool
        :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                           vymazávací systém.
        """
        if len(input_string) > MAXIMUM_RECURSION_DEPTH:
            raise MaximumInputStringLengthExceededException

        if self.__verbose:
            print("------------------------------------------------------------------------------------\n")
            print("#####################")
            print("Start erasing system:")
            print("#####################")
            print("Erasing strings: " + str(self.erasing_strings)[1:-1])
            print("Regular language (expression): " + "".join(self.__regular_language) + "\n")
            print("Input string: " + input_string + "\n\n")

        accepted = self._is_accepted(input_string, "")

        if self.__verbose:
            if accepted:
                print("-> Input string accepted by the erasing system")
                print("###############################################\n")
                print("------------------------------------------------------------------------------------")
            else:
                print("-> Input string rejected by the erasing system")
                print("###############################################\n")
                print("------------------------------------------------------------------------------------")

        return accepted
