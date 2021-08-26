import random
import string

haslo = ""
male_znaki = string.ascii_lowercase
duze_znaki = string.ascii_uppercase
cyfry = string.digits
specjalne = string.punctuation
znaki = male_znaki + duze_znaki + cyfry + specjalne

dlugosc_hasla = 5

while len(haslo)<5:
    znak = random.randint(0,len(znaki) -1)
    haslo = haslo +znaki[znak]

print (haslo)