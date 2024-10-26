from setuptools import setup, find_packages

setup(
    name='fancy-title',
    version='0.0.1.0',
    description='Evaluation metrics for your title.',
    author_email='shaobo.cui@epfl.ch',
    url='https://github.com/cui-shaobo/fancy-title',  # Replace with your URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'transformers',
        'tqdm',
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
