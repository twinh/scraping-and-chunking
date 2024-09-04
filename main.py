"""
# Scraping and Chunking
"""

from bs4 import BeautifulSoup
import requests
import google.generativeai as genai
import json
import typing_extensions as typing
import os


class Chunk(typing.TypedDict):
    # Define the Chunk type to response from the LLM
    text: str
    length: int


def main():
    # Initialize Google API
    if "GOOGLE_API_KEY" not in os.environ:
        raise ValueError("GOOGLE_API_KEY environment variable is not set.")
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

    base_url = "https://www.notion.so"
    all_chunks = []

    # Scrape the Notion help center
    urls = scrape_notion_help_center(base_url + "/help")

    # Process each article
    for article_url in urls:
        url = base_url + article_url

        output_file = 'output' + article_url.replace('/', '-') + '.txt'
        if os.path.isfile(output_file):
            print(f"Skipping {url} because {output_file} already exists")
            continue

        print(f"Extracting {url}")
        content = extract_core_content(url)

        print(f"Chunking content, {len(content)} characters")
        chunks = chunk_content(content)

        print(f"Writing file")
        write_chunks_to_file(url, chunks, output_file)

        all_chunks.extend(chunks)

    #  Print the first 3 chunks
    for i, chunk in enumerate(all_chunks[:3]):
        print(f"Chunk {i + 1}: {len(chunk.get('text'))}\n{chunk.get('text')}\n\n")


def scrape_notion_help_center(base_url):
    response = requests.get(base_url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for link in soup.find_all('a', href=True):
        url = link['href']
        # Ignore Notion Academy
        if '/help' in url and '/help/notion-academy' not in url and '/help/guide' not in url:
            articles.append(url)
    return set(articles)


def extract_core_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the article from {url}")

    soup = BeautifulSoup(response.text, "html.parser")

    if '/help/category' in url:
        target = soup.find("main")
        # Remove sidebar from category page
        target.find_all('aside')[-1].extract()
    else:
        target = soup.find("article")

    return target.prettify()


def chunk_content(content):
    model = genai.GenerativeModel("gemini-1.5-pro",
                                  generation_config={"response_mime_type": "application/json",
                                                     "response_schema": list[Chunk]})

    # Using an LLM to help with formatting and prettifying the information
    response = model.generate_content(f"""
Strip breadcrumbs, toc and help center contact module from the HTML.
Convert the HTML into text, dont contains any HTML tag, keep the line break.
Split the text into smaller chunks. Your chunks should be roughly 750 characters but could be more if it’s necessary to keep related context together.
Make sure to keep headers and paragraphs together and don’t break up bulleted lists mid-list.
Merge multiple chunks if they are too short.
The HTML is:

{content}
""")

    return json.loads(response.text)


def write_chunks_to_file(url, chunks, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(url + "\n\n")
        for i, chunk in enumerate(chunks):
            file.write(f"Chunk {i + 1}: {len(chunk.get('text'))}\n{chunk.get('text')}\n\n")


if __name__ == '__main__':
    main()
