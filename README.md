Wikipedia Link Scraper (Selenium + Python)

A simple recursive web scraper that extracts Wikipedia article links using Selenium and Python. 

Summary
Input: Wikipedia URL + integer n (1–3)
Task: Scrape 10 unique internal Wikipedia links recursively up to n levels
Tools: Selenium, ChromeDriver, validators, json for output

Features:
✅ Validates Wikipedia URLs
✅ Accepts depth input (1 to 3)
✅ Scrapes 10 unique /wiki/ links from each page
✅ Avoid revisiting already scraped links
✅ Repeats for n cycles
✅ Saves results to output.json

Tech Stack:
Python 3.7+
Selenium (Chrome)
validators (for URL validation)

Installation:

1.Clone or Download the Project
https://github.com/your-username/wiki-scraper-selenium.git

2.Navigate to the folder
cd wiki-scraper-selenium

3.Install dependencies
pip install -r requirements.txt

4.Ensure ChromeDriver is installed
Download from: https://sites.google.com/chromium.org/driver/

5.Make sure it matches your Chrome version 
Add chromedriver to your system PATH


Example:
Enter a valid Wikipedia URL: https://en.wikipedia.org/wiki/Temp
Enter a depth (1 to 3): 1

Sample Output:
Output.json
{
    "total_links_found": 10,
    "unique_links": 10,
    "links": [
        "https://en.wikipedia.org/wiki/Temporary_file",
        "https://en.wikipedia.org/wiki/Temporary_folder",
        "https://en.wikipedia.org/wiki/TEMP_(meteorology)",
        "https://en.wikipedia.org/wiki/Temp_(air_base)",
        "https://en.wikipedia.org/wiki/Temporary_variable",
        "https://en.wikipedia.org/wiki/Weather",
        "https://en.wikipedia.org/wiki/Temp_track",
        "https://en.wikipedia.org/wiki/Temperature",
        "https://en.wikipedia.org/wiki/Tempore",
        "https://en.wikipedia.org/wiki/Temporary_work"
    ]
}