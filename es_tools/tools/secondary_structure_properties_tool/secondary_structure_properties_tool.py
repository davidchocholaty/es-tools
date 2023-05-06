"""Nástroj pro ověření vlastností sekundární struktury RNA.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje třídu nástroje reprezentujícího aplikaci vymazávacího systému pro ověření vlastností sekundární
struktury RNA.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: secondary_structure_properties_tool.py
"""

import argparse
import sys

from typing import Tuple

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.internal_error_exception import InternalErrorException
from es_tools.custom_exceptions.invalid_argument_exception import InvalidArgumentException
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.invalid_transition_exception import InvalidTransitionException
from es_tools.custom_exceptions.invalid_value_exception import InvalidValueException
from es_tools.custom_exceptions.invalid_input_data_structure_exception import InvalidInputDataStructure
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.error_utils.exit_code import ExitCode
from es_tools.handlers.argument_handler.argument_handler import ArgumentHandler
from es_tools.shared_utils.input_data_check import is_rna_secondary_structure_sequence
from es_tools.tools.secondary_structure_properties_tool.custom_utils.custom_constants import INPUT_LINES_NUMBER, \
    ABSOLUTE_MIN, ABSOLUTE_MAX, MIN_FLAG, MAX_FLAG
from es_tools.tools.secondary_structure_properties_tool.custom_utils.custom_erasing_system_creation \
    import create_erasing_system
from es_tools.tools.secondary_structure_properties_tool.custom_utils.custom_transducer_creation import create_transducer
from es_tools.tools.secondary_structure_properties_tool.custom_utils.symbols_count_calculation \
    import symbols_count_calculation
from es_tools.tools.tool import Tool


class SecondaryStructurePropertiesTool(Tool):
    """Nástroj reprezentující aplikaci pro ověření vlastností sekundární struktury RNA.

    Tato třída implementuje nástroj realizující navržený algoritmus aplikující vymazávací systém na ověření
    vlastností sekundární struktury RNA. Hlavní algoritmus představený v textu práce na stranách 57-60 reprezentuje
    metoda _run_main_algorithm().
    """

    def __init__(self) -> None:
        """**Konstruktor třídy SecondaryStructurePropertiesTool**

        Konstruktor slouží pouze pro nastavení základních hodnot atributů třídy, přičemž jsou nastaveny atributy
        zdědené od rodičovské třídy Tool. Dvěma atributy, které jsou specifické pro třídu
        SecondaryStructurePropertiesTool, jsou atributy __min a __max. Atribut __min určuje minimální hodnotu
        v procentech a atribut __max určuje maximální hodnotu v procentech.
        """
        super().__init__(INPUT_LINES_NUMBER)
        self.__min = ABSOLUTE_MIN
        self.__max = ABSOLUTE_MAX

    @property
    def min(self) -> int:
        """Minimální hodnota v procentech pro ověření vlastností sekundární struktury RNA.

        :getter: získání minimální hodnoty v procentech.
        :setter: nastavení minimální hodnoty v procentech.
        :type: int
        :raises InvalidValueException: nová nastavovaná hodnota není v povoleném rozsahu nebo je vyšší jak nastavená
                                       maximální hodnota.
        """
        return self.__min

    @min.setter
    def min(self, min_percentual: int) -> None:
        if min_percentual not in range(ABSOLUTE_MIN, ABSOLUTE_MAX + 1):
            raise InvalidValueException
        elif min_percentual > self.__max:
            raise InvalidValueException
        else:
            if min_percentual % 10 != 0:
                min_percentual = min_percentual // 10 * 10

                print("Info: The value of the minimum percentage has been rounded to optimize the calculations "
                      "(rounded down).")
                print("New minimum value: " + str(min_percentual) + "\n")

            self.__min = min_percentual

    @property
    def max(self) -> int:
        """Maximální hodnota v procentech pro ověření vlastností sekundární struktury RNA.

        :getter: získání maximální hodnoty v procentech.
        :setter: nastavení maximální hodnoty v procentech.

        :type: int
        :raises InvalidValueException: nová nastavovaná hodnota není v povoleném rozsahu nebo je nižší jak nastavená
                                       minimální hodnota.
        """
        return self.__max

    @max.setter
    def max(self, max_percentual: int) -> None:
        if max_percentual not in range(ABSOLUTE_MIN, ABSOLUTE_MAX + 1):
            raise InvalidValueException
        elif max_percentual < self.__min:
            raise InvalidValueException
        else:
            if max_percentual % 10 != 0:
                max_percentual = max_percentual // 10 * 10

                print("Info: The value of the maximum percentage has been rounded to optimize the calculations "
                      "(rounded down).")
                print("New maximum value: " + str(max_percentual) + "\n")

            self.__max = max_percentual

    def set_new_min_max(self, min_percentual: int, max_percentual: int) -> None:
        """Nastavení nových hodnot minima a maxima.

        Tato funkce slouží pro společné nastavení specifických argumentů pro daný nástroj, a to minimální a maximální
        hodnoty pro ověření vlastností sekundární struktury RNA.

        :param min_percentual: nová hodnota pro minimum v procentech.
        :type min_percentual: int
        :param max_percentual: nová hodnota pro maximum v procentech.
        :type max_percentual: int
        :raises InvalidValueException: nové nastavované hodnoty pro minimum a maximum nejsou v povoleném rozsahu, nebo
                                       nesplňují podmínku, že minimální hodnota je nižší nebo rovna hodnotě maximální.
        """
        if min_percentual not in range(ABSOLUTE_MIN, ABSOLUTE_MAX + 1):
            raise InvalidValueException
        elif max_percentual not in range(ABSOLUTE_MIN, ABSOLUTE_MAX + 1):
            raise InvalidValueException
        elif min_percentual > max_percentual:
            raise InvalidValueException
        else:
            if min_percentual % 10 != 0:
                min_percentual = min_percentual // 10 * 10

                print("Info: The value of the minimum percentage has been rounded to optimize the calculations "
                      "(rounded down).")
                print("New minimum value: " + str(min_percentual) + "\n")

            if max_percentual % 10 != 0:
                max_percentual = max_percentual // 10 * 10

                print("Info: The value of the maximum percentage has been rounded to optimize the calculations "
                      "(rounded down).")
                print("New maximum value: " + str(max_percentual) + "\n")

            self.__min = min_percentual
            self.__max = max_percentual

    def _add_custom_arguments(self, argument_parser: argparse.ArgumentParser) -> None:
        """Metoda pro přidání specifických uživatelských argumentů pro nástroj.

        Tato metoda implementuje přidání specifických uživatelských argumentů ke společným pro všechny nástroje. Metoda
        přepisuje stejnojmennou metodu z rodičovské třídy Tool.

        :param argument_parser: analyzátor uživatelských argumentů.
        :type argument_parser: argparse.ArgumentParser
        """
        argument_parser.add_argument("-i", "--input", dest="input",
                                     help="the input file with an RNA secondary structure on a single line")
        argument_parser.add_argument("--min", dest="min", type=int, default=0,
                                     help="the minimum percentage value of the pair nucleotides "
                                          "versus non-pair nucleotides")
        argument_parser.add_argument("--max", dest="max", type=int, default=100,
                                     help="the maximum percentage value of the pair nucleotides "
                                          "versus non-pair nucleotides")

    def _create_custom_argument_handler(self) -> ArgumentHandler:
        """Metoda pro vytvoření manipulátoru s uživatelskými argumenty.

        Tato metoda implementuje vytvoření manipulátoru s uživatelskými argumenty, přičemž ke společným argumentům jsou
        přidány i specifické pro tento nástroj. Metoda přepisuje stejnojmennou metody z rodičovské třídy Tool.

        :return: manipulátor s uživatelskými argumenty.
        :rtype: ArgumentHandler
        """
        argument_handler = ArgumentHandler(self.get_tool_name())
        self._add_custom_arguments(argument_handler.handler())

        return argument_handler

    def _load_arguments(self) -> None:
        """Načtení uživatelských argumentů.

        Hlavním cílem této metody je vytvoření manipulátoru s uživatelskými argumenty, včetně přidání specifických
        argumentů ke společným pro všechny nástroje. Zároveň tato metoda, pokud je to možné, provede načtení zadaných
        vstupních hodnot.
        """
        try:
            argument_handler = self._create_custom_argument_handler()
            self.arguments = argument_handler.parse_arguments()
        except InvalidArgumentException:
            raise

        if self.arguments.min is not None and self.arguments.max is not None:
            try:
                self.set_new_min_max(self.arguments.min, self.arguments.max)
            except InvalidValueException:
                raise
        else:
            raise InvalidValueException

        if self.arguments.greedy_quantifier is None or self.arguments.verbose is None:
            raise InternalErrorException

    def _initialize_tool(self) -> None:
        """Inicializace nástroje včetně zpracování vstupních dat.

        Tato metoda slouží pro inicializaci nástroje, to znamená pro načtení vstupních dat ze souboru a zpracování
        uživatelských argumentů.

        :raises OSError: chyba při pokusu o načtení vstupních dat ze souboru (soubor neexistuje, jedná se o adresář,
                         ...).
        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises InvalidArgumentException: zadání neplatného uživatelského argumentu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises InvalidValueException: neplatná hodnota argumentu.
        """
        self.print_tool_name()

        try:
            self._load_arguments()
            self.load_input_data()
        except OSError:
            raise
        except InternalErrorException:
            raise
        except InvalidArgumentException:
            raise
        except InvalidInputDataStructure:
            raise
        except InvalidValueException:
            raise

    def _requirements_met(self, min_max_flag: bool, input_secondary_structure: str) -> Tuple[bool, bool]:
        """Funkce pro ověření vlastností sekundární struktury RNA pro minimum nebo maximum.

        Tato funkce implementuje část hlavního algoritmu aplikace vymazávacího systému na ověření vlastností sekundární
        struktury RNA, která je prezentována v textu na stranách 57-60. Konkrétně se metoda zaměruje na ověření
        vlastností pro jednu konkrétní hodnotu, a to minimální nebo maximální.

        :param min_max_flag: příznak určující, zda má být ověřována minimální nebo maximální hodnota.
        :type min_max_flag: bool
        :param input_secondary_structure: vstupní řetězec obsahující sekundární strukturu RNA.
        :type input_secondary_structure: int
        :return: dvojice obsahující pravdivostní hodnoty, které po řadě určují, zda vstupní řetězec je přijat vstupní
                 částí převodníku a zda převedený řetězec přijme vymazávací systém.
        :rtype: Tuple[bool, bool]
        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů převodníku.
        :raises FinalStatesNotStatesSubsetException: množina konečných stavů převodníku není podmnožinou množiny všech
                                                     stavů.
        :raises InvalidTransitionException: převodník obsahuje neplatný přechod pro splnění požadovaných podmínek.
        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci vymazávacího
                                                  systému.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního jazyka vymazávacího
                                                        systému.
        """
        if min_max_flag:
            percentage = self.__min
        else:
            percentage = self.__max

        paired_count, unpaired_count = symbols_count_calculation(percentage)

        try:
            transducer = create_transducer(paired_count, unpaired_count)
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise
        except InvalidTransitionException:
            raise

        generated_output_strings = transducer.run(input_secondary_structure)
        output_strings = list(generated_output_strings)

        if len(output_strings) != 1:
            return False, False

        try:
            erasing_system = create_erasing_system(min_max_flag,
                                                   self.arguments.greedy_quantifier,
                                                   self.arguments.verbose)
        except IllegalSymbolOccurrenceException:
            raise
        except InvalidRegularLanguagePatternException:
            raise

        return True, erasing_system.run(output_strings[0])

    def _run_main_algorithm(self) -> None:
        """Spuštění hlavního algoritmu nástroje.

        Tato metoda implementuje hlavní tok algoritmu nástroje pro ověření vlastností sekundární struktury RNA.

        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů převodníku.
        :raises FinalStatesNotStatesSubsetException: množina konečných stavů převodníku není podmnožinou množiny všech
                                                     stavů.
        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci vymazávacího
                                                  systému.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního jazyka vymazávacího
                                                        systému.
        :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                           vymazávací systém.
        :raises InvalidTransitionException: převodník obsahuje neplatný přechod pro splnění požadovaných podmínek.
        """
        input_secondary_structure = self.input_data[0]

        print("Input RNA secondary structure: " + input_secondary_structure + "\n")
        print(self.__min)
        print(self.arguments.min)
        print("Entered minimum value:", self.arguments.min if self.__min == self.arguments.min else
            str(self.arguments.min) + " (rounded to: " + str(self.__min) + ")")  # noqa: E128
        print("Entered maximum value:", self.arguments.max if self.__max == self.arguments.max else
            str(self.arguments.max) + " (rounded to: " + str(self.__max) + ")")  # noqa: E128

        if not is_rna_secondary_structure_sequence(input_secondary_structure):
            print("------------------------------------------------------------------------------------\n")
            print("### Invalid input data format - RNA secondary structure expected. ###")
            return

        if self.__min != ABSOLUTE_MIN:
            try:
                accepted_transducer, accepted_erasing_system = self._requirements_met(MIN_FLAG,
                                                                                      input_secondary_structure)
            except IllegalSymbolOccurrenceException:
                raise
            except InvalidRegularLanguagePatternException:
                raise
            except MaximumInputStringLengthExceededException:
                raise
            except InitialStateNotInStatesException:
                raise
            except FinalStatesNotStatesSubsetException:
                raise
            except InvalidTransitionException:
                raise

            if not accepted_transducer:
                print("------------------------------------------------------------------------------------\n")
                print("### Input RNA secondary structure rejected by the transducer. ###")
                return

            if accepted_erasing_system:
                print("------------------------------------------------------------------------------------\n")
                print("### Minimum Accepted ###")
            else:
                print("------------------------------------------------------------------------------------\n")
                print("### Minimum Rejected ###")
        else:
            print("------------------------------------------------------------------------------------\n")
            print("### Minimum Accepted ###")

        if self.__max != ABSOLUTE_MAX:
            try:
                accepted_transducer, accepted_erasing_system = self._requirements_met(MAX_FLAG,
                                                                                      input_secondary_structure)
            except IllegalSymbolOccurrenceException:
                raise
            except InvalidRegularLanguagePatternException:
                raise
            except MaximumInputStringLengthExceededException:
                raise
            except InitialStateNotInStatesException:
                raise
            except FinalStatesNotStatesSubsetException:
                raise
            except InvalidTransitionException:
                raise

            if not accepted_transducer:
                print("------------------------------------------------------------------------------------\n")
                print("### Input RNA secondary structure rejected by the transducer. ###")
                return

            if accepted_erasing_system:
                print("------------------------------------------------------------------------------------\n")
                print("### Maximum Accepted ###")
            else:
                print("------------------------------------------------------------------------------------\n")
                print("### Maximum Rejected ###")
        else:
            print("------------------------------------------------------------------------------------\n")
            print("### Maximum Accepted ###")

    def run(self) -> None:
        """Spuštění běhu nástroje.

        Cílem této metody je spuštění inicializace nástroje a poté samotného hlavního algoritmu implementované aplikace
        vymazávacího systému.

        :raises OSError: chyba při pokusu o načtení vstupních dat ze souboru (soubor neexistuje, jedná se o adresář,
                         ...).
        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises InvalidArgumentException: zadání neplatného uživatelského argumentu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci vymazávacího
                                                  systému.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního jazyka vymazávacího
                                                        systému.
        :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                           vymazávací systém.
        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů převodníku.
        :raises FinalStatesNotStatesSubsetException: množina konečných stavů převodníku není podmnožinou množiny všech
                                                     stavů.
        :raises InvalidTransitionException: převodník obsahuje neplatný přechod pro splnění požadovaných podmínek.
        """
        try:
            self._initialize_tool()
        except OSError:
            raise
        except InternalErrorException:
            raise
        except InvalidArgumentException:
            raise
        except InvalidInputDataStructure:
            raise
        except InvalidValueException:
            raise

        try:
            self._run_main_algorithm()
        except IllegalSymbolOccurrenceException:
            raise
        except InvalidRegularLanguagePatternException:
            raise
        except MaximumInputStringLengthExceededException:
            raise
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise
        except InvalidTransitionException:
            raise


def main() -> None:
    """Hlavní funkce pro spuštění nástroje reprezentujícího aplikaci vymazávacího pro ověření vlastností sekundární
    struktury RNA."""
    tool = SecondaryStructurePropertiesTool()

    try:
        tool.run()
    except OSError:
        print("\nError: An attempt to open the file failed (an invalid file was provided).")
        sys.exit(ExitCode.FILE_NOT_FOUND.value)
    except InternalErrorException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INTERNAL_ERROR.value)
    except InvalidArgumentException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.WRONG_ARGUMENT.value)
    except InvalidInputDataStructure as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_INPUT_DATA_STRUCTURE.value)
    except InvalidValueException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_ARGUMENT_VALUE.value)
    except IllegalSymbolOccurrenceException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_ERASING_STRING.value)
    except InvalidRegularLanguagePatternException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_REGULAR_LANGUAGE.value)
    except MaximumInputStringLengthExceededException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.MAXIMUM_INPUT_STRING_LENGTH_EXCEEDED.value)
    except InitialStateNotInStatesException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INITIAL_STATE_NOT_IN_STATES.value)
    except FinalStatesNotStatesSubsetException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.FINAL_STATES_NOT_STATES_SUBSET.value)
    except InvalidTransitionException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_TRANSITION.value)


if __name__ == "__main__":
    main()
