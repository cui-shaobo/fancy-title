<small>EN | [简体中文](README_zh.md) </small>
# 📝 A Fancy Title Matters 

`fancytitle` is a Python package designed to generate, evaluate, and optimize concise and engaging titles or acronyms. It offers multiple evaluation metrics to ensure the consistency, readability, and creativity of these titles. The package helps you create effective acronyms by balancing three key factors:

- **Shorthand**: The acronym or abbreviated title.
- **Description**: The full text or explanation that the acronym is derived from.

## Example Figure
To illustrate the relationship between shorthand, description, and the various constraints, consider the following example:

![Example Image](images/example.png)

For example, the shorthand `RoBERTa` stands for the description "A Robustly Optimized BERT Pretraining Approach." `fancytitle` will evaluate how well the shorthand aligns with its description based on several metrics:

- **WordLikeness**: Measures how much the acronym resembles a valid word.
- **WordCoverage**: Evaluates the degree to which the acronym covers the words in its description.
- **LCSRatio**: Checks if the acronym follows the sequence of letters from the description.


## 🌟 Key Features ![Key Features](https://img.shields.io/badge/Key_Features-Highlights-orange) 

- **Summarization**: Generates descriptions that encapsulate the key idea of a text, such as paper abstracts or article summaries.
- **Neology**: Suggests new, memorable acronyms from the description while adhering to acronym generation constraints.
- **Algorithmic Precision**: Ensures the acronym derives letters sequentially from its description for better clarity and cohesion.

## 🚀  Installation ![Installation](https://img.shields.io/badge/Installation-Guide-blue)

You can install `fancytitle` directly from the source code:

```bash
git clone https://github.com/cui-shaobo/goodtitle.git
cd fancytitle
pip install .
```

Or, install it directly from PyPI:
```bash
pip install fancy-title
```


## 🛠️ Usage ![Usage](https://img.shields.io/badge/Usage-Instructions-green)

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
final_scores = TitleEvaluator.fancy_title_score(descriptions, shorthands, lowercase=True)

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

The `fancy_title_score` class method accepts the following parameters:

- **descriptions** (dict): Dictionary where keys are examples and values are lists of descriptions.
- **shorthands** (dict): Dictionary where keys are examples and values are lists of acronyms.
- **wordlikeness** (bool): Whether to compute the WordLikeness metric (default: `True`).
- **wordcoverage** (bool): Whether to compute the WordCoverage metric (default: `True`).
- **lcsratio** (bool): Whether to compute the LCSRatio metric (default: `True`).
- **lowercase** (bool): Whether to convert all inputs to lowercase before evaluation (default: `False`).

## 🤝 Contributing [![Contributing](https://img.shields.io/badge/Contributing-Welcome-blue)](./CONTRIBUTING.md) 




We welcome contributions! If you’d like to improve this project, please feel free to fork the repository and submit a pull request with your enhancements.

## 📜 Citation ![Citation](https://img.shields.io/badge/Citation-Required-green) 

If you find this package helpful, please star [this repository](https://github.com/cui-shaobo/fancy-title) and the related repository: [logogram](https://github.com/cui-shaobo/logogram). For academic purposes, please cite our paper:

```bibtex
@inproceedings{cui-etal-2024-unveiling,
    title = "Unveiling the Art of Heading Design: A Harmonious Blend of Summarization, Neology, and Algorithm",
    author = "Cui, Shaobo  and
      Feng, Yiyang  and
      Mao, Yisong  and
      Hou, Yifan  and
      Faltings, Boi",
    editor = "Ku, Lun-Wei  and
      Martins, Andre  and
      Srikumar, Vivek",
    booktitle = "Findings of the Association for Computational Linguistics ACL 2024",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand and virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-acl.368",
    doi = "10.18653/v1/2024.findings-acl.368",
    pages = "6149--6174"
}
```


## ![License](https://img.shields.io/badge/License-MIT-blue)

