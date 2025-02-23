import streamlit as st
import base64
import requests

# Page configuration
st.set_page_config(
    page_title="Artist Category Calculator",
    page_icon="🎵",
    layout="centered"
)

# Spotify API credentials
SPOTIFY_CLIENT_ID = '5f82a48b643046f9ac48cdcb62d62db7'
SPOTIFY_CLIENT_SECRET = '1c18b00531c84a72bf56359a45346cc1'
SPOTIFY_API_URL = 'https://api.spotify.com/v1'

def get_spotify_token():
    auth_string = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    
    result = requests.post(url, headers=headers, data=data)
    json_result = result.json()
    return json_result.get("access_token")

def get_artist_data(artist_name, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        f'{SPOTIFY_API_URL}/search',
        headers=headers,
        params={'q': artist_name, 'type': 'artist'}
    )
    
    if response.status_code == 200:
        data = response.json()
        if data['artists']['items']:
            return data['artists']['items'][0]
    return None

# Main app
st.title("Artist Category Calculator 🎵")
st.markdown("""
This app categorizes artists into A, B, or C levels based on:
- Spotify Popularity (40%+ for A, 25%+ for B)
- Spotify Followers (20K+ for A, 1K+ for B)
- Instagram Followers (20K+ for A, 2.5K+ for B)
""")

# User inputs
artist_name = st.text_input('Enter artist name:', placeholder='e.g., Drake')
instagram_followers = st.number_input('Enter Instagram followers count:', min_value=0, format='%d')

if st.button('Calculate Category'):
    if artist_name:
        try:
            with st.spinner('Fetching artist data...'):
                token = get_spotify_token()
                artist_data = get_artist_data(artist_name, token)
                
                if artist_data:
                    spotify_popularity = artist_data['popularity']
                    spotify_followers = artist_data['followers']['total']
                    
                    # Display results
                    st.success('Artist found!')
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric('Spotify Popularity', f'{spotify_popularity}%')
                    with col2:
                        st.metric('Spotify Followers', f'{spotify_followers:,}')
                    with col3:
                        st.metric('Instagram Followers', f'{instagram_followers:,}')
                    
                    # Calculate category
                    if all([
                        spotify_popularity >= 40,
                        spotify_followers >= 20000,
                        instagram_followers >= 20000
                    ]):
                        category = 'A'
                        color = 'green'
                    elif all([
                        spotify_popularity >= 25,
                        spotify_followers >= 1000,
                        instagram_followers >= 2500
                    ]):
                        category = 'B'
                        color = 'orange'
                    else:
                        category = 'C'
                        color = 'red'
                    
                    st.markdown(f'### Category: <span style="color:{color}">{category}</span>', unsafe_allow_html=True)
                else:
                    st.error('Artist not found on Spotify')
        except Exception as e:
            st.error(f'Error: {str(e)}')
