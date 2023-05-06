# Nástroj NQueensProblemTool

Nástroj reprezentující aplikaci vymazávacího systému pro ověření pravidel řešení problému n dam.

### Použití:
- Unix/macOS
```console
  python3 n_queens_problem_tool.py [-h] [-v] [-l] [-i INPUT] -n BOARD_SIZE
```
- Windows
```console
  py n_queens_problem_tool.py [-h] [-v] [-l] [-i INPUT] -n BOARD_SIZE
```

#### Argumenty:
| Argument nástroje                | Popis argumentu                                                                                                                                                       |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -h, --help                       | zobrazí nápovědu                                                                                                                                                      |
| -v, --verbose                    | pokud je nastaveno, vytisknou se použité vymazávací řetězce, aktuální tvar vstupní pásky a aktuální tvar řetězce vzniklého konkatenací použitých vymazávacích řetězců |
| -l, --lazy                       | pokud je nastaveno, použije se typ líného kvantifikátoru pro použitý vymazávací systém (systémy). Vy výchozím nastavení se používá typ chamtivého kvantifikátoru      |
| -i INPUT, --input INPUT          | vstupní soubor s řešením problému n dam                                                                                                                               |
| -n BOARD_SIZE, --size BOARD_SIZE | velikost šachovnice pro vstupní řešení problému n královen                                                                                                            |
