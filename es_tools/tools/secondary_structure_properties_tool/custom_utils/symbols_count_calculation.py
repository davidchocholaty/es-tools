"""Výpočet počtu symbolů pro zakódování sekundární struktury RNA na příslušný tvar.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro výpočet počtu symbolů pro zakódování sekundární struktury RNA na příslušný tvar.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: symbols_count_calculation.py
"""

from math import gcd
from typing import Tuple

from es_tools.tools.secondary_structure_properties_tool.custom_utils.custom_constants import PERCENTUAL_DIVIDER


def symbols_count_calculation(percentage_level: int) -> Tuple[int, int]:
    """Výpočet počtu symbolů pro zakódování párových a nepárových nukleotidů sekundární struktury RNA.

    Tato funkce slouží pro výpočet počtu symbolů pro zakódování párových a nepárových nukleotidů sekundární
    struktury RNA. V textu je využitý sled kroků blíže popsaný na straně 57, přičemž jsou použity výrazy 6.1, 6.2 a 6.3.

    :param percentage_level: procentuální hodnota pro výpočet počtu symbolů.
    :type percentage_level: int
    :return: hodnoty pro zakódování po řadě párových a nepárových nukleotidů.
    :rtype: Tuple[int, int]
    """
    greatest_common_divisor = gcd(percentage_level, PERCENTUAL_DIVIDER)

    unpaired_count = int(percentage_level / greatest_common_divisor)
    paired_count = int(PERCENTUAL_DIVIDER / greatest_common_divisor) - unpaired_count

    return paired_count, unpaired_count
