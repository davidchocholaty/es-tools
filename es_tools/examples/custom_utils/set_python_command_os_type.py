"""Nastavení příkazu python na základě operačního systému.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci, která navrací příslušný příkaz pro spuštění Python3 na základě aktulního operačního
systému.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: set_python_command_os_type.py
"""

from platform import system

from es_tools.custom_exceptions.unknown_platform_system_exception import UnknownPlatformSystemException


def set_python_command_os_type() -> str:
    """Nastavení příkazu python na základě operačního systému.

    :return: příkaz pro Python3 (Linux/macOS: python3, Windows: py).
    :rtype: str
    """
    platform_system = system()
    command = ""

    if platform_system in ["Linux", "Darwin"]:
        command = command + "python3 "
    elif platform_system == "Windows":
        command = command + "py "
    else:
        raise UnknownPlatformSystemException

    return command
