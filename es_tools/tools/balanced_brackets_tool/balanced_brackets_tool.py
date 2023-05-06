"""Nástroj pro ověření vyvážených závorek.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje třídu nástroje reprezentujícího aplikaci vymazávacího systému pro ověření vyvážených závorek.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: balanced_brackets_tool.py
"""

import argparse
import sys

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.internal_error_exception import InternalErrorException
from es_tools.custom_exceptions.invalid_argument_exception import InvalidArgumentException
from es_tools.custom_exceptions.invalid_input_data_structure_exception import InvalidInputDataStructure
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.invalid_transition_exception import InvalidTransitionException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.error_utils.exit_code import ExitCode
from es_tools.handlers.argument_handler.argument_handler import ArgumentHandler
from es_tools.tools.balanced_brackets_tool.custom_utils.custom_erasing_system_creation import create_erasing_system
from es_tools.tools.balanced_brackets_tool.custom_utils.custom_transducer_creation import create_transducer
from es_tools.tools.tool import Tool


class BalancedBracketsTool(Tool):
    """Nástroj reprezentující aplikaci pro ověření vyvážených závorek.

    Tato třída implementuje nástroj realizující navržený algoritmus aplikující vymazávací systém na ověření
    vyvážených závorek. Hlavní algoritmus představený v textu práce na stranách 60-62 reprezentuje metoda
    _run_main_algorithm().
    """
    def __init__(self) -> None:
        """**Konstruktor třídy BalancedBracketsTool**

        Konstruktor slouží pouze pro nastavení základních hodnot atributů třídy, přičemž jsou nastaveny pouze atributy
        zdědené od rodičovské třídy Tool.
        """
        super().__init__()

    def _add_custom_arguments(self, argument_parser: argparse.ArgumentParser) -> None:
        """Metoda pro přidání specifických uživatelských argumentů pro nástroj.

        Tato metoda implementuje přidání specifických uživatelských argumentů ke společným pro všechny nástroje. Metoda
        přepisuje stejnojmennou metodu z rodičovské třídy Tool.

        :param argument_parser: analyzátor uživatelských argumentů.
        :type argument_parser: argparse.ArgumentParser
        """
        argument_parser.add_argument("-i", "--input", dest="input",
                                     help="the input is plain text or a source code file containing brackets")

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
        # Load arguments.
        try:
            argument_handler = self._create_custom_argument_handler()
            self.arguments = argument_handler.parse_arguments()
        except InvalidArgumentException:
            raise

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

    def _run_main_algorithm(self) -> None:
        """Spuštění hlavního algoritmu nástroje.

        Tato metoda implementuje hlavní tok algoritmu nástroje pro ověření vyvážených závorek.

        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů převodníku.
        :raises FinalStatesNotStatesSubsetException: množina konečných stavů převodníku není podmnožinou množiny všech
                                                     stavů.
        :raises InvalidTransitionException: převodník obsahuje neplatný přechod pro splnění požadovaných podmínek.

        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci vymazávacího
                                                  systému.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního jazyka vymazávacího
                                                        systému.
        :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                           vymazávací systém.
        """
        input_text = "".join(self.input_data)

        print("Input file name: " + self.arguments.input)

        try:
            transducer = create_transducer()
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise
        except InvalidTransitionException:
            raise

        generated_output_strings = transducer.run(input_text)
        output_strings = list(generated_output_strings)

        if len(output_strings) != 1:
            print("------------------------------------------------------------------------------------\n")
            print("### Input text rejected by the transducer. ###")
            return

        try:
            erasing_system = create_erasing_system(self.arguments.greedy_quantifier, self.arguments.verbose)
        except IllegalSymbolOccurrenceException:
            raise
        except InvalidRegularLanguagePatternException:
            raise

        try:
            accepted = erasing_system.run(output_strings[0])
        except MaximumInputStringLengthExceededException:
            raise

        if accepted:
            print("------------------------------------------------------------------------------------\n")
            print("### Balanced brackets ###")
        else:
            print("------------------------------------------------------------------------------------\n")
            print("### Unbalanced brackets ###")

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
    """Hlavní funkce pro spuštění nástroje reprezentujícího aplikaci vymazávacího pro ověření vyvážených závorek."""
    tool = BalancedBracketsTool()

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
