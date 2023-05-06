"""Seznam symbolů a podřetězců, které se nesmí vyskytovat v řetězci obsahujícím regulární výraz pro regulární jazyk.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: not_allowed_regular_language_symbols.py
"""

not_allowed_regular_language_strings = ["{", "}", "<", ">",
                                        "\\", ".", "^", "$",
                                        "?", "#", ":", "!",
                                        "=", "*+", "++"]
