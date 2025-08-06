# Projektna naloga: Analiza hiphop skladb s spletno analizo

## Opis projekta

Že od nekdja sem velik oboževalec hip-hop glasbe, zato sem se odločil, da raziščem kateri izvajalci, albumi in pesmi so v tem žanru najbolj popularni med poslušalci.V projektni nalogi sem zbral top 1000 najboljših **hiphop skladb** s spletne strani [Last.fm](https://www.last.fm/tag/hip-hop/tracks).
Za pridobivanje podatkov sem uporabil knjižnici **`requests`** in **`BeautifulSoup`** v jeziku Python.

Cilj je prikazati praktično uporabo spletnega strganja(scrapinga), obdelave podatkov in priprave CSV datoteke za nadaljnjo analizo. Prv tako izdelava raznih tabel in grafov.

---

## Zajeti podatki

Za vsako skladbo so zbrani naslednji podatki:
- **Naslov skladbe** (`title`)
- **Izvajalec** (`artist`)
- **Album** (`album`)
- **Dolžina** (`length`)
- **Eksplicitnost** (`explicit`)

Podatki so shranjeni v datoteki `hiphop_tracks_enriched.csv`, ločeni s **podpičjem (`;`)**.

---


