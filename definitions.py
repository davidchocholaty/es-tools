"""Definice konstant projektu

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje definice konstant projektu, přičemž obsahuje jedinou konstantu, a to ROOT_DIRECTORY. Ta slouží
především pro využití cesty ke kořenovému adresáři projektu.

Autor: David Chocholatý
Kontakt: xchoch09@stud.fit.vutbr.cz
Soubor: definitions.py
"""


import os

# Následující řádek kódu je převzat:
#
# Zdrojový web: Stack Overflow.
# Odkaz na původní otázku: https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure
# Autor otázky: matanc1 (https://stackoverflow.com/users/1306168/matanc1).
# Autor odpovědi: jrd1 (https://stackoverflow.com/users/866930/jrd1).
#
# *** Začátek převzatého kódu. ***
ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))  # Cesta ke kořenovému adresáři projektu es-tools.
# *** Konec převzatého kódu. ***
