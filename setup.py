from setuptools import setup, find_packages
import importlib.metadata

version_string_of_fortmes_pypi = importlib.metadata.version('fortmes.pypi')
print(version_string_of_fortmes_pypi)

setup(
    name="fortmes-pypi",
    version="0.1.15",
    packages=find_packages(),
    install_requires=["aiohttp", "asyncio", "logging"],
)
