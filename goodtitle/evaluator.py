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
        final_scores = {}
        for scorer, metric in self.scorers:
            score, _ = scorer.compute_score(descriptions, shorthands)
            final_scores[metric] = score
        return final_scores

    def evaluate(self, descriptions, shorthands):
        if self.lowercase:
            refs = self._lowercase(descriptions)
            shorthands = self._lowercase(shorthands)
        final_scores = self.score(descriptions, shorthands)

        # Output results
        for metric in final_scores:
            print(f"{metric}: {final_scores[metric]:.6f}")

        return final_scores