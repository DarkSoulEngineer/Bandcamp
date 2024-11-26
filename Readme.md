# Bandcamp Album Scraper

This Python script scrapes track titles and their links from Bandcamp for a given list of artists. Using Selenium, the script navigates Bandcamp's search results, clicks on albums, and extracts relevant track details. The collected data is saved in both CSV and Excel formats for easy access and analysis.

---

## Table of Contents
- [Introduction](#bandcamp-album-scraper) 
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Important Notes](#important-notes)
- [Customizable Settings](#customizable-settings)

## Features

- Scrapes track titles and their links from Bandcamp albums.
- Saves output in both **CSV** and **Excel** formats.
- Customizable list of artists via an `artists.txt` input file.
- Adjustable playback duration to simulate listening behavior.

---

## Requirements

- **Python 3.x**
- **Google Chrome** (latest version recommended)
- **ChromeDriver** (matching your Chrome version)
- Required Python libraries:
  - `selenium`
---

## Installation

1. Clone this repository or download the script:
```bash
   git clone https://github.com/DarkSoulEngineer/Pybandcam.git
   cd Pybandcam
```
2. Install the necessary Python packages:
```
    pip install selenium
```

# Usage

Prepare Input File
Update the artists.txt file with a comma-separated list of artist names. For example:
- `Radiohead`, `Coldplay`, `The Beatles`

Run the Script:
```
    python bandcam.py
```

# Output

A CSV file named albums_data.csv will be generated with the scraped data.
An Excel file (albums_data.xlsx) is also created for additional formatting and compatibility.

# Important Notes

- Wait for Playback Completion
- The script simulates song playback for a defined duration. To ensure all data is saved properly in the Excel file, allow the script to finish processing all
songs before exiting.

# Customizable Settings:
You can modify these parameters in the script:
    - SONGS_LIMIT: Number of albums to process per artist.
    - TIME_TO_LISTEN: Time to "listen" to each song in seconds.

