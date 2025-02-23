# README.md

# Artist Category App

## Overview
The Artist Category App is a Python application that determines the level of an artist based on their popularity on Spotify and their follower count on Instagram. The app categorizes artists into three levels: A, B, and C, based on specific criteria.

## Features
- Input an artist's name.
- Fetches artist data from Spotify and Instagram.
- Determines the artist's level based on defined criteria.

## Levels Criteria
- **A Artist:**
  - Popularity on Spotify: 40%
  - Instagram: minimum 20K followers
  - Spotify followers: 20K

- **B Artist:**
  - Popularity on Spotify: 25%
  - Instagram: minimum 2.5K followers
  - Spotify followers: 1K

- **C Artist:**
  - Lower than B

## Project Structure
```
ARTIST-CATEGORY-APP
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── spotify_service.py
│   │   └── instagram_service.py
│   ├── models
│   │   ├── __init__.py
│   │   └── artist.py
│   └── config
│       ├── __init__.py
│       └── credentials.py
├── tests
│   ├── __init__.py
│   └── test_artist.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory.
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Update the `src/config/credentials.py` file with your API keys for Spotify and Instagram.
5. Run the application:
   ```
   python src/main.py
   ```

## Usage
- Enter the artist's name when prompted.
- The application will display the artist's Spotify popularity, Spotify followers, Instagram followers, and their corresponding level (A/B/C).

## License
This project is licensed under the MIT License.