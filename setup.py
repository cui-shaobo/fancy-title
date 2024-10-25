from setuptools import setup, find_packages

setup(
    name='goodtitle',
    version='0.1.0',
    description='Evaluation metrics for your title.',
    author='Shaobo Cui',
    author_email='shaobo.cui@epfl.ch',
    url='https://github.com/cui-shaobo/goodtitle',  # Replace with your URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'transformers',
        'tqdm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
