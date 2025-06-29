#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is  None or len(a_dictionary) == 0:
        return None
    top_scorer = None
    top_score = 0
    for k, v in a_dictionary.items():
        if v > top_score:
            top_score = v
            top_scorer = k
    return top_scorer
