from flask import Flask, jsonify, request
import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import logging
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/collect', methods=['POST'])
def collectData():
    # logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('Starting the web scraping process.')

    global response
    url = (request.get_json())["url"]

    # throw an exception incase the url not found
    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find('script', {'id': 'tawsiyat-metadata'})
        json_data = data.string.strip()
        data = json.loads(json_data)  # Parse the JSON data

        # Get the postid
        post_id = data.get('postid')
        return {"data": post_id}

    # exception incase the url is wrong or any http exceptions
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), response.status_code
    except requests.exceptions.ConnectionError as conn_err:
        return jsonify({'error': f'Connection error occurred: {conn_err}'}), 500
    except requests.exceptions.Timeout as timeout_err:
        return jsonify({'error': f'Timeout error occurred: {timeout_err}'}), 500
    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'Invalid URL or request error occurred: {req_err}'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
