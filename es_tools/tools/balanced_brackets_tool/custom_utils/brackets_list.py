"""Seznam všech možných symbolů pro závorky a jejich odpovádajících symbolů pro převod.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje seznam všech možných symbolů závorek pro nástroj na ověření vyvážených závorek. Ke každému
symbolu je přiložen odpovídající symbol. Ten je potřebný při převodu řetězce pro vymazávací systém za účelem odstranění
nepovolených znaků ze vstupního řetězce.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: brackets_list.py
"""


brackets_list = [("(", "A"),
                 (")", "a"),
                 ("[", "B"),
                 ("]", "b"),
                 ("{", "C"),
                 ("}", "c")]
