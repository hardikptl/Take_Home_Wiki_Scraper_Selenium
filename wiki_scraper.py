import re
import time
import validators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://en.wikipedia.org"
visited_links = set()
final_links = []

def get_driver():
    driver = webdriver.Chrome()
    return driver

def is_valid_wiki_url(url):
    """
    Checks if the URL is a valid Wikipedia article link using regex.
    Excludes URLs with namespaces like ':', fragments like '#',
    and common non-content pages like Main_Page.
    """
    pattern = r"^https://en\.wikipedia\.org/wiki/(?!Main_Page)(?!.*[:#]).+$"
    return re.match(pattern, url) is not None

def scrape_links(driver, url, max_links=10):
    print(f"Scraping: {url}")
    driver.get(url)
    time.sleep(1)
    anchors = driver.find_elements(By.TAG_NAME, "a")
    links = []

    for anchor in anchors:
        href = anchor.get_attribute("href")
        if href and is_valid_wiki_url(href) and href not in visited_links:
            links.append(href)
            visited_links.add(href)
        if len(links) >= max_links:
            break     
    return links


def crawl(start_url, depth):
    if not validators.url(start_url) or not is_valid_wiki_url(start_url):
        raise ValueError("Invalid Wikipedia URL.")

    driver = get_driver()
    try:
        queue = [start_url]
        visited_links.add(start_url)

        for cycle in range(depth):
            print(f"\nCycle {cycle + 1} of {depth}")
            new_queue = []
            for url in queue:
                found = scrape_links(driver, url)
                final_links.extend(found)
                new_queue.extend(found)
            queue = new_queue
    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        start_url = input("Enter a valid Wikipedia URL: ").strip()
        depth = int(input("Enter a depth between 1 to 3: ").strip())
        if depth not in [1, 2, 3]:
            raise ValueError("Depth must be 1, 2, or 3.")

        crawl(start_url, depth)
    except Exception as e:
        print(f"Error: {e}")