import csv
import requests


def obogati_podatke():
    vhodna_datoteka = "hiphop_tracks_scraped.csv"
    izhodna_datoteka = "hiphop_tracks_obogateno.csv"

    def poisci_na_deezerju(naslov_pesmi, izvajalec):
        poizvedba = f'https://api.deezer.com/search?q=artist:"{izvajalec}" track:"{naslov_pesmi}"'
        try:
            odziv = requests.get(poizvedba)
            podatki = odziv.json()
            if podatki['data']:
                prvi_rezultat = podatki['data'][0] # če je rezultatov več, vzame prvega
                album = prvi_rezultat['album']['title']
                trajanje_v_s = prvi_rezultat['duration']
                eksplicitna_vsebina = prvi_rezultat['explicit_lyrics']
                minute = trajanje_v_s // 60
                sekunde = trajanje_v_s % 60
                trajanje = f"{minute}:{sekunde:02d}"
                oznaka_eksplicitnosti = "eksplicitna" if eksplicitna_vsebina else "ni_eksplicitna"
                return album, trajanje, oznaka_eksplicitnosti
            else:
                return "Ni podatka", "Ni podatka", "ni_eksplicitna"
        except Exception:
            return "Napaka", "Napaka", "ni_eksplicitna"

    # prebere vhodno CSV datoteko z naslovom in izvajalcem
    with open(vhodna_datoteka, "r", encoding="utf-8") as f:
        bralnik = csv.DictReader(f, delimiter=';')
        skladbe = list(bralnik)

    # doda ostale podatke o skladbah
    obogatene_skladbe = []
    for skladba in skladbe:
        naslov = skladba['naslov']
        izvajalec = skladba['izvajalec']
        album, trajanje, oznaka_eksplicitnosti = poisci_na_deezerju(naslov, izvajalec)

        obogatene_skladbe.append({
            'naslov': naslov,
            'izvajalec': izvajalec,
            'album': album,
            'trajanje': trajanje,
            'eksplicitnost': oznaka_eksplicitnosti
        })



    # shrani podatke v novo CSV datoteko
    with open(izhodna_datoteka, "w", newline='', encoding="utf-8") as f:
        pisec = csv.DictWriter(f, fieldnames=['naslov', 'izvajalec', 'album', 'trajanje', 'eksplicitnost'], delimiter=';')
        pisec.writeheader()
        pisec.writerows(obogatene_skladbe)

# pokliče funkcijo
obogati_podatke()



# primer: https://api.deezer.com/search?q=artist:%22Eminem%22%20track:%22Lose%20Yourself%22