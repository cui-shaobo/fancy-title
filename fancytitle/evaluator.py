import collections
from .metrics import WordLikeness, WordCoverage, LCSRatio

class TitleEvaluator(object):
    """
    Evaluator class that computes selected metrics for generated shorthands.
    """

    def __init__(self, wordlikeness=True, wordcoverage=True, lcsratio=True, lowercase=False):
        self.lowercase = lowercase
        self.scorers = []

        if wordlikeness:
            self.scorers.append((WordLikeness(), "WordLikeness"))

        if wordcoverage:
            self.scorers.append((WordCoverage(), "WordCoverage"))

        if lcsratio:
            self.scorers.append((LCSRatio(), "LCSRatio"))

    def _lowercase(self, inputs):
        return {k: [s.lower() for s in v] for k, v in inputs.items()}


    def score(self, descriptions, shorthands):
        all_final_scores = {}
        avg_final_scores = {}
        for scorer, metric in self.scorers:
            avg_score, all_scores = scorer.compute_score(descriptions, shorthands)
            avg_final_scores[metric] = avg_score
            all_final_scores[metric] = all_scores
        return avg_final_scores, all_final_scores

    def evaluate(self, descriptions, shorthands):
        if self.lowercase:
            descriptions = self._lowercase(descriptions)
            shorthands = self._lowercase(shorthands)
        avg_final_scores, all_final_scores = self.score(descriptions, shorthands)

        # Output results
        for metric in all_final_scores:
            print(f"{metric}: {all_final_scores[metric]}")

        return avg_final_scores, all_final_scores

    @classmethod
    def fancy_title_score(cls, descriptions, shorthands, wordlikeness=True, wordcoverage=True, lcsratio=True, lowercase=False):
        """
        Class method to directly instantiate the evaluator and evaluate the given inputs.
        """
        evaluator = cls(wordlikeness=wordlikeness, wordcoverage=wordcoverage, lcsratio=lcsratio, lowercase=lowercase)
        return evaluator.evaluate(descriptions, shorthands)