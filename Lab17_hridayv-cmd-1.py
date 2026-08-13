"""
Program Name: Refactored Hacker News API Script
Author: Hriday Vermani
Purpose: Fetches top stories from the Hacker News API and safely handles 
         articles missing comment counts ('descendants' key) using .get() 
         to prevent KeyError crashes before printing.
Starter Code Source: Python Crash Course (Chapter 17)
Date: August 13, 2026
"""

from operator import itemgetter
import requests

# Make an API call to get top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []