from setuptools import setup, find_packages

setup(
    name="DDoSProject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "ipykernel",
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn"
    ],
)