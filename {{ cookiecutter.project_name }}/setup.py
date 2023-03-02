from setuptools import setup, find_packages
import pathlib

def get_version():
    # Edited from https://packaging.python.org/guides/single-sourcing-package-version/
    init_path = pathlib.Path(__file__).parent / "{{ cookiecutter.package_name }}/__init__.py"
    for line in init_path.open("r").readlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="{{ cookiecutter.project_name }}",
    version=get_version(),
    description="{{ cookiecutter.project_short_description }}",
    author="Nelen & Schuurmans",
    author_email="info@nelen-schuurmans.nl",
    url="https://github.com/nens/{{ cookiecutter.project_name }}",
    packages=find_packages(include="{{ cookiecutter.package_name }}*"),
    python_requires=">=3.7",
)
