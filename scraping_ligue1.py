import requests
from bs4 import BeautifulSoup
import csv
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

url = 'https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2024-2025'

response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', {'class': 'wikitable'})
target_table = None
for table in tables:
    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    if 'Club' in headers and 'Stade' in headers:
        target_table = table
        break

if not target_table:
    print("Le tableau des clubs n'a pas été trouvé.")
    exit()

geolocator = Nominatim(user_agent="ligue1_mapper")

def geocode_with_retry(query):
    try:
        location = geolocator.geocode(f"{query}, France")
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        time.sleep(1)
        return geocode_with_retry(query)

clubs_data = []
for row in target_table.find_all('tr')[1:]:
    cells = row.find_all(['td', 'th'])
    if len(cells) < 7:
        continue

    club = cells[0].get_text(strip=True)
    derniere_montee = cells[1].get_text(strip=True)
    classement = cells[2].get_text(strip=True)
    entraineur = cells[3].get_text(strip=True)
    stade = cells[5].get_text(strip=True)
    capacite = cells[6].get_text(strip=True)
    saisons_L1 = cells[7].get_text(strip=True)

    lat, lon = geocode_with_retry(stade)
    time.sleep(1) 

    clubs_data.append({
        'Club': club,
        'Dernière montée': derniere_montee,
        'Classement (dernier disponible)': classement,
        'Entraîneur': entraineur,
        'Stade': stade,
        'Capacité': capacite,
        'Nombre de saisons en L1': saisons_L1,
        'Latitude': lat,
        'Longitude': lon
    })

with open('clubs_ligue1_2024_2025.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'Club', 'Dernière montée', 'Classement (dernier disponible)', 'Entraîneur',
        'Stade', 'Capacité', 'Nombre de saisons en L1', 'Latitude', 'Longitude'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for club in clubs_data:
        writer.writerow(club)

print("✅ Données enregistreeee")
