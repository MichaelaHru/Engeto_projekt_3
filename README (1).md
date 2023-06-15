
# Engeto projekt 3

Treti projek pro Engeto akademii

# Popis projektu
Projekt slouzi k extrahovani vysledku voleb do snemovny pro rok 2021. Odkaz k prohlednuti [zde](https://volby.cz/pls/ps2021/ps3?xjazyk=CZ)




# Instalace knihoven

Knihovny, ktere jsou pouzity v kodu jsou ulozeny v `requirements.txt`. Pro instalaci doporucuji vytvorit nove virtualni prostredi.

```bash
 $ pip3 --version                      # overi verzi
 $ pip install -r requirements.txt     # nainstaluje knihovny

```
# Spusteni programu
Spusteni souboru `Elections_scrapers.py` v ramci prikazoveho radku,
vyzaduje dva argumenty

```bash
python Elections_scrapers.py <odkaz-uzemniho-celku> <vysledny soubor>
```
Nasledne se stahnout vysledky v souboru .csv



# Ukazka projektu

Vysledky hlasovani pro okres Ostrava-mesto.

```bash
1.argument: https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106
2.argument: ostrava.csv
```
Spusteni programu:
```bash
python Elections_scrapers.py "https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106" "ostrava.csv"
```
Prubeh stahovani:
```bash
Probíhá stahování dat z vybrané URL: https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=569119&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=506711&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=569500&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=599549&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=554049&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=554821&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=598739&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=598798&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=598836&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=510882&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=598879&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=500291&xvyber=8106
Zpracovává se odkaz: https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=568449&xvyber=8106
Data byla uložena do souboru ostrava.csv
Ukládám data z vybraného URL: https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106 do souboru ostrava.csv

```
Castecny vystup:
```bash
Cislo,Nazev obce,Volici v seznamu,Vydane obalky,Platne hlasy,Strana zelených,Švýcarská demokracie,VOLNÝ blok,...
569119,Čavisov,406,310,308,4,0,2,27,14,0,9,0,1,19,82,0,0,0,37,21,88,3,1,-
506711,Dolní Lhota,1 204,958,955,4,1,18,87,45,0,12,1,3,59,265,2,0,0,107,20,330,0,1,-
...
```