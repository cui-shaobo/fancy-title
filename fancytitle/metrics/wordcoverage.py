#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import difflib
import nltk
import pandas as pd
import os

help(difflib)

class WordCoverage(object):
    """
    Class for computing WordCoverage score for generated shorthands.
    Note that this evaluation metric doesn't use the ground truth for evaluation.
    Besides, WordLikeness is case-insensitive.
    """

    def __init__(self, tokenizer_type='t5-base'):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        rel_path = "../data/frequent_words.csv"
        abs_file_path = os.path.join(script_dir, rel_path)
        self._dictionary = pd.read_csv(abs_file_path, keep_default_na=False)["word"].tolist()

    def _wc(self, word_to_match: str):
        return max(difflib.SequenceMatcher(None, word_to_match, word).ratio() for word in self._dictionary)

    def compute_score(self, descriptions, shorthands):
        from tqdm import tqdm
        print("Computing WordCoverage score...")

        assert len(descriptions.keys()) == len(shorthands.keys())

        scores = []
        for idx in tqdm(descriptions.keys()):
            shorthand = "".join(shorthands[idx][0].split()).lower()
            description = descriptions[idx][0].lower()
            if shorthand == "" or description == "":
                score = 0
            else:
                score = self._wc(shorthand)
            scores.append(score)

        return sum(scores) / len(scores), scores

    @staticmethod
    def method():
        return "WordCoverage"