# Testovací data ukázkových příkladů pro nástroj SequenceSearchTool

#### Příklad 1
- Popis: vstupní DNA obsahuje sekvenci *TCAGA* na prvním vláknu ve směru 5'->3'
- Soubor: 1_dna_single_5_3_accepted.txt
- Zdroj 1: https://www.bioinformatics.org/sms2/random_dna.html
- Zdroj 2: https://www.bioinformatics.org/sms/rev_comp.html
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/1_dna_single_5_3_accepted.txt -s TCAGA -t 53
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/1_dna_single_5_3_accepted.txt -s TCAGA -t 53
  ```
#### Příklad 2
- Popis: vstupní DNA obsahuje sekvenci *TCACCATC* na druhém vláknu ve směru 3'->5' (vyhledávání ve směru 3'->5')
- Soubor: 2_dna_single_3_5_reversed_accepted.txt
- Zdroj 1: https://www.bioinformatics.org/sms2/random_dna.html
- Zdroj 2: https://www.bioinformatics.org/sms/rev_comp.html
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/2_dna_single_3_5_reversed_accepted.txt -s TCACCATC -t 35_reversed
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/2_dna_single_3_5_reversed_accepted.txt -s TCACCATC -t 35_reversed
  ```
#### Příklad 3
- Popis: vstupní DNA neobsahuje sekvenci *ATCTCGGGAGGCG* na druhém vláknu ve směru 3'->5' (vyhledávání ve směru 5'->3')
- Soubor: 3_dna_single_3_5_rejected.txt
- Zdroj 1: https://www.bioinformatics.org/sms2/random_dna.html
- Zdroj 2: https://www.bioinformatics.org/sms/rev_comp.html
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/3_dna_single_3_5_rejected.txt -s ATCTCGGGAGGCG -t 35
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/3_dna_single_3_5_rejected.txt -s ATCTCGGGAGGCG -t 35
  ```
#### Příklad 4
- Popis: vstupní DNA obsahuje obě sekvence: *GTCAAA* ve druhém vláknu ve směru 3'->5' při vyhledávání ve směru 5'->3', *GAGGC* v prvním vláknu ve směru 5'->3'
- Soubor: 4_dna_both_accepted.txt
- Zdroj 1: https://www.bioinformatics.org/sms2/random_dna.html
- Zdroj 2: https://www.bioinformatics.org/sms/rev_comp.html
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/4_dna_both_accepted.txt -s GTCAAA GAGGC -t both
  ```
  * Windows
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/4_dna_both_accepted.txt -s GTCAAA GAGGC -t both
  ```
#### Příklad 5
- Popis: vstupní RNA sekvence obsahuje podsekvenci *CGAUUGGGA*
- Soubor: 5_rna_search_single_accepted.txt
- Zdroj: https://bprna.cgrb.oregonstate.edu/search.php?query=bpRNA_CRW_1897
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/5_rna_search_single_accepted.txt -s CGAUUGGGA
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/5_rna_search_single_accepted.txt -s CGAUUGGGA
  ```
#### Příklad 6
- Popis: vstupní RNA sekvence neobsahuje podsekvenci *CGAUUAA*
- Soubor: 6_rna_search_single_rejected.txt
- Zdroj: https://bprna.cgrb.oregonstate.edu/search.php?query=bpRNA_CRW_1897
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/6_rna_search_single_rejected.txt -s CGAUUAA
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/6_rna_search_single_rejected.txt -s CGAUUAA
  ```
#### Příklad 7
- Popis: vstupní RNA sekvence obsahuje podsekvence *GUCA*, *CCC* a *UUU*
- Soubor: 7_rna_search_multiple_accepted.txt
- Zdroj: https://bprna.cgrb.oregonstate.edu/search.php?query=bpRNA_CRW_8496
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/7_rna_search_multiple_accepted.txt -s GUCA CCC UUU
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/7_rna_search_multiple_accepted.txt -s GUCA CCC UUU
  ```
#### Příklad 8
- Popis: vstupní RNA sekvence neobsahuje všechny podsekvence *GUCA*, *CCC* a *AAA*
- Soubor: 8_rna_search_multiple_rejected.txt
- Zdroj: https://bprna.cgrb.oregonstate.edu/search.php?query=bpRNA_CRW_8496
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/8_rna_search_multiple_rejected.txt -s GUCA CCC AAA
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/8_rna_search_multiple_rejected.txt -s GUCA CCC AAA
  ```
#### Příklad 9
- Popis: vstupní sekvence sekundární struktury RNA obsahuje podsekvence "[[[:)):" a "(((:"
- Soubor: 9_rna_secondary_structure_accepted.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB180
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/9_rna_secondary_structure_accepted.txt -s "[[[:)):" "(((:"
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/9_rna_secondary_structure_accepted.txt -s "[[[:)):" "(((:"
  ```
#### Příklad 10
- Popis: vstupní sekvence sekundární struktury RNA neobsahuje všechny podsekvence "::::::::::::" a ":[[:[[" 
- Soubor: 10_rna_secondary_structure_rejected.txt
- Zdroj: https://rnavlab.utep.edu/static/PKB_files/PKB373
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/10_rna_secondary_structure_rejected.txt -s "::::::::::::" ":[[:[["
  ```
  * Windows
  ```console
  py es_tools/tools/sequence_search_tool/sequence_search_tool.py -i es_tools/examples/sequence_search_tool/data/10_rna_secondary_structure_rejected.txt -s "::::::::::::" ":[[:[["
  ```
