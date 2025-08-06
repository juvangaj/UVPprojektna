from naslov_avtor import zajemi_osnovne_podatke
from ostalo import obogati_podatke

# 1. Najprej dobimo nsalov skladbe in avtorja iz seznama top hip-hop tracks
print("Zbiram naslov skladbe in avtorja...")
zajemi_osnovne_podatke()

# 2. Nato dodamo 
print("Dodajam album, dolžino skladbe in eksplicitnost...")
obogati_podatke()

print("Vse končano.")
