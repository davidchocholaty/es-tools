"""Nástroj pro vyhledávání sekvencí.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje třídu nástroje reprezentujícího aplikaci vymazávacího systému pro vyhledávání podsekvencí
v DNA sekvenci, RNA sekvenci nebo sekundární struktuře RNA.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: sequence_search_tool.py
"""

import argparse
import sys

from es_tools.custom_exceptions.argument_not_expected_exception import ArgumentNotExpectedException
from es_tools.custom_exceptions.data_types_not_match_exception import DataTypesNotMatchException
from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.internal_error_exception import InternalErrorException
from es_tools.custom_exceptions.invalid_argument_exception import InvalidArgumentException
from es_tools.custom_exceptions.invalid_input_data_structure_exception import InvalidInputDataStructure
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.invalid_searched_sequences_exception import InvalidSearchedSequencesException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.custom_exceptions.required_argument_not_provided_exception import RequiredArgumentNotProvidedException
from es_tools.custom_exceptions.unexpected_input_data_type_exception import UnexpectedInputDataTypeException
from es_tools.error_utils.exit_code import ExitCode
from es_tools.handlers.argument_handler.argument_handler import ArgumentHandler
from es_tools.tools.sequence_search_tool.custom_utils.custom_constants import MAX_INPUT_LINES_NUMBER
from es_tools.shared_utils.input_data_check import is_rna_sequence, is_rna_secondary_structure_sequence, \
    is_dna_double_stranded_sequence
from es_tools.tools.sequence_search_tool.custom_utils.data_type import DataType
from es_tools.tools.sequence_search_tool.custom_utils.process_rna_secondary_structure \
    import process_rna_secondary_structure
from es_tools.tools.sequence_search_tool.custom_utils.process_rna_sequence import process_rna_sequence
from es_tools.tools.sequence_search_tool.custom_utils.process_dna_sequence import process_dna_sequence
from es_tools.tools.sequence_search_tool.custom_utils.dna_search_types import dna_search_types
from es_tools.tools.sequence_search_tool.custom_utils.valid_searched_sequences import valid_searched_sequences
from es_tools.tools.tool import Tool


class SequenceSearchTool(Tool):
    """Nástroj reprezentující aplikaci pro vyhledávání podsekvencí v DNA sekvenci, RNA sekvenci nebo sekundární
    struktuře RNA.

    Tato třída implementuje nástroj realizující navržený algoritmus aplikující vymazávací systém na vyhledávání
    podsekvencí v DNA sekvenci, RNA sekvenci nebo sekundární struktuře RNA. Hlavní algoritmus představený v textu práce
    na stranách 51-53 reprezentuje metoda _run_main_algorithm().
    """
    def __init__(self):
        """**Konstruktor třídy SequenceSearchTool**

        Konstruktor slouží pouze pro nastavení základních hodnot atributů třídy, přičemž jsou nastaveny atributy
        zdědené od rodičovské třídy Tool. Čtyřmi atributy, které jsou specifické pro třídu SequenceSearchTool, jsou
        atributy __input_data_type, __sequences_data_type, __sequences a __dna_type. Atribut __input_data_type určuje
        typ dat zadaných ve vstupním souboru a atribut __sequences_data_type určuje typ dat zadaných prostřednictvím
        uživatelských argumentů. Dále atribut __sequences určuje vyhledávané sekvence a atribut __dna_type typ
        vyhledávání ve vláknech DNA.
        """
        super().__init__(MAX_INPUT_LINES_NUMBER)
        self.__input_data_type = DataType.UNSET
        self.__sequences_data_type = DataType.UNSET
        self.__sequences = list()
        self.__dna_type = ""

    def _add_custom_arguments(self, argument_parser: argparse.ArgumentParser) -> None:
        """Metoda pro přidání specifických uživatelských argumentů pro nástroj.

        Tato metoda implementuje přidání specifických uživatelských argumentů ke společným pro všechny nástroje. Metoda
        přepisuje stejnojmennou metodu z rodičovské třídy Tool.

        :param argument_parser: analyzátor uživatelských argumentů.
        :type argument_parser: argparse.ArgumentParser
        """
        argument_parser.add_argument("-i", "--input", dest="input", type=str,
                                     help="the input file with a DNA sequence on two lines or an RNA sequence "
                                          "or RNA secondary structure on a single line")
        argument_parser.add_argument("-s", "--seq", dest="sequences", nargs="*", type=str,
                                     help="searched sequences (to find their non-overlapping occurrences)")
        argument_parser.add_argument("-t", "--dnatype", dest="dna_type", type=str,
                                     choices=dna_search_types,
                                     help="search type for DNA. Possible values: 53 (only the first 5'->3' strand), "
                                          "35 (only the second 3'->5' strand, searching in direction 5'->3'), "
                                          "35_reversed (only the second 3'->5' strand, searching in direction 3'->5'), "
                                          "both (searching on both strands, for the reversed in 5'->3' direction), "
                                          "both_35_reversed (searching on both strands, for the reversed in 3'->5' "
                                          "direction)")

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

    def _set_sequences(self):
        """Nastavení vyhledávaných sekvencí.

        Tato metoda slouží pro nastavení vyhledávaných sekvencí jako atributů třídy. Zároveň jsou provedeny kontroly
        validity vstupních dat.
        """
        if self.arguments.sequences is not None:
            valid, sequences_type = valid_searched_sequences(self.arguments.sequences)
            if valid:
                self.__sequences = self.arguments.sequences
                self.__sequences_data_type = sequences_type
            else:
                raise InvalidSearchedSequencesException
        else:
            raise RequiredArgumentNotProvidedException

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

        try:
            self._set_sequences()
        except InvalidSearchedSequencesException:
            raise
        except RequiredArgumentNotProvidedException:
            raise

        if self.arguments.dna_type is not None:
            self.__dna_type = self.arguments.dna_type

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
        :raises RequiredArgumentNotProvidedException: nezadán požadovaný uživatelský argument.
        :raises InvalidSearchedSequencesException: neplatná vyhledávaná sekvence.
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
        except InvalidSearchedSequencesException:
            raise
        except RequiredArgumentNotProvidedException:
            raise

    def _set_input_data_type(self) -> None:
        """Nastavení typu vstupních dat.

        Tato metoda slouží pro nastavení typu dat ze vstupního souboru a z uživatelských argumentů jako atributů třídy.
        """
        input_data_lines_number = len(self.input_data)

        if input_data_lines_number == DataType.RNA_SEQUENCE.value:
            if is_rna_sequence(self.input_data[0]):
                if self.__sequences_data_type in [DataType.RNA_SEQUENCE, DataType.RNA_OR_DNA_SEQUENCE]:
                    self.__input_data_type = DataType.RNA_SEQUENCE
                else:
                    raise DataTypesNotMatchException
            elif is_rna_secondary_structure_sequence(self.input_data[0]):
                self.__input_data_type = DataType.RNA_SECONDARY_STRUCTURE_SEQUENCE
            else:
                raise UnexpectedInputDataTypeException

        elif input_data_lines_number == DataType.DNA_SEQUENCE.value:
            if is_dna_double_stranded_sequence(self.input_data[0], self.input_data[1]):
                if self.__sequences_data_type in [DataType.DNA_SEQUENCE, DataType.RNA_OR_DNA_SEQUENCE]:
                    self.__input_data_type = DataType.DNA_SEQUENCE
                else:
                    raise DataTypesNotMatchException
            else:
                raise UnexpectedInputDataTypeException
        else:
            raise InvalidInputDataStructure

    def _run_main_algorithm(self) -> None:
        """Spuštění hlavního algoritmu nástroje.

        Tato metoda implementuje hlavní tok algoritmu nástroje pro vyhledávání sekvení.

        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises DataTypesNotMatchException: typy dat ze vstupního souboru a uživatelských argumentů se neshodují.
        :raises UnexpectedInputDataTypeException: zadán neočekávaný typ vstupních dat.
        :raises ArgumentNotExpectedException: zadání neočekávaného argumentu.
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
        try:
            self._set_input_data_type()
        except InvalidInputDataStructure:
            raise
        except DataTypesNotMatchException:
            raise
        except UnexpectedInputDataTypeException:
            raise

        is_rna_type = self.__input_data_type == DataType.RNA_SEQUENCE or \
                      self.__input_data_type == DataType.RNA_SECONDARY_STRUCTURE_SEQUENCE

        if is_rna_type and self.__dna_type != "":
            raise ArgumentNotExpectedException
        try:
            if self.__input_data_type == DataType.RNA_SEQUENCE:
                process_rna_sequence(self.input_data[0],
                                     self.__sequences,
                                     self.arguments.greedy_quantifier,
                                     self.arguments.verbose)
            elif self.__input_data_type == DataType.RNA_SECONDARY_STRUCTURE_SEQUENCE:
                process_rna_secondary_structure(self.input_data[0],
                                                self.__sequences,
                                                self.arguments.greedy_quantifier,
                                                self.arguments.verbose)
            elif self.__input_data_type == DataType.DNA_SEQUENCE:
                process_dna_sequence(self.input_data,
                                     self.__sequences,
                                     self.__dna_type,
                                     self.arguments.greedy_quantifier,
                                     self.arguments.verbose)
            else:
                raise InternalErrorException
        except InternalErrorException:
            raise
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise
        except IllegalSymbolOccurrenceException:
            raise
        except InvalidRegularLanguagePatternException:
            raise
        except MaximumInputStringLengthExceededException:
            raise

    def run(self) -> None:
        """Spuštění běhu nástroje.

        Cílem této metody je spuštění inicializace nástroje a poté samotného hlavního algoritmu implementované aplikace
        vymazávacího systému.

        :raises OSError: chyba při pokusu o načtení vstupních dat ze souboru (soubor neexistuje, jedná se o adresář,
                         ...).
        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises InvalidArgumentException: zadání neplatného uživatelského argumentu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises RequiredArgumentNotProvidedException: nezadán požadovaný uživatelský argument.
        :raises InvalidSearchedSequencesException: neplatná vyhledávaná sekvence.
        :raises ArgumentNotExpectedException: zadání neočekávaného argumentu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises DataTypesNotMatchException: typy dat ze vstupního souboru a uživatelských argumentů se neshodují.
        :raises UnexpectedInputDataTypeException: zadán neočekávaný typ vstupních dat.
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
        except InvalidSearchedSequencesException:
            raise
        except RequiredArgumentNotProvidedException:
            raise

        try:
            self._run_main_algorithm()
        except ArgumentNotExpectedException:
            raise
        except InvalidInputDataStructure:
            raise
        except InternalErrorException:
            raise
        except DataTypesNotMatchException:
            raise
        except UnexpectedInputDataTypeException:
            raise
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
    """Hlavní funkce pro spuštění nástroje reprezentujícího aplikaci vymazávacího pro vyhledávání podsekvencí
    v DNA, RNA sekvenci nebo sekundární struktuře RNA."""
    tool = SequenceSearchTool()

    try:
        tool.run()
    except OSError:
        print("\nError: An attempt to open the file failed (an invalid file was provided).")
        sys.exit(ExitCode.FILE_NOT_FOUND.value)
    except ArgumentNotExpectedException as error:
        print("\nError: " + error.msg)
    except InternalErrorException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INTERNAL_ERROR.value)
    except InvalidArgumentException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.WRONG_ARGUMENT.value)
    except InvalidInputDataStructure as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_INPUT_DATA_STRUCTURE.value)
    except InvalidSearchedSequencesException as error:
        print("\nError: " + error.msg)

        print("One of the following options expected:")
        print("1. RNA sequences.")
        print("2. RNA secondary structure sequences.")
        print("3. DNA sequences.")

        sys.exit(ExitCode.INVALID_ARGUMENT_VALUE.value)
    except RequiredArgumentNotProvidedException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.REQUIRED_ARGUMENT_NOT_PROVIDED.value)
    except DataTypesNotMatchException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_INPUT_DATA_TYPE.value)
    except UnexpectedInputDataTypeException as error:
        print("\nError: " + error.msg)

        print("One of the following options expected:")
        print("1. RNA sequence on a single line.")
        print("2. RNA secondary structure sequence on a single line.")
        print("3. DNA sequence on two lines, when the first line represents the 5->3 strand and the second one "
              "the 3->5 strand.")

        sys.exit(ExitCode.INVALID_INPUT_DATA_TYPE.value)
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
