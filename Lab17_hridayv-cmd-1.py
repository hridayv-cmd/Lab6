"""
Program Name: Refactored Hacker News API Script
Author: Hriday Vermani
Purpose: Fetches top stories from the Hacker News API and safely handles 
         articles missing comment counts ('descendants' key) using .get() 
         to prevent KeyError crashes before printing from hn_submissions.py from the textbook.
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

# Loop through the top 30 submissions
for submission_id in submission_ids[:30]:
    # Make a separate API call for each item
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    
    if r.status_code != 200:
        continue
        
    response_dict = r.json()
    
    # Safely get comment count; default to 0 if 'descendants' key is missing
    comments = response_dict.get('descendants', 0)
    # Build dictionary for the article
    submission_dict = {
        'title': response_dict.get('title', 'No Title Available'),
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': comments,
    }
    submission_dicts.append(submission_dict)

# Sort submissions by number of comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Print results to the console
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"URL: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

