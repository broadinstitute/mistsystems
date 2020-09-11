import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mistsystems",
    version="0.1.1",
    author="Thomas Munzer",
    author_email="tmunzer@juniper.net",
    description="Python Library to use Juniper-Mist APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tmunzer/mistsystems",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)