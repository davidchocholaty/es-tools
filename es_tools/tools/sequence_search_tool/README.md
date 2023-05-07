# Nástroj SequenceSearchTool

Nástroj reprezentující aplikaci vymazávacího systému pro vyhledávání podsekvencí v DNA, RNA sekvenci nebo sekundární struktuře RNA.

### Použití:
- Unix/macOS
```console
  python3 sequence_search_tool [-h] [-v] [-l] [-i INPUT] [-s [SEQUENCES ...]] [-t {53,35,35_reversed,both,both_35_reversed}]
```
- Windows
```console
  py sequence_search_tool [-h] [-v] [-l] [-i INPUT] [-s [SEQUENCES ...]] [-t {53,35,35_reversed,both,both_35_reversed}]
```

#### Argumenty:
| Argument nástroje                                                                                 | Popis argumentu                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -h, --help                                                                                        | zobrazí nápovědu                                                                                                                                                                                                                                                                                                                                           |
| -v, --verbose                                                                                     | pokud je nastaveno, vytisknou se použité vymazávací řetězce, aktuální tvar vstupní pásky a aktuální tvar řetězce vzniklého konkatenací použitých vymazávacích řetězců                                                                                                                                                                                      |
| -l, --lazy                                                                                        | pokud je nastaveno, použije se typ líného kvantifikátoru pro použitý vymazávací systém (systémy). Vy výchozím nastavení se používá typ chamtivého kvantifikátoru                                                                                                                                                                                           |
| -i INPUT, --input INPUT                                                                           | vstupní soubor se sekvencí DNA na dvou řádcích nebo sekvencí RNA nebo sekundární strukturou RNA na jednom řádku                                                                                                                                                                                                                                            |
| -s [SEQUENCES ...], --seq [SEQUENCES ...]                                                         | vyhledávané sekvence (pro nalezení jejich nepřekrývajících se výskytů)                                                                                                                                                                                                                                                                                     |
| -t {53,35,35_reversed,both,both_35_reversed}, --dnatype {53,35,35_reversed,both,both_35_reversed} | typ vyhledávání DNA. Možné hodnoty: 53 (pouze první 5'->3' vlákno), 35 (pouze druhé 3'->5' vlákno, vyhledávání ve směru 5'->3'), 35_reversed (pouze druhé 3'-> 5' vlákno, vyhledávání ve směru 3'->5'), both (hledání na obou vláknech, pro obrácený směr ve směru 5'->3'), both_35_reversed (hledání na obou vláknech, pro obrácený směr ve směru 3'->5') |
