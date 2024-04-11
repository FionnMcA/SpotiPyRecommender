# SpotiPyRecommender

SpotiPyRecommender is a simple Python script that creates a Spotify playlist full of recommended songs based on a genre provided by the user. It uses the [Spotipy library](https://spotipy.readthedocs.io/en/2.22.1/) to interact with the Spotify Web API.

## Prerequisites

- **Python 3.6 or higher**.
- **Python libraries**: `spotipy`, `python-dotenv`. These can be installed with pip:
  
  ```bash
  pip install spotipy python-dotenv
  ```
  - A Spotify account (either free or premium).

- An application registered on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) to obtain your `CLIENT_ID` and `CLIENT_SECRET`.

## Setup
1. Clone this repository.
```bash
https://github.com/FionnMcA/SpotiPyRecommender.git
```
2. Navigate to the your newly created ```SpotiPyRecommender``` Repository
3. Navigate to the `.env` file and replace the Placeholders ```YOUR_SPOTIFY_CLIENT_ID``` with your own spotify client id and ```YOUR_SPOTIFY_CLIENT_SECRET``` with your spotify client secret

## How to Run

After you have set up your environment, you can run the SpotiPyRecommender application with these steps:

1. Open your terminal or command prompt.

2. Ensure you are in the root directory of the cloned `SpotiPyRecommender` repository.

3. If you are using a virtual environment, activate it with the following command:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```cmd
     .\venv\Scripts\activate
     ```

4. Run the script by executing:

   ```bash
   python SpotiPyRecommender.py
   ```


