# Nástroj AminoAcidSequenceSearchTool

Nástroj reprezentující aplikaci vymazávacího systému pro vyhledávání proteinů a sekvencí aminokyselin proteinů.

### Použití:
- Unix/macOS
```console
  python3 amino_acid_sequence_search_tool [-h] [-v] [-l] [-i INPUT] [-b [SUBSEQUENCES ...]] [-s [SEQUENCES ...]] [-n]
```
- Windows
```console
  py amino_acid_sequence_search_tool [-h] [-v] [-l] [-i INPUT] [-b [SUBSEQUENCES ...]] [-s [SEQUENCES ...]] [-n]
```

#### Argumenty:
| Argument nástroje                                  | Popis argumentu                                                                                                                                                       |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -h, --help                                         | zobrazí nápovědu                                                                                                                                                      |
| -v, --verbose                                      | pokud je nastaveno, vytisknou se použité vymazávací řetězce, aktuální tvar vstupní pásky a aktuální tvar řetězce vzniklého konkatenací použitých vymazávacích řetězců |
| -l, --lazy                                         | pokud je nastaveno, použije se typ líného kvantifikátoru pro použitý vymazávací systém (systémy). Vy výchozím nastavení se používá typ chamtivého kvantifikátoru      |
| -i INPUT, --input INPUT                            | vstupní soubor se sekvencí RNA na jednom řádku                                                                                                                        |
| -b [SUBSEQUENCES ...], --subseq [SUBSEQUENCES ...] | hledané aminokyselinové podsekvence proteinů                                                                                                                          |
| -s [SEQUENCES ...], --seq [SEQUENCES ...]          | hledané celé proteiny (jejich aminokyselinové sekvence)                                                                                                               |
| -n, --nonterminated                                | pokud je nastaven, umožňuje neukončenou proteinovou sekvenci na konci RNA (kódující triplety musí být stále správné a konec musí být triplet)                         |
