import torch
from setuptools import find_packages, setup

requirements = ["transformers>=4.26.1", "nltk==3.7", "torch>=1.13.0"]

setup(
    name="ViNLP",
    version="1.0",
    author="Nguyen Van Nha",
    url="https://github.com/bino282/ViNLP",
    description="A NLP toolkit for Vietnamese",
    install_requires=requirements,
    packages=find_packages()
)
