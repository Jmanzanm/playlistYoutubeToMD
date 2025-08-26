# ✅ YouTube Playlist to Markdown

This Python script allows you to convert any public YouTube playlist into a Markdown checklist. Each item in the list includes a cleaned-up video title and a clickable link to the video.

## 📌 Features

- Accepts a full YouTube playlist URL.
- Uses the YouTube Data API (v3) to fetch video details.
- Cleans video titles by removing playlist name and numbering.
- Generates a `.md` file named after the playlist.
- Each video is listed with a checkbox and a clickable link.

## 🚀 Requirements

- Python 3.7+
- YouTube Data API key
- `requests` library

Install dependencies:

```bash
pip install requests
```
## 🐍 Setting Up the Python Environment
To ensure consistent dependencies and avoid conflicts, it's recommended to use a virtual environment.

### Linux/Mac

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate

```

### Windows(CMD)

```cmd
:: Create a virtual environment
python -m venv .venv

:: Activate the environment
.venv\Scripts\activate

```

## 🔑 Setup
1. Get a YouTube Data API key from Google Cloud Console.
2. Set your API key as an environment variable:

```bash
export YOUTUBE_API_KEY=your_api_key_here  # Linux/macOS
```

```cmd
set YOUTUBE_API_KEY=your_api_key_here     # Windows
```
## 🧑‍💻 Usage

 Run the script and enter the playlist URL when prompted:

```bash
python playListYoutubeToMarkdown.py
```




