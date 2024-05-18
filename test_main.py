# test_main.py
import json
import unittest
from unittest.mock import patch, MagicMock
from main import add_polyanet, add_soloon, add_cometh, update_map

# Function to retrieve the candidate ID from the config.json file
def get_candidate_id():
    with open('config.json') as f:
        config = json.load(f)
    return config['CANDIDATE_ID']

class TestMegaverse(unittest.TestCase):

    @patch('main.requests.post')
    def test_add_polyanet(self, mock_post):
        candidateId = get_candidate_id()
        mock_post.return_value = MagicMock(status_code=200)
        payload = {'row': 2, 'column': 2, 'candidateId': candidateId}

        with patch.dict('main.__dict__', {'candidateId': candidateId}):
            add_polyanet(2, 2)
        
        mock_post.assert_called_with('https://challenge.crossmint.io/api/polyanets', json=payload)

    @patch('main.requests.post')
    def test_add_soloon(self, mock_post):
        candidateId = get_candidate_id()
        mock_post.return_value = MagicMock(status_code=200)
        payload = {'row': 3, 'column': 3, 'candidateId': candidateId, 'color': 'red'}

        with patch.dict('main.__dict__', {'candidateId': candidateId}):
            add_soloon(3, 3, 'red')
        
        mock_post.assert_called_with('https://challenge.crossmint.io/api/soloons', json=payload)

    @patch('main.requests.post')
    def test_add_cometh(self, mock_post):
        candidateId = get_candidate_id()
        mock_post.return_value = MagicMock(status_code=200)
        payload = {'row': 4, 'column': 4, 'candidateId': candidateId, 'direction': 'up'}

        with patch.dict('main.__dict__', {'candidateId': candidateId}):
            add_cometh(4, 4, 'up')
        
        mock_post.assert_called_with('https://challenge.crossmint.io/api/comeths', json=payload)

    @patch('main.requests.post')
    def test_update_map(self, mock_post):
        candidateId = get_candidate_id()
        mock_post.return_value = MagicMock(status_code=200)
        payload_soloon = {'row': 6, 'column': 6, 'candidateId': candidateId, 'color': 'red'}
        payload_cometh = {'row': 7, 'column': 7, 'candidateId': candidateId, 'direction': 'up'}

        with patch.dict('main.__dict__', {'candidateId': candidateId}):
            update_map(6, 6, 'RED_SOLOON')
        mock_post.assert_called_with('https://challenge.crossmint.io/api/soloons', json=payload_soloon)

        with patch.dict('main.__dict__', {'candidateId': candidateId}):
            update_map(7, 7, 'UP_COMETH')
        mock_post.assert_called_with('https://challenge.crossmint.io/api/comeths', json=payload_cometh)

if __name__ == '__main__':
    unittest.main()
