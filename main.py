"""
This script interacts with the Crossmint Megaverse API to construct a megaverse map by placing various celestial bodies
(POLYanets, SOLOons, and COMETHs) on a 2D grid. It reads configuration data from a JSON file to get the candidate ID,
fetches the goal map from the API, and updates the map accordingly.

The script defines the following main components:
1. CelestialBody class: Contains constants for different types of celestial bodies.
2. load_config function: Loads configuration data from 'config.json'.
3. add_polyanet, add_soloon, add_cometh functions: Send requests to add respective celestial bodies to the map.
4. handle_response function: Handles the API response, including retry logic for rate limit errors.
5. update_map function: Determines the type of celestial body to add based on the goal map cell value.
6. main function: Coordinates the overall process, including fetching the goal map and updating the map.

The script ensures resilience by handling various potential errors, such as missing configuration data, JSON decoding errors,
and server rate limiting.
"""


import logging
import requests
import json
import sys
import time

BASE_API_URL = 'https://challenge.crossmint.io/api'

class CelestialBody:
    POLYANET = 'POLYANET'
    RED_SOLOON = 'RED_SOLOON'
    BLUE_SOLOON = 'BLUE_SOLOON'
    PURPLE_SOLOON = 'PURPLE_SOLOON'
    WHITE_SOLOON = 'WHITE_SOLOON'
    UP_COMETH = 'UP_COMETH'
    RIGHT_COMETH = 'RIGHT_COMETH'
    DOWN_COMETH = 'DOWN_COMETH'
    LEFT_COMETH = 'LEFT_COMETH'

def load_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            if 'CANDIDATE_ID' not in config or not config['CANDIDATE_ID']:
                raise ValueError("CANDIDATE_ID is not set in the config file.")
            return config
    except FileNotFoundError:
        logging.error("The configuration file config.json does not exist.")
        sys.exit(1)
    except json.JSONDecodeError:
        logging.error("Error decoding config.json. Ensure it is valid JSON.")
        sys.exit(1)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        sys.exit(1)

def add_polyanet(i, j):
    payload = {'row': i, 'column': j, 'candidateId': candidateId}
    response = requests.post(f'{BASE_API_URL}/polyanets', json=payload)
    handle_response(response, 'polyanet', i, j)

def add_soloon(i, j, color):
    payload = {'row': i, 'column': j, 'candidateId': candidateId, 'color': color}
    response = requests.post(f'{BASE_API_URL}/soloons', json=payload)
    handle_response(response, f'{color} soloon', i, j)

def add_cometh(i, j, direction):
    payload = {'row': i, 'column': j, 'candidateId': candidateId, 'direction': direction}
    response = requests.post(f'{BASE_API_URL}/comeths', json=payload)
    handle_response(response, f'{direction} cometh', i, j)

def handle_response(response, entity_type, i, j):
    if response.status_code == 200:
        logging.info('Successfully added %s at row: %s, column: %s', entity_type, i, j)
    elif response.status_code == 429:
        logging.error('Rate limit exceeded for %s at row: %s, column: %s - Retrying after a delay', entity_type, i, j)
        time.sleep(2)
        handle_response(response, entity_type, i, j)
    else:
        logging.error('Failed to add %s at row: %s, column: %s - Status Code: %s', entity_type, i, j, response.status_code)

def update_map(i, j, cell):
    if cell == CelestialBody.POLYANET:
        add_polyanet(i, j)
    elif 'SOLOON' in cell:
        color = cell.split('_')[0].lower()
        add_soloon(i, j, color)
    elif 'COMETH' in cell:
        direction = cell.split('_')[0].lower()
        add_cometh(i, j, direction)

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    config = load_config()
    global candidateId
    candidateId = config['CANDIDATE_ID']

    # Fetch the goal map for Phase 2
    resp = requests.get(f'{BASE_API_URL}/map/{candidateId}/goal')
    if resp.status_code == 200:
        goal = resp.json().get('goal')
        if goal:
            for i, row in enumerate(goal):
                for j, cell in enumerate(row):
                    update_map(i, j, cell)
                    time.sleep(0.2)  # Add a delay to handle rate limits
        else:
            logging.error("Goal map is empty or not available.")
    else:
        logging.error("Failed to fetch goal map - Status Code: %s", resp.status_code)

if __name__ == '__main__':
    main()

