import pathlib
from setuptools import setup, find_packages

ROOT = pathlib.Path(__file__).parent


README = (ROOT / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cardsol",
    version="0.1.2",
    description="Cardinality constrained Solver",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Alirezalm/cardsol.git",
    author="Alireza Olama",
    author_email="alireza.lm69@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages = find_packages(include = ["cardsol*"]),
    include_package_data=True,
    install_requires=["numpy", "scipy", "gurobipy"]
)
