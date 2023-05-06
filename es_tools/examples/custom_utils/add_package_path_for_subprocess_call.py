"""Přidání cesty aktuální pracovní složky do PYTHONPATH pro spuštění podprocesu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci, která přidává do PYTHONPATH aktuální pracovní složku před spuštěním podprocesu.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: add_package_path_for_subprocess_call.py
"""

import os


# Následující funkce je založena na kódu, který byl převzat:
#
# Zdrojový web: Stack Overflow.
# Odkaz na původní otázku: https://stackoverflow.com/questions/49472326/call-python-script-with-custom-sys-path
# Autor otázky: user9309163
# Autor odpovědi: Stephen Rauch (https://stackoverflow.com/users/7311767/stephen-rauch)
# Odpověď upravena na základě rady od: Mad Physicist (https://stackoverflow.com/users/2988730/mad-physicist)
#
# *** Začátek převzatého kódu. ***
def add_package_path_for_subprocess_call():
    """Přidání cesty aktuální pracovní složky do PYTHONPATH pro spuštění podprocesu.

    Tato funkce přidává do PYTHONPATH cestu aktuální pracovní složky před spuštěním podprocesu. Funkcionalita této
    funkce se využívá při spuštění v režimu bez instalace balíčku.
    """
    script_directory_to_add = os.getcwd()
    path = os.environ.get('PYTHONPATH', script_directory_to_add).split(os.pathsep)

    if script_directory_to_add not in path:
        path.append(script_directory_to_add)
    os.environ['PYTHONPATH'] = os.pathsep.join(path)
# *** Konec převzatého kódu. ***
