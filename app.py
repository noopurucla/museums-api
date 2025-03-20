from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Allow all origins

# Scrape Hammer Museum exhibitions
def scrape_hammer():
    url = "https://hammer.ucla.edu/exhibitions/on-view"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    exhibitions = []
    for item in soup.select('.views-row'):
        title = item.find('h3')
        link = item.find('a')['href'] if item.find('a') else None
        if title:
            exhibitions.append({
                "museum": "Hammer Museum",
                "title": title.text.strip(),
                "url": f"https://hammer.ucla.edu{link}" if link else "https://hammer.ucla.edu/exhibitions/on-view"
            })
    return exhibitions

# Scrape LACMA exhibitions
def scrape_lacma():
    url = "https://www.lacma.org/art/exhibitions/current"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    exhibitions = []
    for item in soup.select('.views-row'):
        title = item.find('h3')
        link = item.find('a')['href'] if item.find('a') else None
        if title:
            exhibitions.append({
                "museum": "LACMA",
                "title": title.text.strip(),
                "url": f"https://www.lacma.org{link}" if link else "https://www.lacma.org/art/exhibitions/current"
            })
    return exhibitions

# Scrape Getty Museum exhibitions
def scrape_getty():
    url = "https://www.getty.edu/visit/exhibitions/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    exhibitions = []
    for item in soup.select('.exhibition-card'):
        title = item.find('h2')
        link = item.find('a')['href'] if item.find('a') else None
        if title:
            exhibitions.append({
                "museum": "Getty Museum",
                "title": title.text.strip(),
                "url": f"https://www.getty.edu{link}" if link else "https://www.getty.edu/visit/exhibitions/"
            })
    return exhibitions

@app.route('/')
def home():
    return "LA Museums API is running!"

@app.route('/exhibitions', methods=['GET'])
def get_exhibitions():
    exhibitions = scrape_hammer() + scrape_lacma() + scrape_getty()
    return jsonify(exhibitions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
