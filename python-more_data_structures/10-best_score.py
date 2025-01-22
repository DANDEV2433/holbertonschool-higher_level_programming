#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
# dit à max() d'utiliser les valeurs du dictionnaire pour comparaison
