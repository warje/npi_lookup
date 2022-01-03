# npi_lookup

## Assumptions
- All npi code + address combos are unique per file
- All NPI registry responses with addresses will have a postal code

## Installation
Requirements:
- Python (3.10.1)
- `openpyxl` compatability

To install run the following commands:
```
git clone https://github.com/warje/npi_lookup.git
cd ./npi_lookup
pip install .
```

This will clone the repository, change to the directory, and install the python package. When installed the `lookup_sync` command will be installed onto your path.

## Execution
Run the following command to execute the script:
`./lookup_sync`

### Example output
```
> npi_lookup git:(main) ✗ lookup_sync
Output files:
        odd - odd.csv
        even - even.csv
Records written:
        odd - 127
        even - 131
total execution time: 33.89115524291992 seconds
>
```

### Async (Experimentation)
Run `./lookup_async`
