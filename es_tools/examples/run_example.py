"""Skript pro spuštení ukázkového příkladu pro demonstraci funkcionality nástroje.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci pomocného nástroje pro spuštění jednotlivých ukázkových příkladů pro implementované
nástroje reprezentující aplikace vymazávacího systému.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: run_example.py
"""

import sys
import os

from typing import Any

current_script_directory = os.path.dirname(__file__)
project_root_directory = os.path.join(current_script_directory, '..', '..')

if project_root_directory not in sys.path:
    sys.path.append(project_root_directory)

from es_tools.custom_exceptions.internal_error_exception import InternalErrorException  # noqa: E402
from es_tools.custom_exceptions.invalid_argument_exception import InvalidArgumentException  # noqa: E402
from es_tools.custom_exceptions.invalid_example_number_exception import InvalidExampleNumberException  # noqa: E402
from es_tools.custom_exceptions.invalid_tool_name_exception import InvalidToolNameException  # noqa: E402
from es_tools.custom_exceptions.unknown_platform_system_exception import UnknownPlatformSystemException  # noqa: E402
from es_tools.error_utils.exit_code import ExitCode  # noqa: E402
from es_tools.examples.n_queens_problem_tool.run_example_n_queens_problem_tool import \
    run_example_n_queens_problem_tool  # noqa: E402
from es_tools.examples.amino_acid_sequence_search_tool.run_example_amino_acid_sequence_search_tool import \
    run_example_amino_acid_sequence_search_tool  # noqa: E402
from es_tools.handlers.argument_handler.argument_handler import ArgumentHandler  # noqa: E402
from es_tools.examples.balanced_brackets_tool.run_example_balanced_brackets_tool import \
    run_example_balanced_brackets_tool  # noqa: E402
from es_tools.examples.secondary_structure_properties_tool.run_example_secondary_structure_properties_tool import \
    run_example_secondary_structure_properties_tool  # noqa: E402
from es_tools.examples.sequence_search_tool.run_example_sequence_search_tool import \
    run_example_sequence_search_tool  # noqa: E402


def create_custom_argument_handler() -> ArgumentHandler:
    """Vytvoření manipulátoru pro zpracování uživatelských argumentů.

    Tato funkce slouží pro vytvoření manipulátoru pro zpracování uživatelských argumentů. Zároveň jsou přidány vlastní
    specifické argumenty, a to název spouštěného nástroje, číslo spouštěného testu a argumentu určujícího, zda má být
    skript spuštěn v režimu bez instalace balíčku.

    :return: manipulátor pro zpracování uživatelských argumentů.
    :rtype: ArgumentHandler
    """
    argument_handler = ArgumentHandler("run_example")

    argument_handler.handler().add_argument("-t", "--tool", dest="tool_name", type=str, required=True,
                                            help="the name of a tool")
    argument_handler.handler().add_argument("-n", "--number", dest="example_number", type=int, required=True,
                                            help="the number of a example")
    argument_handler.handler().add_argument("-i", "--noinstall", dest="no_install_run", action="store_true",
                                            help="run an example without installing the es-tools package")

    return argument_handler


def run_tool(user_arguments: Any) -> None:
    """Spuštění nástroje pro prezentaci ukázkového příkladu příslušné aplikace.

    Tato funkce implementuje především výběr nástroje dle příslušného uživatelského argumentu.

    :param user_arguments: uživatelské argumenty.
    :type user_arguments: Any
    :raises InternalErrorException: výskyt neočekávané interní chyby programu.
    :raises InvalidExampleNumberException: hodnota čísla příkladu mimo příslušný rozsah.
    :raises InvalidToolNameException: nesprávný název spouštěného nástroje.
    :raises UnknownPlatformSystemException: neznámý operační systém.
    """
    if user_arguments is None:
        raise InternalErrorException

    if user_arguments.tool_name is None or user_arguments.example_number is None or \
            user_arguments.verbose is None or user_arguments.greedy_quantifier is None or \
            user_arguments.no_install_run is None:
        raise InternalErrorException

    print("#######################################")
    print("#         Run example utility         #")
    print("#######################################")

    print("Running tool: n_queens_problem_tool")
    print("Running example: " + str(user_arguments.example_number))
    print("Verbose: " + ("Yes" if user_arguments.verbose else "No"))
    print("Quantifier type: " + ("greedy" if user_arguments.greedy_quantifier else "lazy"))
    print("####################################################################################\n")

    try:
        match user_arguments.tool_name:
            case "amino_acid_sequence_search_tool":
                run_example_amino_acid_sequence_search_tool(user_arguments.no_install_run,
                                                            user_arguments.example_number,
                                                            user_arguments.verbose,
                                                            user_arguments.greedy_quantifier)
            case "balanced_brackets_tool":
                run_example_balanced_brackets_tool(user_arguments.no_install_run,
                                                   user_arguments.example_number,
                                                   user_arguments.verbose,
                                                   user_arguments.greedy_quantifier)
            case "n_queens_problem_tool":
                run_example_n_queens_problem_tool(user_arguments.no_install_run,
                                                  user_arguments.example_number,
                                                  user_arguments.verbose,
                                                  user_arguments.greedy_quantifier)
            case "secondary_structure_properties_tool":
                run_example_secondary_structure_properties_tool(user_arguments.no_install_run,
                                                                user_arguments.example_number,
                                                                user_arguments.verbose,
                                                                user_arguments.greedy_quantifier)
            case "sequence_search_tool":
                run_example_sequence_search_tool(user_arguments.no_install_run,
                                                 user_arguments.example_number,
                                                 user_arguments.verbose,
                                                 user_arguments.greedy_quantifier)
            case other:
                raise InvalidToolNameException
    except InvalidExampleNumberException:
        raise
    except InvalidToolNameException:
        raise
    except UnknownPlatformSystemException:
        raise


def main() -> None:
    """Hlavní funkce pro spuštění ukázkového demonstračního příkladu nástroje reprezentujícího aplikaci vymazávacího
    systému."""
    argument_handler = create_custom_argument_handler()

    try:
        arguments = argument_handler.parse_arguments()
        run_tool(arguments)
    except InternalErrorException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INTERNAL_ERROR.value)
    except InvalidArgumentException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.WRONG_ARGUMENT.value)
    except InvalidExampleNumberException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_EXAMPLE_NUMBER.value)
    except InvalidToolNameException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_ARGUMENT_VALUE.value)
    except UnknownPlatformSystemException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.UNKNOWN_PLATFORM_SYSTEM.value)


if __name__ == "__main__":
    main()
