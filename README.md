# A Fancy Title Matters

`fancytitle` is a Python package that offers various evaluation metrics for generating concise and engaging titles, including:

- **WordLikeness**: Measures how much the generated acronym resembles a real word.
- **WordCoverage**: Evaluates the extent of overlap between the acronym and its description.
- **LCSRatio**: Checks the consistency between the acronym and the sequence of letters in its description.

## Key Features

- **Summarization**: Generates descriptions that encapsulate the key idea of a text, such as paper abstracts or article summaries.
- **Neology**: Suggests new, memorable acronyms from the description while adhering to acronym generation constraints.
- **Algorithmic Precision**: Ensures the acronym derives letters sequentially from its description for better clarity and cohesion.

## Installation

You can install `fancytitle` directly from the source code:

```bash
git clone https://github.com/cui-shaobo/goodtitle.git
cd fancytitle
pip install .
```

## Usage

### 1. Using as a Python Script

You can use `fancytitle` within a Python script for evaluating descriptions and their corresponding acronyms.

#### Example: Using the Class Method

The `fancy_title_scores` class method allows you to instantiate and evaluate the titles in one step.
```python
from fancytitle import TitleEvaluator

description = "A Robustly Optimized Pretraining Approach for Language Models"
shorthand = "RoBERTa"

# Use class method to instantiate and evaluate
final_scores = TitleEvaluator.fancy_title_score(description, shorthand, lowercase=True)
```
This will now output the following without errors:

```plaintext
Evaluation Results:
============================================================

Description: a robustly optimized pretraining approach for language models
Shorthand: roberta
------------------------------------------------------------
WordLikeness: 0.5714285714285714
WordCoverage: 0.9230769230769231
LCSRatio: 1.0
============================================================
```


### Example with Multiple Propositions:
```python
from fancytitle import TitleEvaluator
descriptions = {
    "proposition1": ["A Robustly Optimized Pretraining Approach for Language Models"],
    "proposition2": ["Neural Networks for Image Recognition"]
}
shorthands = {
    "proposition1": ["RoBERTa"],
    "proposition2": ["NNIR"]
}

# Use class method to instantiate and evaluate
final_scores = TitleEvaluator.from_inputs(descriptions, shorthands, lowercase=True)

```

This will now output the following without errors:
```plaintext
Evaluation Results:
============================================================

Description: a robustly optimized bert pretraining approach
Shorthand: roberta
------------------------------------------------------------
WordLikeness: 0.5714285714285714
WordCoverage: 0.9230769230769231
LCSRatio: 1.0
============================================================

Description: a training approach for language models
Shorthand: atalm
------------------------------------------------------------
WordLikeness: 0.6
WordCoverage: 0.8
LCSRatio: 1.0
============================================================
```



### Parameters for Evaluation

The `from_inputs` class method accepts the following parameters:

- **descriptions** (dict): Dictionary where keys are examples and values are lists of descriptions.
- **shorthands** (dict): Dictionary where keys are examples and values are lists of acronyms.
- **wordlikeness** (bool): Whether to compute the WordLikeness metric (default: `True`).
- **wordcoverage** (bool): Whether to compute the WordCoverage metric (default: `True`).
- **lcsratio** (bool): Whether to compute the LCSRatio metric (default: `True`).
- **lowercase** (bool): Whether to convert all inputs to lowercase before evaluation (default: `False`).

## Contributing

We welcome contributions! If you’d like to improve this project, please feel free to fork the repository and submit a pull request with your enhancements.

## License

