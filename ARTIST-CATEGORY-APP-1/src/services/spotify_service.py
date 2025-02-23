import requests
from config.credentials import SPOTIFY_API_URL, SPOTIFY_API_TOKEN

def fetch_artist_data(artist_name):
    headers = {
        'Authorization': f'Bearer {SPOTIFY_API_TOKEN}'
    }
    response = requests.get(f'{SPOTIFY_API_URL}/search', headers=headers, params={'q': artist_name, 'type': 'artist'})
    
    if response.status_code == 200:
        data = response.json()
        if data['artists']['items']:
            return data['artists']['items'][0]
    return None

def get_artist_popularity(artist_id):
    headers = {
        'Authorization': f'Bearer {SPOTIFY_API_TOKEN}'
    }
    response = requests.get(f'{SPOTIFY_API_URL}/artists/{artist_id}', headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['popularity']
    return 0