import requests

def get_instagram_followers(artist_name, access_token):
    url = f"https://graph.instagram.com/v1/users/self?fields=followers_count&access_token={access_token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('followers_count', 0)
    else:
        print(f"Error fetching data from Instagram: {response.status_code}")
        return 0