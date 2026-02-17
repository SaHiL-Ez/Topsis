from setuptools import setup, find_packages

setup(
    name="Topsis-Sahil-102316091",
    version="1.0.0",
    author="Sahil Kumar",
    author_email="sahil@example.com",
    description="A Python package for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sahil/topsis",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.main:main",
        ],
    },
)
