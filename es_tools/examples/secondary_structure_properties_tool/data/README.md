# Testovací data ukázkových příkladů pro nástroj SecondaryStructurePropertiesTool

#### Příklad 1
- Popis: vstupní sekvence sekundární struktury RNA obsahuje minimálně 60% párových nukleotidů
- Soubor: 1_accepted.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB73
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/1_min_accepted.txt --min 60
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/1_min_accepted.txt --min 60
  ```
#### Příklad 2
- Popis: vstupní sekvence sekundární struktury RNA obsahuje méně než 80% párových nukleotidů
- Soubor: 2_min_not_accepted.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB207
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/2_min_not_accepted.txt --min 80
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/2_min_not_accepted.txt --min 80
  ```
#### Příklad 3
- Popis:  vstupní sekvence sekundární struktury RNA obsahuje maximálně 60% párových nukleotidů
- Soubor: 3_max_accepted.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB71
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/3_max_accepted.txt --max 60
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/3_max_accepted.txt --max 60
  ```
#### Příklad 4
- Popis:  vstupní sekvence sekundární struktury RNA obsahuje více jak 50% párových nukleotidů
- Soubor: 4_max_not_accepted.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB373
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/4_max_not_accepted.txt --max 50
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/4_max_not_accepted.txt --max 50
  ```
#### Příklad 5
- Popis:  vstupní sekvence sekundární struktury RNA obsahuje minimálně 60% a maximálně 80% párových nukleotidů
- Soubor: 5_both_accepted.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB180
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/5_both_accepted.txt --min 60 --max 80
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/5_both_accepted.txt --min 60 --max 80
  ```
#### Příklad 6
- Popis: vstupní sekvence sekundární struktury RNA obsahuje méně než 80% párových nukleotidů
- Soubor: 6_both_not_accepted_below.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB74
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/6_both_not_accepted_below.txt --min 80 --max 90
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/6_both_not_accepted_below.txt --min 80 --max 90
  ```
#### Příklad 7
- Popis: vstupní sekvence sekundární struktury RNA obsahuje více jak 40% párových nukleotidů
- Soubor: 7_both_not_accepted_above.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB170
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/7_both_not_accepted_above.txt --min 20 --max 40
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/7_both_not_accepted_above.txt --min 20 --max 40
  ```
#### Příklad 8
- Popis: výchozí hodnoty pro minimální (0%) a maximální (100%) procentuální počet párových nukleotidů oproti nukleotidům nepárovým
- Soubor: 8_default_min_max_levels.txt
- Zdroj: https://bprna.cgrb.oregonstate.edu/search.php?query=bpRNA_CRW_1897
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/8_default_min_max_levels.txt
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/8_default_min_max_levels.txt
  ```
#### Příklad 9
- Popis: vstupní sekvence sekundární struktury RNA obsahuje minimálně 50% párových nukleotidů, přičemž vstupní hodnota 57% je zaokrouhlena na hodnotu 50%
- Soubor: 9_min_rounded_accepted.txt
- Zdroj: https://bprna.cgrb.oregonstate.edu/search.php?query=bpRNA_CRW_8496
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/9_min_rounded_accepted.txt --min 57
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/9_min_rounded_accepted.txt --min 57
  ```
#### Příklad 10
- Popis: vstupní sekvence sekundární struktury RNA obsahuje maximálně 70% párových nukleotidů, přičemž vstupní hodnota 71% je zaokrouhlena na hodnotu 70%
- Soubor: 10_max_rounded_accepted.txt
- Zdroj: https://bprna.cgrb.oregonstate.edu/search.php?query=bpRNA_CRW_15563
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/10_max_rounded_accepted.txt --max 71
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/10_max_rounded_accepted.txt --max 71
  ```
#### Příklad 11
- Popis: vstupní sekvence sekundární struktury RNA obsahuje minimálně 50% a maximálně 90% párových nukleotidů, přičemž vstupní hodnoty 57% a 91% jsou zaohrouhleny na hodnoty 50% a 90%
- Soubor: 11_both_rounded_accepted.txt
- Zdroj: https://bprna.cgrb.oregonstate.edu/search.php?query=bpRNA_PDB_650
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/11_both_rounded_accepted.txt --min 57 --max 91
  ```
  * Windows
  ```console
  py es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py -i es_tools/examples/secondary_structure_properties_tool/data/11_both_rounded_accepted.txt --min 57 --max 91
  ```
