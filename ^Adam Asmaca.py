import random
import os
from time import sleep

kelimeler = ["Bilişim", "Python", "Kodlama", "Satranç", "Oyun", "Okul"]

resim = ["""
   +---+
       |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]

secilen_kelime = random.choice(kelimeler)
zemin="-"*len(secilen_kelime)
zeminx=[]
zeminin_alti=[]
zemin=list(zemin)
sayac2=-1
sayac3=0
while (True):
   sayac=-1
   sayac2+=1
   os.system("cls")
   print(resim[sayac3])
   print(" ")
   print("".join(zemin))
   print("".join(zeminin_alti))
   print(" ")
   if sayac2==0:
      kullanici_girisi=input("harfi veya tahmin ettiğiniz kelimeyi giriniz: ")
      print("".join(zemin))
   else:
      kullanici_girisi=input("harfi veya kelimeyi giriniz: ")
   if kullanici_girisi.lower()==secilen_kelime.lower():
      os.system("cls")
      print(secilen_kelime.lower())
      print("Kazandın")
      sleep(5)
      os.system("cls")
      break
   for i in secilen_kelime:
      sayac += 1
      if i==kullanici_girisi.upper() or i==kullanici_girisi.lower():
         zemin[sayac]=kullanici_girisi
         zeminx.append(kullanici_girisi)
      elif kullanici_girisi.lower() not in secilen_kelime.lower():
         sayac3+=1
         if sayac2==0:
            zeminin_alti.append(kullanici_girisi)
            break
         else:
            zeminin_alti.append("-")
            zeminin_alti.append(kullanici_girisi)
            break
   if len(zeminx)==len(secilen_kelime):
      os.system("cls")
      print(secilen_kelime.lower())
      print("Kazandın")
      sleep(5)
      os.system("cls")
      break
   if sayac3==8:
      os.system("cls")
      print(resim[sayac-1])
      print(" ")
      print("kaybettin")
      print(" ")
      print(f"kelime {secilen_kelime} idi")
      sleep(5)
      os.system("cls")
      break