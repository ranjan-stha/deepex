from setuptools import setup, find_packages

PACKAGE_VERSION = "0.1"
MINOR_RELEASE = "0"

setup(
    name="deep_parser",
    version=f"{PACKAGE_VERSION}.{MINOR_RELEASE}",
    packages=find_packages(where="src"),  # include all packages under src
    package_dir={"": "src"},
    include_package_data=True,

    install_requires=[
        "numpy",
        "PyMuPDF",
        "anytree",
        "pyyaml",
        "beautifulsoup4",
        "lxml",
        "requests-html",
        "readable-content",
        "func_timeout",
        "pyppeteer==0.0.14"
        ],

    author="",
    author_email="",
    description="This package contains parsing utilities for text extraction",

    classifiers=[
        ""
    ]
)
