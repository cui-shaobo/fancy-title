from setuptools import setup, find_packages

readme = open('READMEpypi.md').read()


setup(
    name='fancy-title',
    version='0.1.3',
    description='Evaluation metrics for your fancy title. The higher the better.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Shaobo Cui',
    author_email='shaobo.cui@epfl.ch',
    license='MIT',
    url='https://github.com/cui-shaobo/fancy-title',
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
