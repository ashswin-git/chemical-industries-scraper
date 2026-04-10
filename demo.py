# Demo Script for Chemical Industries Scraper

"""
This is a demo script that shows how to use the Chemical Industries Scraper.

Usage: python demo.py
"""

# Import the necessary classes or functions from the scraper
from scraper import ChemicalIndustriesScraper

# Create an instance of the scraper
scraper = ChemicalIndustriesScraper()

# Run the scraper and store the results
results = scraper.scrape()

# Print the results
print("Sample Output:")
for item in results:
    print(item)