"""
Program Name: Refactored Hacker News API Script
Author: Hriday Vermani
Purpose: Fetches top stories from the Hacker News API and safely handles 
         articles missing comment counts ('descendants' key) using .get() 
         to prevent KeyError crashes before printing.
Starter Code Source: Python Crash Course (Chapter 17)
Date: August 13, 2026
"""

