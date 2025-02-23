from services.spotify_service import fetch_artist_data, get_artist_popularity
from services.instagram_service import get_instagram_followers

def determine_artist_level(spotify_popularity, spotify_followers, instagram_followers):
    # Check for A level
    if (spotify_popularity >= 40 and 
        instagram_followers >= 20000 and 
        spotify_followers >= 20000):
        return 'A'
    
    # Check for B level
    elif (spotify_popularity >= 25 and 
          instagram_followers >= 2500 and 
          spotify_followers >= 1000):
        return 'B'
    
    # If neither A nor B, then C
    return 'C'

def main():
    artist_name = input("Enter artist name: ")
    
    # Get Spotify data
    artist_data = fetch_artist_data(artist_name)
    if not artist_data:
        print("Artist not found on Spotify")
        return
    
    spotify_popularity = get_artist_popularity(artist_data['id'])
    spotify_followers = artist_data['followers']['total']
    
    # Get Instagram followers
    instagram_username = input("Enter artist's Instagram username: ")
    instagram_followers = get_instagram_followers(instagram_username)
    
    # Print results
    print("\nResults:")
    print(f"Spotify Popularity: {spotify_popularity}")
    print(f"Spotify Followers: {spotify_followers}")
    print(f"Instagram Followers: {instagram_followers}")
    
    # Determine and print level
    level = determine_artist_level(spotify_popularity, spotify_followers, instagram_followers)
    print(f"\n{level} Artist")

if __name__ == "__main__":
    main()