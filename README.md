# Topsis-Sahil-102316091

[![PyPI version](https://badge.fury.io/py/Topsis-Sahil-102316091.svg)](https://badge.fury.io/py/Topsis-Sahil-102316091)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package to implement **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution), a multi-criteria decision analysis method.

---

## 📋 Table of Contents
- [Installation](#installation)
- [Part 1: Command Line Usage](#part-1-command-line-usage)
- [Part 2: Library Usage](#part-2-library-usage)
- [Part 3: Web Service](#part-3-web-service)
- [License](#license)

---

## 📦 Installation

You can install the package directly from PyPI:

```bash
pip install Topsis-Sahil-102316091
```

---

## Part 1: Command Line Usage

You can use the `topsis` command directly in your terminal to process CSV files.

### Syntax
```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Parameters
1.  **InputDataFile**: Path to the input CSV file. Must contain numeric data from the 2nd column onwards.
2.  **Weights**: Comma-separated weights (e.g., `1,1,1,1`).
3.  **Impacts**: Comma-separated impacts (`+` for beneficial, `-` for non-beneficial).
4.  **OutputResultFileName**: Name of the output CSV file to save results.

### Example
```bash
topsis data.csv "1,1,1,1,1" "+,+,+,+,+" result.csv
```

---

## Part 2: Library Usage

You can import the package in your Python scripts.

```python
from topsis.main import topsis_logic
import pandas as pd

# Load your dataset
df = pd.read_csv("data.csv")

# processing...
# ...
```

---

## Part 3: Web Service

A user-friendly web interface is provided to use the TOPSIS method without writing code.

### Features
*   **Upload CSV**: Easily upload your input file.
*   **Custom Parameters**: Enter weights and impacts.
*   **Email Results**: Get the resultant CSV file directly in your inbox.
*   **Interactive Table**: View the results (Topsis Score and Rank) instantly.

### Running the Web App

Ensure you have `streamlit` installed (`pip install streamlit`).

```bash
streamlit run app.py
```

### Screenshot

![Web Service Interface](image/final.png)

> *Note: Provide your sender Gmail and App Password in the sidebar to enable email functionality.*

---

## 📄 License

This project is licensed under the MIT License.
