# Hot-Billboard-Tub-TimeMachine

Hot Billboard Tub TimeMachine is a Python script that allows you to travel back in time to a specific year and create a private Spotify playlist containing the top tracks from that year's Billboard Hot 100 chart. The script uses web scraping to fetch the Billboard Hot 100 chart data for the specified year and then uses the Spotify API to search for and add the corresponding tracks to a new playlist.

## Getting Started

To use the Hot Billboard Tub TimeMachine, follow these steps:

### 1. Clone the repository to your local machine:
```
git clone https://github.com/your-username/Hot-Billboard-Tub-TimeMachine.git
cd Hot-Billboard-Tub-TimeMachine
```
### 2. Install the required Python packages using pip:
```
pip install -r requirements.txt
```
### 3. Replace the placeholder values in the script with your own Spotify API credentials:

**CLIENT_ID**: Your Spotify client ID

**CLIENT_SECRET**: Your Spotify client secret

**URI**: The redirect URI for your Spotify app (e.g., "http://example.com")

### 4. Run the script:
```
python hot_billboard_tub.py
```
### 5. The script will prompt you to enter a year in the format "YYYY-MM-DD". It will then fetch the Billboard Hot 100 chart data for that year, search for the corresponding tracks on Spotify, and create a private playlist with the retrieved tracks.

## Dependencies

The Hot Billboard Tub TimeMachine project relies on the following Python packages:

1. **beautifulsoup4**: Used for web scraping Billboard Hot 100 chart data from the website.

2. **requests**: Used to make HTTP requests to fetch web page content.

3. **spotipy**: A Python library for the Spotify Web API. It is used to search for tracks and create playlists on Spotify.

Make sure you have these packages installed before running the script.

## Notes

1. The script uses web scraping to extract data from the Billboard website. Please use this script responsibly and respect the website's terms of use.

2. The Spotify API credentials (client ID and client secret) are sensitive information. Keep them secure and do not share them publicly.

3. The script uses the Spotify OAuth authorization flow to access your Spotify account. You'll need to set up a Spotify Developer account and create an app to obtain the required credentials.
