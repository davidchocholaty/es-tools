# Nástroj SecondaryStructurePropertiesTool

Nástroj reprezentující aplikaci vymazávacího systému pro ověření vlastností sekundární struktury RNA.

### Použití:
- Unix/macOS
```console
  python3 secondary_structure_properties_tool [-h] [-v] [-l] [-i INPUT] [--min MIN] [--max MAX]
```
- Windows
```console
  py secondary_structure_properties_tool [-h] [-v] [-l] [-i INPUT] [--min MIN] [--max MAX]
```

#### Argumenty:
| Argument nástroje       | Popis argumentu                                                                                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -h, --help              | zobrazí nápovědu                                                                                                                                                      |
| -v, --verbose           | pokud je nastaveno, vytisknou se použité vymazávací řetězce, aktuální tvar vstupní pásky a aktuální tvar řetězce vzniklého konkatenací použitých vymazávacích řetězců |
| -l, --lazy              | pokud je nastaveno, použije se typ líného kvantifikátoru pro použitý vymazávací systém (systémy). Vy výchozím nastavení se používá typ chamtivého kvantifikátoru      |
| -i INPUT, --input INPUT | vstupní soubor se sekundární strukturou RNA na jednom řádku                                                                                                           |
| --min MIN               | minimální procentuální hodnota párových nukleotidů oproti nepárovým nukleotidům                                                                                       |
| --max MAX               | maximální procentuální hodnota párových nukleotidů oproti nepárovým nukleotidům                                                                                       |
