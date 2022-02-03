#!/usr/bin/env python3

import hashlib
import os

#definizione delle funzioni 

def funzione_MD5(stringa):
    s = hashlib.md5(stringa.encode()).hexdigest()
    file_md5 = input("Nome del file di salvataggio: ")
    destinazione = input("Destinazione del file: ")
    t = destinazione + file_md5
    f = open(t, "a")
    f.write(s + "\n")
    f.close()

def funzione_sha256(stringa):
    s = hashlib.sha256(stringa.encode()).hexdigest()
    file_sha256 = input("Nome del file di salvataggio: ")
    destinazione = input("Destinazione del file: ")
    t = destinazione + file_sha256
    f = open(t, "a")
    f.write(s + "\n")
    f.close()

def funzione_sha512(stringa):
    s = hashlib.sha512(stringa.encode()).hexdigest()
    file_sha512 = input("Nome file di salvataggio: ")
    destinazione = input("destinazione del file: ")
    t = destinazione + file_sha512
    f = open(t, "a")
    f.write(s + "\n")
    f.close()

#programma dove comincia

try:
    testo = input("Inserisci tresto da convertire: ")
    print("\nPremi 1 per convertire in MD5")
    print("Premi 2 per convertire in Sha256")
    print("Premi 3 per convertire in sha512")
    print("Premi 4 per uscire dal programma")
    scelta = input("Scelta: ")
    if scelta == "1":
        funzione_MD5(testo)
    elif scelta == "2":
        funzione_sha256(testo)
    elif scelta == "3": 
        funzione_sha512(testo)
    elif scelta == "4":
        exit(-1)
    else:
        print("Errore di digitazione comando! \n")
except KeyboardInterrupt:
    print("Can't use CTRL^C\n")
