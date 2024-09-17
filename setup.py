from setuptools import setup, find_packages

setup(
    name="datetime_utils",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytz",
    ],
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description=(
        "This is a Python package that provides general utility functions for "
        "managing and manipulating datetime objects. It includes features for "
        "scheduling, formatting, and timezone handling, with the flexibility "
        "to extend its capabilities as needed."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/datetime_utils",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
