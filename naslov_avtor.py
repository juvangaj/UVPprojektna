import requests
from bs4 import BeautifulSoup
import csv



def zajemi_osnovne_podatke():
    stran_url = "https://www.last.fm/tag/hip-hop/tracks"


    skladbe = []
    for page in range(1, 21):  # 20 strani x 50 skladb = 1000 skladb
        print(f"Zbiram podatke strani {page}...")
        url = f"{stran_url}?page={page}" # naredi URL za ta page
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        vrstice = soup.select('tr.chartlist-row')
        
        for vrstica in vrstice:
            title_tag = vrstica.select_one('.chartlist-name a')
            artist_tag = vrstica.select_one('.chartlist-artist a')
            
            if title_tag and artist_tag:
                naslov = title_tag.text.strip()
                izvajalec = artist_tag.text.strip()
                
                skladbe.append({
                    "naslov": naslov,
                    "izvajalec": izvajalec
                })
        
       

    # Shrani v CSV (ločeno s podpičjem)
    with open("hiphop_tracks_scraped.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["naslov", "izvajalec"], delimiter=';')
        writer.writeheader() # zgornja vrstica
        writer.writerows(skladbe) # iz seznama skladbe 



