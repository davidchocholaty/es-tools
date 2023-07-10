# es-tools
Source code and documentation for the bachelor's thesis [Regulated Language Operations and Their Use](https://www.vut.cz/en/students/final-thesis/detail/141140).

---

Balíček obsahující nástroje reprezentující aplikace nového formálního systému nazývaného *vymazávací systém*.

## Seznam aplikací
| Aplikace vymazávacího systému                              | Příslušející třída (nástroj)                                                           |
|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Vyhledávání proteinů a sekvencí aminokyselin proteinů      | [AminoAcidSequenceSearchTool](es_tools/tools/amino_acid_sequence_search_tool)          |
| Vyvážené závorky v textových editorech                     | [BalancedBracketsTool](es_tools/tools/balanced_brackets_tool)                          |
| Validace řešení problému n dam                             | [NQueensProblemTool](es_tools/tools/n_queens_problem_tool)                             |
| Vlastnosti sekundární struktury RNA                        | [SecondaryStructurePropertiesTool](es_tools/tools/secondary_structure_properties_tool) |
| Vyhledávání sekvencí v DNA, RNA a sekundární struktuře RNA | [SequenceSearchTool](es_tools/tools/sequence_search_tool)                              |

## Manuál pro instalaci balíčku a spuštění ukázkových příkladů
Tento manuál popisuje instalaci balíčku a spuštění ukázkových příkladů pro jednotlivé nástroje.

Ukázkové příklady je možné spustit po instalaci balíčku. Pro demonstrační účely ovšem příslušný nástroj také nabízí spuštění ukázkového příkladu v režimu bez instalace.

### Spuštění příkladu v režimu bez instalace balíčku
Pro spuštění ukázkového příkladu v režimu bez instalace je nutné nacházet se ve složce *examples*, jejíž cesta od kořenové složky projektu (*es-tools*) je *es-tools/es_tools/examples*. Dále se vyžaduje nainstalovaný jazyk Python3 verze 3.10 nebo vyšší. Následně je možné spustit příklad pomocí příkazu:
* Unix/macOS
```console
python3 run_example.py -t název_nástroje -n číselné_označení_testu -i
```
* Windows
```console
py run_example.py -t název_nástroje -n číselné_označení_testu -i
```

Parametr -i (v dlouhé variantě --noinstall) určuje, že má být ukázkový příklad spuštěn
v režimu bez instalace.
Popis významu dalších parametrů nástroje a konkrétní ukázkový příklad blíže představuje sekce [Popis parametrů nástroje a demonstračního příkladu](#parameters-description).

### Instalace balíčku a spuštění příkladu
Pro instalaci balíčku es-tools je nutné nacházet se v kořenové složce projektu — složka es-tools, která obsahuje soubor pyproject.toml. Pro sestavení je vyžadován nainstalovaný jazyk Python3 (pro spuštění programového řešení se požaduje verze 3.10 nebo vyšší) a nástroj pip (otestováno s verzí 22.0.2 ). Dále se požadují balíčky setuptools verze rovna nebo vyšší 43.0.0 (otestováno s verzí 58.1.0 a vyšší) a wheel (otestováno s verzí 0.37.1 a vyšší). Samotnou instalaci lze provést následujícím příkazem (*upozornění: symbol „.“ je součástí příkazu a je nutné jej zadat*):
* Unix/macOS
```console
python3 -m pip install .
```
* Windows
```console
py -m pip install .
```

Po úspěšné instalaci lze přejít ke spuštění jednotlivých ukázkových příkladů. Nejprve je nutné nacházet se ve složce examples, jejíž cesta od kořenové složky projektu je *es-tools/es_tools/examples*. Následně je možné spustit příklad pomocí příkazu:
* Unix/macOS
```console
python3 run_example.py -t název_nástroje -n číselné_označení_testu
```
* Windows
```console
py run_example.py -t název_nástroje -n číselné_označení_testu
```

<h3 id="parameters-description">Popis parametrů nástroje a demonstračního příkladu</h3>

Tato sekce blíže popisuje význam a funkcionalitu jednotlivých parametrů nástroje, který je určen pro spuštění ukázkového příkladu již pro konkrétní nástroj implementující aplikaci vymazávacího systému. Na závěr sekce je představen jeden konkrétní příklad pro aplikaci vymazávacího systému na ověření řešení problému n dam, kterou implementuje nástroj *n_queens_problem_tool*.

Parametry -t (v dlouhé variantě --tool) a -n (v dlouhé variantě --number) jsou povinné a značí po řadě název spouštěného nástroje a číslo spouštěného testu. Název nástroje může nabývat jedné z hodnot:

1. amino_acid_sequence_search_tool
2. balanced_brackets_tool
3. n_queens_problem_tool
4. secondary_structure_properties_tool
5. sequence_search_tool

Číslo spouštěného testu nabývá hodnoty dle počtu testů pro daný nástroj, jenž lze nalézt v přiložené dokumentaci (většinou se pohybuje v rozsahu 1-10) viz sekce [Popis testovacích dat pro ukázkové příklady](#test-data).

Volitelně lze využít parametr -v (v dlouhé variantě --verbose), jenž slouží pro výpis aktuálního tvaru vstupní pásky, jednotlivých použitých vymazávacích řetězců a ověřovaného řetězce vzniklého konkatenací doposud aplikovaných vymazávacích řetězců.

Posledním volitelným parametrem je parametr -l (v dlouhé variantě --lazy). Při zadání uvedeného parametru veškeré vymazávací systémy používají líný kvantifikátor. V opačném případě je využíván chamtivý kvantifikátor jako výchozí.

Lze uvažovat názorný příklad:
* Unix/macOS
```console
python3 run_example.py -t n_queens_problem_tool -n 1 -v -l
```
* Windows
```console
py run_example.py -t n_queens_problem_tool -n 1 -v -l
```

V uvedeném příkladu je spuštěn test číslo *1* pro nástroj *n_queens_problem_tool* při vypisování dodatečných informací pomocí parametru -v a použití líného kvantifikátoru pro vymazávací systémy pomocí parametru -l.

<h2>Manuály pro spuštění jednotlivých nástrojů</h2>

- [AminoAcidSequenceSearchTool](es_tools/tools/amino_acid_sequence_search_tool/README.md)
- [BalancedBracketsTool](es_tools/tools/balanced_brackets_tool/README.md)
- [NQueensProblemTool](es_tools/tools/n_queens_problem_tool/README.md)
- [SecondaryStructurePropertiesTool](es_tools/tools/secondary_structure_properties_tool/README.md)
- [SequenceSearchTool](es_tools/tools/sequence_search_tool/README.md)

<h2 id="test-data">Popis testovacích dat pro ukázkové příklady</h2>

- [Testovací data pro nástroj AminoAcidSequenceSearchTool](es_tools/examples/amino_acid_sequence_search_tool/data/README.md)
- [Testovací data pro nástroj BalancedBracketsTool](es_tools/examples/balanced_brackets_tool/data/README.md)
- [Testovací data pro nástroj NQueensProblemTool](es_tools/examples/n_queens_problem_tool/data/README.md)
- [Testovací data pro nástroj SecondaryStructurePropertiesTool](es_tools/examples/secondary_structure_properties_tool/data/README.md)
- [Testovací data pro nástroj SequenceSearchTool](es_tools/examples/sequence_search_tool/data/README.md)

## Dokumentace
### Vygenerovaná dokumentace
- [HTML dokumentace (cesta: es-tools/docs/_build/html/index.html)](docs/_build/html/index.html)

### Popis vygenerování dokumentace
Možné pouze po nainstalování balíčku *es-tools*. Pro vygenerování dokumentace je zapotřebí mít nainstalované balíčky *sphinx* a *sphinx_rtd_theme*. To lze provést následujícím příkazem:

```console
pip3 install sphinx sphinx_rtd_theme
```

Dále je nutné při generování nacházet se ve složce *docs*, jejíž cesta od kořenové složky projektu je *es-tools/docs*. Poté lze provést vygenerování dokumentace následujícím příkazem:
```console
make html
```
