import requests
from bs4 import BeautifulSoup
import time


def fetch_html(url):
    """Fetch the HTML content of a given URL."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch {url}, Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching {url}: {e}")
        return None


def save_html(content, filename):
    """Save the HTML content to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def extract_article_urls_from_html(content):
    """Extract article URLs from the HTML content."""
    soup = BeautifulSoup(content, 'html.parser')
    article_urls = set()  # Use a set to avoid duplicates
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith("https://www.moneycontrol.com/news/") and href not in article_urls:
            article_urls.add(href)
    return article_urls


def fetch_article_url():
    urls = [
        "https://www.moneycontrol.com/news/business/",
        "https://www.moneycontrol.com/news/business/economy/",
        "https://www.moneycontrol.com/news/business/mutual-funds/",
        "https://www.moneycontrol.com/news/business/personal-finance/",
        "https://www.moneycontrol.com/news/business/ipo/",
        "https://www.moneycontrol.com/news/business/startups/",
        "https://www.moneycontrol.com/news/business/markets/",
        "https://www.moneycontrol.com/news/business/stocks/",
        "https://www.moneycontrol.com/news/business/commodity/",
        "https://www.moneycontrol.com/news/business/companies"
    ]
    # # For testing
    # return [
    #     "https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html",
    #     "https://www.moneycontrol.com/news/business/markets/wall-street-rises-as-tesla-soars-on-ai-optimism-11351111.html",
    #
    # ]

    """Main function to fetch, save, and extract article URLs from a list of URLs."""
    all_article_urls = set()
    for url in urls:
        print(f"Processing {url}")
        html_content = fetch_html(url)
        if html_content:
            # # Optional: Save HTML to file (comment out if not needed)
            # filename = url.split('/')[-1] + ".html"
            # save_html(html_content, filename)

            # Extract article URLs
            article_urls = extract_article_urls_from_html(html_content)
            all_article_urls.update(article_urls)

            # Be respectful to the server; sleep between requests
            time.sleep(1)
    filtered_urls = []
    for url in all_article_urls:
        if ".html" in url:
            filtered_urls.append(url)
    return filtered_urls
