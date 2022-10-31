from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="livermore",
    version="0.0.1",
    author="Valeriy Uvarov",
    author_email="Valerion052@gmail.com",
    description="test",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/livermore-Inc/livermore/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)