# pckstat Command Line Tool

This is a command line tool that allows users to query statistics of packages obtained from a Debian mirror. The program downloads the compressed "Contents" file associated with a given architecture, parses the file, and outputs the statistics of the top 10 packages that have the most files associated with them.

## Installation

To install the `pckstat` command line tool, follow these steps:

1. Download the repository.

2. Install the package using pip:

```bash
cd <repo path>
pip install .
```

## Usage
```bash
pckstat <architecture>
```

### example
```bash
pckstat amd64
```
