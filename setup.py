from setuptools import setup, find_packages

# import importlib.metadata
import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
print(data["project"]["version"])

setup(
    name="fortmes-pypi",
    version="0.1.16",
    packages=find_packages(),
    # install_requires=["aiohttp", "asyncio", "logging"],
)
