# Nástroj BalancedBracketsTool

Nástroj reprezentující aplikaci vymazávacího systému pro ověření vyvážených závorek.

### Použití:
- Unix/macOS
```console
  python3 balanced_brackets_tool.py [-h] [-v] [-l] [-i INPUT]
```
- Windows
```console
  py balanced_brackets_tool.py [-h] [-v] [-l] [-i INPUT]
```

#### Argumenty:
| Argument nástroje                | Popis argumentu                                                                                                                                                       |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -h, --help                       | zobrazí nápovědu                                                                                                                                                      |
| -v, --verbose                    | pokud je nastaveno, vytisknou se použité vymazávací řetězce, aktuální tvar vstupní pásky a aktuální tvar řetězce vzniklého konkatenací použitých vymazávacích řetězců |
| -l, --lazy                       | pokud je nastaveno, použije se typ líného kvantifikátoru pro použitý vymazávací systém (systémy). Vy výchozím nastavení se používá typ chamtivého kvantifikátoru      |
| -i INPUT, --input INPUT          | vstupní soubor obsahující prostý text nebo soubor zdrojového kódu obsahujícího závorky                                                                                |
