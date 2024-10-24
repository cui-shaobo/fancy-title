from fancytitle.evaluator import TitleEvaluator

# Prepare your references and hypotheses as dictionaries
refs = {
    0: ['description for shorthand 0'],
    1: ['description for shorthand 1'],
    # ...
}

hypos = {
    0: ['generated shorthand 0'],
    1: ['generated shorthand 1'],
    # ...
}

# Initialize the evaluator
evaluator = TitleEvaluator()

# Evaluate and get the scores
scores = evaluator.evaluate(refs, hypos)

print(scores)
