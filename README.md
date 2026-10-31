# Chemical Industries Scraper

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-early%20stage-orange)

A project to collect data about chemical industries from various sources.

## Status

The repository currently contains only `demo.py`, which shows the intended usage. The `scraper` package (`ChemicalIndustriesScraper`) is not in the repo yet, so the demo will not run until it is added.

## Intended usage

```python
from scraper import ChemicalIndustriesScraper

scraper = ChemicalIndustriesScraper()
for item in scraper.scrape():
    print(item)
```

## Built with

- **Language:** Python 3

## Project structure

```
demo.py     usage demo
README.md
```
