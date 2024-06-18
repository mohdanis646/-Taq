import requests
import os

# URLs of high-quality images for the website
image_urls = {
    "hero-background.jpg": "https://images.unsplash.com/photo-1581091870623-9e8e1d7df9d4",
    "manpower.jpg": "https://images.pexels.com/photos/585419/pexels-photo-585419.jpeg",
    "heavy-equipment.jpg": "https://images.pexels.com/photos/1078883/pexels-photo-1078883.jpeg",
    "sandblasting.jpg": "https://images.unsplash.com/photo-1595268573667-28d7e9e17e1a",
    "coating.jpg": "https://images.unsplash.com/photo-1599599810196-d5f6654e89b7",
    "road-line-marking.jpg": "https://images.pexels.com/photos/3993797/pexels-photo-3993797.jpeg",
    "fire-proofing.jpg": "https://images.unsplash.com/photo-1595266113641-1eeae0c26e5a",
    "pwas-installation.jpg": "https://images.pexels.com/photos/3280134/pexels-photo-3280134.jpeg",
}

# Ensure the target directory exists
os.makedirs("data", exist_ok=True)

# Download images and save to the local directory
for filename, url in image_urls.items():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        with open(f"data/{filename}", 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename} from {url}: {e}")

print(list(image_urls.keys()))
