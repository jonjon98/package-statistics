"""Module setup for Python project."""
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setup(
    name="pckstat-command-line",
    version="0.1",
    author="Jonathan Yap",
    author_email="yapzh.jon@gmail.com",
    description=("A command line interface to allow users to query statistics "
             "of packages obtained from a Debian mirror."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=find_packages(),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "pckstat = api.cli:cli_main",
        ]
    }
)
