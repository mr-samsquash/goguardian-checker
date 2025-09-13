# URL Categorizer (GoGuardian API)

This is a simple Python CLI tool that queries the GoGuardian API to check which categories a given URL belongs to.  
It uses a mapping of category IDs to human-readable names.

## Requirements

- Python 3.7+
- `requests` library

Install dependencies with:

```bash
pip install requests
````

## Usage

Run the script with a domain as an argument:

```bash
python categorizer.py google.com
```

Example output:

```
['Search Engines']
```

If there’s an error (e.g., network issue, invalid domain), it will return an error dictionary:

```
{'error': '...'}
```

## Files

* `goguardian.py` — main script.

## Notes

* The script relies on an API key (`AUTH_KEY`) defined in the file. Replace it with your own if necessary.
* Category IDs are translated to human-readable names using the `category_map` dictionary. Any unknown IDs will be returned as-is.
