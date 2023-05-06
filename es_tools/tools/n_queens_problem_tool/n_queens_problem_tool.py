"""Nástroj pro ověření pravidel problému n dam.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje třídu nástroje reprezentujícího aplikaci vymazávacího systému pro ověření pravidel řešení
problému n dam.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: n_queens_problem_tool.py
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
from es_tools.custom_exceptions.invalid_value_exception import InvalidValueException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.error_utils.exit_code import ExitCode
from es_tools.handlers.argument_handler.argument_handler import ArgumentHandler
from es_tools.tools.n_queens_problem_tool.custom_utils.custom_constants import INPUT_LINES_NUMBER
from es_tools.tools.n_queens_problem_tool.custom_utils.custom_transducer_creation import create_transducer
from es_tools.tools.n_queens_problem_tool.custom_utils.custom_erasing_system_base_coordinates_creation \
    import create_erasing_system_base_coordinates
from es_tools.tools.n_queens_problem_tool.custom_utils.custom_erasing_system_diagonal_coordinates_creation \
    import create_erasing_system_diagonal_coordinates
from es_tools.tools.n_queens_problem_tool.custom_utils.convert_to_diagonal_axes import \
    convert_to_diagonal_axes
from es_tools.tools.tool import Tool


class NQueensProblemTool(Tool):
    """Nástroj reprezentující aplikaci pro ověření pravidel řešení problému n dam.

    Tato třída implementuje nástroj realizující navržený algoritmus aplikující vymazávací systém na ověření
    pravidel řešení problému n dam. Hlavní algoritmus představený v textu práce na stranách 62-67 reprezentuje metoda
    _run_main_algorithm().
    """
    def __init__(self) -> None:
        """**Konstruktor třídy NQueensProblemTool**

        Konstruktor slouží pouze pro nastavení základních hodnot atributů třídy, přičemž jsou nastaveny atributy
        zdědené od rodičovské třídy Tool. Jediným atributem, který je specifický pro třídu NQueensProblemTool je
        atribut __board_size určující rozměry šachovnice pro řešení zadané ve vstupním souboru.
        """
        super().__init__(INPUT_LINES_NUMBER)
        self.__board_size = 1

    @property
    def board_size(self) -> int:
        """Rozměr šachovnice pro vstupní řešení problému n dam.

        :getter: získání rozměru šachovnice pro vstupní řešení.
        :setter: nastavení nového rozměru šachovnice pro vstupní řešení.
        :type: int
        """
        return self.__board_size

    @board_size.setter
    def board_size(self, board_size: int) -> None:
        if board_size < 1:
            raise InvalidValueException

        self.__board_size = board_size

    def _add_custom_arguments(self, argument_parser: argparse.ArgumentParser) -> None:
        """Metoda pro přidání specifických uživatelských argumentů pro nástroj.

        Tato metoda implementuje přidání specifických uživatelských argumentů ke společným pro všechny nástroje. Metoda
        přepisuje stejnojmennou metodu z rodičovské třídy Tool.

        :param argument_parser: analyzátor uživatelských argumentů.
        :type argument_parser: argparse.ArgumentParser
        """
        argument_parser.add_argument("-i", "--input", dest="input",
                                     help="the input file with the solution to the n queens problem")
        argument_parser.add_argument("-n", "--size", dest="board_size", type=int, required=True,
                                     help="the size of the board for the input solution of the n queens problem")

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

        if self.arguments.board_size is not None:
            try:
                self.board_size = self.arguments.board_size
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

    def _run_main_algorithm(self) -> None:
        """Spuštění hlavního algoritmu nástroje.

        Tato metoda implementuje hlavní tok algoritmu nástroje pro ověření pravidel problému n dam.

        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů převodníku.
        :raises FinalStatesNotStatesSubsetException: množina konečných stavů převodníku není podmnožinou množiny všech
                                                     stavů.
        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci vymazávacího
                                                  systému.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního jazyka vymazávacího
                                                        systému.
        :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                           vymazávací systém.
        """
        input_solution = self.input_data[0]

        print("Input n queens problem solution: " + input_solution)
        print("Entered board size: " + str(self.arguments.board_size))
        print("\n")

        try:
            transducer = create_transducer(self.__board_size)
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise

        generated_output_strings = transducer.run(input_solution)
        output_strings = list(generated_output_strings)

        if len(output_strings) != 1:
            print("------------------------------------------------------------------------------------\n")
            print("### Input solution rejected by the transducer. ###")
            return

        try:
            erasing_system_base_coordinates = create_erasing_system_base_coordinates(self.__board_size,
                                                                                     self.arguments.greedy_quantifier,
                                                                                     self.arguments.verbose)
        except IllegalSymbolOccurrenceException:
            raise
        except InvalidRegularLanguagePatternException:
            raise

        try:
            accepted = erasing_system_base_coordinates.run(output_strings[0])
        except MaximumInputStringLengthExceededException:
            raise

        if not accepted:
            print("------------------------------------------------------------------------------------\n")
            print("### Unvalid solution ###")
            return

        # Převod do diagonálních souřadnic.
        solution_in_diagonal_axes = convert_to_diagonal_axes(self.__board_size, output_strings[0])

        try:
            erasing_system_diagonal_coordinates = create_erasing_system_diagonal_coordinates(
                self.__board_size,
                self.arguments.greedy_quantifier,
                self.arguments.verbose)
        except IllegalSymbolOccurrenceException:
            raise
        except InvalidRegularLanguagePatternException:
            raise

        try:
            accepted = erasing_system_diagonal_coordinates.run(solution_in_diagonal_axes)
        except MaximumInputStringLengthExceededException:
            raise

        if not accepted:
            print("------------------------------------------------------------------------------------\n")
            print("### Valid solution ###")
        else:
            print("------------------------------------------------------------------------------------\n")
            print("### Unvalid solution ###")

    def run(self) -> None:
        """Spuštění běhu nástroje.

        Cílem této metody je spuštění inicializace nástroje a poté samotného hlavního algoritmu implementované aplikace
        vymazávacího systému.

        :raises OSError: chyba při pokusu o načtení vstupních dat ze souboru (soubor neexistuje, jedná se o adresář,
                         ...).
        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises InvalidArgumentException: zadání neplatného uživatelského argumentu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises InvalidValueException: neplatná hodnota argumentu.
        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci vymazávacího
                                                  systému.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního jazyka vymazávacího
                                                        systému.
        :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                           vymazávací systém.
        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů převodníku.
        :raises FinalStatesNotStatesSubsetException: množina konečných stavů převodníku není podmnožinou množiny všech
                                                     stavů.
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


def main() -> None:
    """Hlavní funkce pro spuštění nástroje reprezentujícího aplikaci vymazávacího pro ověření pravidel řešení problému
    n dam."""
    tool = NQueensProblemTool()

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


if __name__ == "__main__":
    main()
