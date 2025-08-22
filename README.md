# Projektna naloga: Analiza hiphop skladb s spletno analizo

## Opis projekta

Že od nekdja sem velik oboževalec hip-hop glasbe, zato sem se odločil, da raziščem, kateri izvajalci, albumi in pesmi so v tem žanru najbolj popularni med poslušalci. V projektni nalogi sem zbral top 1000 najboljših **hiphop skladb** s spletne strani [Last.fm](https://www.last.fm/tag/hip-hop/tracks).
Za pridobivanje podatkov sem uporabil knjižnici **`requests`** in **`BeautifulSoup`** v jeziku Python.
Ko sem pidobil naslove skladb in izvajalce sem nato s pomočjo strani [deezer.com] dobil še podatke o albumu, dolžini pesmi in eksplicitnosti besedila.

Cilj je prikazati praktično uporabo spletnega strganja (scrapinga), obdelave podatkov in priprave CSV datoteke za nadaljno analizo. Prav tako sem izdelal razne grafe in tabele ter analiziral podatke s pomočjo Jupyter notebooka.

---

## Zajeti podatki

Za vsako skladbo so zbrani naslednji podatki:
- **Naslov skladbe** (`title`)
- **Izvajalec** (`artist`)
- **Album** (`album`)
- **Dolžina** (`length`)
- **Eksplicitnost** (`explicit`)

Podatki so shranjeni v datoteki `hiphop_tracks_obogateno.csv`, ločeni s **podpičjem (`;`)**.

---


