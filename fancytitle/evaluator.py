from fancytitle import WordLikeness, WordCoverage, LCSRatio


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
        return {k: [s.lower() for s in v] for k, v in inputs.items()} if isinstance(inputs, dict) else [s.lower() for s
                                                                                                        in inputs]

    def score(self, descriptions, shorthands):
        all_final_scores = {}
        avg_final_scores = {}
        for scorer, metric in self.scorers:
            avg_score, all_scores = scorer.compute_score(descriptions, shorthands)
            avg_final_scores[metric] = avg_score
            all_final_scores[metric] = {key: score for key, score in zip(descriptions.keys(), all_scores)}

        # print(all_final_scores)
        return avg_final_scores, all_final_scores

    def evaluate(self, descriptions, shorthands):
        if self.lowercase:
            descriptions = self._lowercase(descriptions)
            shorthands = self._lowercase(shorthands)

        avg_final_scores, all_final_scores = self.score(descriptions, shorthands)

        # Format the output beautifully
        print("\nEvaluation Results:\n" + "=" * 60)
        for key in descriptions:
            print(f"\nDescription: {descriptions[key][0]}")
            print(f"Shorthand: {shorthands[key][0]}")
            print("-" * 60)
            for metric in all_final_scores:
                print(f"{metric}: {all_final_scores[metric][key]}")
            print("=" * 60)

        return avg_final_scores, all_final_scores

    @classmethod
    def fancy_title_score(cls, descriptions, shorthands, wordlikeness=True, wordcoverage=True, lcsratio=True,
                          lowercase=False):
        """
        Class method to directly instantiate the evaluator and evaluate the given inputs.
        Supports both single and multiple title evaluations, accepting strings or dictionaries.
        """
        # If inputs are strings, convert them to dictionary format
        if isinstance(descriptions, str) and isinstance(shorthands, str):
            descriptions = {"single_input": [descriptions]}
            shorthands = {"single_input": [shorthands]}

        evaluator = cls(wordlikeness=wordlikeness, wordcoverage=wordcoverage, lcsratio=lcsratio, lowercase=lowercase)
        return evaluator.evaluate(descriptions, shorthands)
