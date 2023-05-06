"""Implementace konečného převodníku.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci konečného převodníku dle definic uvedených v textu bakalářské práce
na stranách 19-21. Samotnou funkcionalitu implementují metody příslušné třídy FiniteTransducer, přičemž hlavní logiku
převodníku implementuje metoda run().

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: finite_transducer.py
"""

from typing import Dict, Generator, List, Set, Tuple

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.formal_models.formal_model import FormalModel


class FiniteTransducer(FormalModel):
    """Implementace konečného převodníku.

    Tato třída poskytuje metody, které implementují funkcionalitu konečného převodníku. Kromě konstruktoru, metod
    pro získání či nastavení hodnot, hlavní funkcionalitu představuje metoda run(), která implementuje zpracování
    vstupního řetězce a generování výstupních řetězců s využitím konečného převodníku.

    Třida je zděděna od abstraktní třídy FormalModel, která slouží jako bázová třída pro všechny formální modely
    implementované v celém projektu.
    """

    def __init__(self, transition_relations: List[Tuple[str, str, str, str]],
                 initial_state: str,
                 final_states: Set[str],
                 max_generated_output_string_length_level: int = -1) -> None:
        """**Konstruktor třídy FiniteTransducer**

        Konstruktor slouží především pro nastavení základních entit konečného převodníku, jako je například
        počáteční stav, přechody převodníku nebo množina koncových stavů. Zároveň je nastavena maximální délka
        vygenerovaného výstupního řetězce za účelem zabránění nekonečného generování pomocí epsilon-přechodů převodníku.

        :param transition_relations: přechody konečného převodníku.
        :type transition_relations: List[Tuple[str, str, str, str]]
        :param initial_state: počáteční stav.
        :type initial_state: str
        :param final_states: množina koncových stavů.
        :type final_states: Set[str]
        :param max_generated_output_string_length_level: maximální délka generovaného řetězce (zabránění nekonečného
                                                         generování výstupu pomocí epsilon-přechodů).
        :type max_generated_output_string_length_level: int
        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů.
        :raises FinalStatesNotStatesSubsetException: množina koncových stavů není podmnožinou množiny stavů.
        """
        self.__max_generated_output_string_length_level = max_generated_output_string_length_level
        self.__states = set()
        self.__input_alphabet = set()
        self.__output_alphabet = set()
        self.transition_relations_ = {}
        self.initial_state_ = ""
        self.final_states_ = set()

        self._set_transition_relations(transition_relations)

        try:
            self._set_initial_state(initial_state)
        except InitialStateNotInStatesException:
            raise

        try:
            self._set_final_states(final_states)
        except FinalStatesNotStatesSubsetException:
            raise

    @property
    def states(self) -> Set[str]:
        """Množina stavů definovaného konečného převodníku.

        :getter: získání množiny stavů definovaného konečného převodníku.
        :type: Set[str]
        """
        return self.__states

    @property
    def input_alphabet(self) -> Set[str]:
        """Vstupní abeceda definovaného konečného převodníku.

        :getter: získání vstupní abecedy definovaného konečného převodníku.
        :type: Set[str]
        """
        return self.__input_alphabet

    @property
    def output_alphabet(self) -> Set[str]:
        """Výstupní abeceda definovaného konečného převodníku.

        :getter: získání výstupní abecedy definovaného konečného převodníku.
        :type: Set[str]
        """
        return self.__output_alphabet


    @property
    def transition_relations(self) -> Dict[Tuple[str, str], Tuple[str, str]]:
        """Přechody definovaného konečného převodníku.

        :getter: získání přechodů definovaného konečného převodníku.
        :type: Dict[Tuple[str, str], Tuple[str, str]]
        """
        return self.transition_relations_

    @property
    def initial_state(self) -> str:
        """Počáteční stav definovaného konečného převodníku.

        :getter: získání počátečního stavu definovaného konečného převodníku.
        :type: str
        """
        return self.initial_state_

    @property
    def final_states(self) -> Set[str]:
        """ Množina koncových stavů konečného převodníku.

        :getter: získání množiny koncových stavů konečného převodníku.
        :type: Set[str]
        """
        return self.final_states_

    @property
    def max_generated_output_string_length(self) -> int:
        """Maximální délka výstupního řetězce pro omezení nekonečného generování pomocí epsilon-přechodů.

        :getter: získání maximální nastavené délky výstupního řetězce pro omezení nekonečného generování pomocí
                 epsilon-přechodů.
        :setter: nastavení maximální délky výstupního řetězce pro omezení nekonečného generování pomocí
                 epsilon-přechodů.
        :type: int
        """
        return self.__max_generated_output_string_length_level

    @max_generated_output_string_length.setter
    def max_generated_output_string_length(self, new_max_length: int) -> None:
        self.__max_generated_output_string_length_level = new_max_length

    def _add_transition_relation(self, from_state: str, input_string: str, to_state: str, output_string: str) -> None:
        """Přidání přechodu do slovníku přechodů.

        Tato metoda zajišťuje přidání jednoho přechodu do slovníku obsahujícího jednotlivé přechody konečného
        převodníku. Zároveň s nastavením řetězce, který je přečten ze vstupní pásky, je rozšířena vstupní abeceda
        o nové symboly. To stejné platí pro řetězec zapisovaný na výstupní pásku a pro výstupní abecedu.

        :param from_state: počáteční stav přechodu.
        :type from_state: str
        :param input_string: vstupní řetězec, který při provedení přechodu je přečten ze vstupní pásky.
        :type input_string: str
        :param to_state: konečný stav přechodu.
        :type to_state: str
        :param output_string: výstupní řetězec, který je při provedení přechodu zapsán na výstupní pásku.
        :type output_string: str
        """
        # Přidání stavů do množiny stavů pro případ, pokud ještě nejsou zahrnuty.
        self.__states.add(from_state)
        self.__states.add(to_state)

        # Přidání nových symbolů do vstupní abecedy z řetězce, který má být přečten ze vstupní pásky.
        if input_string != "":
            self.__input_alphabet.union(set(input_string))

        # Přidání nových symbolů do výstupní abecedy z řetězce, který má být zapsán ná výstupní pásku.
        if output_string != "":
            self.__output_alphabet.union(set(output_string))

        head = (from_state, input_string)

        # Rozdělení pro případ, pokud slovník již obsahuje přechod s totožnou vstupní konfigurací.
        if head in self.transition_relations_:
            self.transition_relations_[head].append((to_state, output_string))
        else:
            self.transition_relations_[head] = [(to_state, output_string)]

    def _set_transition_relations(self, transition_relations: List[Tuple[str, str, str, str]]) -> None:
        """Nastavení přechodů do slovníku přechodů.

        Tato metoda nastaví všechny přechody konečného převodníku s využitím metody _add_transition_relation().

        :param transition_relations: seznam přechodů konečného převodníku.
        :type transition_relations: List[Tuple[str, str, str, str]]
        """
        for from_state, input_string, to_state, output_string in transition_relations:
            self._add_transition_relation(from_state,
                                          input_string,
                                          to_state,
                                          output_string)

    def _set_final_states(self, final_states: Set[str]) -> None:
        """Nastavení koncových stavů konečného převodníku.

        Tato metoda nastaví koncové stavy konečného převodníku. Zároveň je provedena kontrola, zda množina koncových
        stavů je podmnožinou množiny stavů definovaného konečného převodníku.

        :param final_states: množina koncových stavů.
        :type final_states: Set[str]
        """
        if not final_states.issubset(self.__states):
            raise FinalStatesNotStatesSubsetException

        self.final_states_ = final_states

    def _set_initial_state(self, initial_state: str) -> None:
        """Nastavení počátečního stavu konečného převodníku.

        Tato metoda nastaví počáteční stav konečného převodníku. Zároveň je provedena kontrola, zda počáteční stav
        náleží do množiny stavů konečného převodníku.

        :param initial_state: počáteční stav.
        :type initial_state: str
        """
        if initial_state not in self.__states:
            raise InitialStateNotInStatesException

        self.initial_state_ = initial_state

    # Následující metoda je založena na kódu, který byl převzat (metoda byla modifikována, ovšem původní zdroj sloužil
    # jako základ kódu pro tuto metodu):
    #
    # Zdrojový web: GitHub.
    # Odkaz na původní metodu: https://github.com/Aunsiels/pyformlang/blob/ab999ff9ba73e4f5f9ec59dd919da1d85038700d/pyformlang/fst/fst.py#L164
    # Odkaz na původní soubor: https://github.com/Aunsiels/pyformlang/blob/ab999ff9ba73e4f5f9ec59dd919da1d85038700d/pyformlang/fst/fst.py
    # Odkaz na původní repozitář: https://github.com/Aunsiels/pyformlang
    # Autor metody: Julien Romero - Aunsiels (https://github.com/Aunsiels).
    #
    # Název článku, ve kterém byla vytvořena zdrojová knihovna: Pyformlang: An Educational Library for Formal Language Manipulation
    # DOI článku: https://doi.org/10.1145/3408877.3432464
    # Autor článku: Julien Romero.
    #
    # *** Začátek převzatého kódu. ***
    def run(self, input_string: str) -> Generator[str, None, None]:
        """Spuštění běhu definovaného konečného převodníku.

        Tato metoda poskytuje fundamentální funkcionalitu běhu konečného převodníku.

        :param input_string: vstupní řetězec.
        :type input_string: str
        :return: navrací všechny vygenerované výstupní řetězce, které je možné získat pro daný vstupní řetězec.
        :rtype: Generator[str, None, None]
        """
        to_process = [(input_string, "", self.initial_state_)]
        # Pro kontrolu, zda aktuální tvar vstupní a výstupní pásky pro daný stav již nebyl zpracováván.
        seen_by_state = {state: [] for state in self.__states}

        while to_process:
            remaining_input_string, generated_output_string, current_state = to_process.pop()

            if (remaining_input_string, generated_output_string) not in seen_by_state[current_state]:
                # Přidání aktuálního tvaru vstupní a výstupní pásky pro současný stav.
                seen_by_state[current_state].append((remaining_input_string, generated_output_string))

                # Vstupní páska byla zcela přečtena a aktuální stav náleží do množiny koncových stavů
                # konečného převodníku.
                if len(remaining_input_string) == 0 and current_state in self.final_states_:
                    yield generated_output_string

                for transition_relation_key in self.transition_relations_:
                    state, expected_input_string = transition_relation_key

                    # Pokud je expected_input_string prázdný řetězec, metoda startswith() taktéž navrací True.
                    if state == current_state and remaining_input_string.startswith(expected_input_string):
                        # Pokud očekávaný vstupní řetězec není prázdný symbol. V opačném případě je ověřováno,
                        # zda je povoleno neomezeně generovat výstupy (hodnota -1) nebo zda délka vygenerovaného
                        # výstupu nepřesahuje maximální povolenou délku.
                        if expected_input_string != "" or (self.__max_generated_output_string_length_level == -1 or
                                                           len(generated_output_string) <
                                                           self.__max_generated_output_string_length_level):
                            # Přidání dalších možných zpracování aktuálního tvaru vstupní pásky pomocí definovaného
                            # konečného převodníku.
                            for next_state, output_string in self.transition_relations_[transition_relation_key]:
                                to_process.append((remaining_input_string[len(expected_input_string):],
                                                   generated_output_string + output_string, next_state))

    # *** Konec převzatého kódu. ***
