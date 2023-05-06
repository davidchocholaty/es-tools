# Testovací data ukázkových příkladů pro nástroj AminoAcidSequenceSearchTool

#### Příklad 1
- Popis: protein složený ze sekvence aminokyselin *MALGHR* se nachází ve vstupní prokaryotické RNA sekvenci
- Soubor: 1_protein_accepted.txt
- Zdroj: https://rnacentral.org/rna/URS00019F225C/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/1_protein_accepted.txt -s MALGHR -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/1_protein_accepted.txt -s MALGHR -n
  ```
#### Příklad 2
- Popis:  protein složený ze sekvence aminokyselin *MALGHRG* se nenachází ve vstupní prokaryotické RNA sekvenci
- Soubor: 2_protein_rejected.txt
- Zdroj: https://rnacentral.org/rna/URS00019DE172/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/2_protein_rejected.txt -s MALGHRG -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/2_protein_rejected.txt -s MALGHRG -n
  ```
#### Příklad 3
- Popis: sekvence aminokyselin *TSKSLWE* se nachází ve vstupní prokaryotické RNA sekvenci
- Soubor: 3_amino_acid_sequence_accepted.txt
- Zdroj: https://rnacentral.org/rna/URS00019F225C/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/3_amino_acid_sequence_accepted.txt -b TSKSLWE -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/3_amino_acid_sequence_accepted.txt -b TSKSLWE -n
  ```
#### Příklad 4
- Popis: sekvence aminokyselin *DVDVT* se nenachází ve vstupní prokaryotické RNA sekvenci
- Soubor: 4_amino_acid_sequence_rejected.txt
- Zdroj: https://rnacentral.org/rna/URS00019DE172/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/4_amino_acid_sequence_rejected.txt -b DVDVT -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/4_amino_acid_sequence_rejected.txt -b DVDVT -n
  ```  
#### Příklad 5
- Popis: protein složený ze sekvence aminokyselin *MALGHR* a sekvence aminokyselin *DVDVLRET* se oboje nachází ve vstupní prokaryotické RNA sekvenci.
- Soubor: 5_both_accepted.txt
- Zdroj: https://rnacentral.org/rna/URS00019F225C/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/5_both_accepted.txt -s MALGHR -b DVDVLRET -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/5_both_accepted.txt -s MALGHR -b DVDVLRET -n
  ```
#### Příklad 6
- Popis: protein složený ze sekvence aminokyselin *MALGHRG* a sekvence aminokyselin *DVDVLRET* se oboje nachází ve vstupní prokaryotické RNA sekvenci.
- Soubor: 6_both_protein_rejected.txt
- Zdroj: https://rnacentral.org/rna/URS00019DE172/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/6_both_protein_rejected.txt -s MALGHRG -b DVDVLRET -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/6_both_protein_rejected.txt -s MALGHRG -b DVDVLRET -n
  ```
#### Příklad 7
- Popis: proteiny složené ze sekvencí aminokyselin *MALGHR* a *MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR* a sekvence aminokyselin *MAT* a *QAEQN* se náchází vs vstupní prokaryotické RNA sekvenci
- Soubor: 7_both_multiple_accepted.txt
- Zdroj: https://rnacentral.org/rna/URS00019DE172/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/7_both_multiple_accepted.txt -s MALGHR MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR  -b MAT QAEQN -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/7_both_multiple_accepted.txt -s MALGHR MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR  -b MAT QAEQN -n
  ```
#### Příklad 8
- Popis:  proteiny složené ze sekvencí aminokyselin *MALGHR* a *MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR* a sekvence aminokyselin *MATAAQA* a *QAEQN* se náchází vs vstupní prokaryotické RNA sekvenci
- Soubor: 8_both_multiple_rejected_overlapped.txt
- Zdroj: https://rnacentral.org/rna/URS00019DE172/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/8_both_multiple_rejected_overlapped.txt -s MALGHR MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR  -b MATAAQA QAEQN -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/8_both_multiple_rejected_overlapped.txt -s MALGHR MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR  -b MATAAQA QAEQN -n
  ```
#### Příklad 9
- Popis: vstupní data jsou odmítnuta na základě skutečnosti, že poslední aminokyselinová sekvence proteinu není ukončena jedním ze stop kodonů
- Soubor: 9_input_data_rejected_non_terminated.txt
- Zdroj: https://rnacentral.org/rna/URS00019F225C/562
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/9_input_data_rejected_non_terminated.txt -s MALGHRG -b DVDVLRET
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/9_input_data_rejected_non_terminated.txt -s MALGHRG -b DVDVLRET
  ```      
#### Příklad 10
- Popis: vstupní prokaryotická RNA sekvence neobsahuje žádný protein
- Soubor: 10_input_data_without_proteins.txt
- Zdroj: https://rnacentral.org/rna/URS00019F225C/562 (původní sekvence upravena — vymazání všech AUG)
- Příkaz pro spuštění nástroje:
  * Unix/macOS
  ```console
  python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/10_input_data_without_proteins.txt -s MALGHRG -b DVDVLRET -n
  ```
  * Windows
  ```console
  py es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py -i es_tools/examples/amino_acid_sequence_search_tool/data/10_input_data_without_proteins.txt -s MALGHRG -b DVDVLRET -n
  ```       
