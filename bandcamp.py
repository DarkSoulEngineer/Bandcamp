from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import csv

# Configuration
SONGS_LIMIT = 2  # Limit to process albums per artist
TIME_TO_LISTEN = 5  # Time to listen to each song in seconds
ARTISTS_FILE = 'artists.txt'
CSV_FILE = 'albums_data.csv'

# Initialize CSV with headers if not already present
def initialize_csv(file_name):
    try:
        with open(file_name, 'x', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Artist', 'Track Title', 'Track Link'])
            writer.writeheader()
    except FileExistsError:
        # File already exists, do nothing
        pass

# Append data to CSV
def append_to_csv(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Artist', 'Track Title', 'Track Link'])
        writer.writerow(data)

# Load artist names
def load_artists(file_name):
    with open(file_name, 'r') as f:
        return [artist.strip() for artist in f.read().split(',')]

# Scrape albums
def scrape_albums(artist_name, driver, wait):
    albums = []
    driver.get(f"https://bandcamp.com/search?q={artist_name}&item_type=")
    try:
        artist_albums = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#pgBd > div.search > div.leftcol > div > ul > li'))
        )
        for artist_album in artist_albums[:SONGS_LIMIT]:
            try:
                album_art = artist_album.find_element(By.CLASS_NAME, 'artcont')
                album_art.click()
                
                # Play button
                try:
                    play_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'playbutton')))
                    play_button.click()
                except TimeoutException:
                    print(f"No play button for {artist_name}. Skipping album.")
                
                # Track details
                track_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'trackTitle'))).text
                track_link = driver.current_url
                
                album_data = {'Artist': artist_name, 'Track Title': track_title, 'Track Link': track_link}
                append_to_csv(CSV_FILE, album_data)  # Save after each song
                albums.append(album_data)
                
                print(f"Processed: {album_data}")
                
                time.sleep(TIME_TO_LISTEN)  # Wait for time to listen to each song
                driver.back()
            except Exception as e:
                print(f"Error processing album for {artist_name}: {e}")
                driver.back()
    except TimeoutException:
        print(f"No albums found for {artist_name}.")
    except Exception as e:
        print(f"Error searching for {artist_name}: {e}")
    
    return albums

# Main execution
def main():
    initialize_csv(CSV_FILE)
    artists = load_artists(ARTISTS_FILE)
    
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, TIME_TO_LISTEN)  # 10-second timeout
    
    try:
        for artist in artists:
            print(f"Processing artist: {artist}")
            scrape_albums(artist, driver, wait)
    except Exception as e:
        print(f"Critical error during execution: {e}")
    finally:
        driver.quit()
        print("Driver closed. Process complete.")

if __name__ == "__main__":
    main()
