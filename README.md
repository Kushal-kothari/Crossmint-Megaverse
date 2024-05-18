# Crossmint-Megaverse

## Overview

This project automates the creation of a megaverse using Python and API interactions. It adheres to clean code principles and robustness. The main goal is to programmatically build the megaverse by interacting with the Crossmint challenge API, adding various celestial entities such as Polyanets, Saloons, and Comeths.

## Features

- **Automated API Interactions**: Uses Python scripts to interact with the Crossmint API.
- **Celestial Entities**: Adds different celestial bodies like Polyanets, Saloons (of various colors), and Comeths (facing different directions) to the megaverse.
- **Rate Limiting Handling**: Implements mechanisms to handle API rate limits and retries.
- **Logging**: Provides detailed logging for tracking the process and any issues that arise.

## Files

- **config.json**: Configuration file containing necessary IDs and other settings.
- **main.py**: Main script to fetch the goal map and update the megaverse by adding celestial entities.
- **test_main.py**: Contains unit tests to validate the functionality of the main script.
- **__pycache__/**: Cache directory for compiled Python files.

## Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Kushal-kothari/Crossmint-Megaverse.git
   cd Crossmint-Megaverse

2. **Create and activate a virtual environment (optional but recommended):**:
   ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**:
   ```sh
     pip install -r requirements.txt

## Update `config.json`

Ensure the `CANDIDATE_ID` is set correctly in the `config.json` file.

## Usage

  To run the main script and start the process of creating the megaverse:
  
    ```sh
    python main.py

## Testing
  To run the unit tests

  ```sh
  python -m unittest test_main.py
  ```

## Contributing
  Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
