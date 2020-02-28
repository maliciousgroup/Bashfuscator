from setuptools import setup, find_packages

with open("README.md") as f:
    longDescription = f.read()

setup(
    name="bashfuscator",
    version="0.0.1",
    description="Configurable and extendable Bash obfuscation framework, modified by d3d (Malicious Group)",
    license="MIT",
    long_description=longDescription,
    author="Andrew LeFevre",
    packages=find_packages(),
    scripts=["bashfuscator/bin/44fb466ffe5a424a9ec9a48a9706278c"],
)
