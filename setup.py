from setuptools import setup, find_packages


with open("README.md") as f:
    longDescription = f.read()

setup(
    name="bashfuscator",
    version="0.0.1",
    description="Configurable and extendable Bash obfuscation framework - modified by Malicious Group",
    license="MIT",
    long_description=longDescription,
    author="Andrew LeFevre",
    packages=find_packages(),
)

