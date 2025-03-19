from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Scrape Hammer Museum
def scrape_hammer():
    url = "https://hammer.ucla.edu/exhibitions/on-view"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    exhibitions = []
    for item in soup.select('.exhibition-listing__content'):
        title = item.find('h3').text.strip()
        link = "https://hammer.ucla.edu" + item.find('a')['href']
        exhibitions.append({"museum": "Hammer Museum", "title": title, "url": link})

    return exhibitions

# Scrape LACMA
def scrape_lacma():
    url = "https://www.lacma.org/art/exhibitions/current"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    exhibitions = []
    for item in soup.select('.views-row'):
        title = item.find('h3').text.strip()
        link = "https://www.lacma.org" + item.find('a')['href']
        exhibitions.append({"museum": "LACMA", "title": title, "url": link})

    return exhibitions

# Scrape Getty
def scrape_getty():
    url = "https://www.getty.edu/visit/exhibitions/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    exhibitions = []
    for item in soup.select('.exhibition-card'):
        title = item.find('h2').text.strip()
        link = "https://www.getty.edu" + item.find('a')['href']
        exhibitions.append({"museum": "Getty Museum", "title": title, "url": link})

    return exhibitions

@app.route('/exhibitions', methods=['GET'])
def get_exhibitions():
    data = scrape_hammer() + scrape_lacma() + scrape_getty()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
