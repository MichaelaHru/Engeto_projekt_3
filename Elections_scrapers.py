import csv
import sys

import requests
from bs4 import BeautifulSoup

from typing import List, Tuple


def ziskej_nazvy_obci(url: str) -> List[Tuple[str, str]]:
    '''
    Ziskava nazvy obci a jejich cisla ze zadane URL.
    Args:
        url (str): Adresa URL, ze ktere se maji ziiskat nazvy obci.
    Vraci:
        List[Tuple[str, str]]: Seznam obsahujici dvojice cisla a nazvu obce.
    Test:
        url='https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106'
    Vysledek:
        [('569119', 'Čavisov'), ('506711', 'Dolní Lhota')]
    '''
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    data = [(sloupce[0].text.strip(), sloupce[1].text.strip())
            for tabulka in soup.find_all("table", class_="table")
            for radek in tabulka.find_all("tr")
            if (sloupce := radek.find_all("td")) and len(sloupce) >= 2]
    return data

def ziskej_odkazy(url: str) -> List[str]:
    '''
    Ziskava seznam odkazu na podrobne vysledky volby z dane URL.
    Args:
        url (str): URL adresa stranky s vysledky volby.
    Vraci:
        List[str]: Seznam odkazů na podrobne vysledky volby.
    Test:
        url='https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106'
    Vysledek:
      ['https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=569119&xvyber=8106',
      'https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=506711&xvyber=8106',]
    '''
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    prvni_odkazy = ['https://volby.cz/pls/ps2021/' + link.get('href')
                    for td in soup.find_all('td', {'class': 'cislo'})
                    if (link := td.find('a'))]
    return prvni_odkazy

def ziskej_informace_odkazu(url: str) -> Tuple[str, str, str]:
    '''
    Ziska informace o volicich, vydani obalek a platnych hlasech z daneho odkazu.
    Args:
        odkaz (str): Odkaz na stranku s detailnimi vysledky volby.
    Vraci:
        Tuple[str, str, str]: Informace o volicich, vydani obalek a platnych hlasech.
    Test:
        url='https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=569119&xvyber=8106'
    Vysledek:
        ('406', '310', '308')
    '''
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    volici_seznamu = soup.find('td', {'headers': 'sa2'}).text.strip()
    vydane_obalky = soup.find('td', {'headers': 'sa3'}).text.strip()
    platne_hlasy = soup.find('td', {'headers': 'sa6'}).text.strip()
    return volici_seznamu, vydane_obalky, platne_hlasy

def ziskej_info_strany(url: str) -> Tuple[List[str], List[str]]:
    '''
    Ziska informace o stranach a poctech hlasu z daneho odkazu.
    Args:
        url (str): Odkaz na stranku s vysledky hlasovani pro jednotlive strany.
    Vraci:
        Tuple[List[str], List[str]]: Seznamy obsahujici nazvy stran a pocty
    Test:
      url='https://volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=14&xobec=569119&xvyber=8106'
    Vysledek:
        (['Strana zelených',
        'Švýcarská demokracie',
        'VOLNÝ blok],
        ['4',
         '0',
         '2',])
    '''
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    strany = [(sloupce[1].text.strip(), sloupce[2].text.strip())
              for tabulka in soup.find_all("table", class_="table")
              for radek in tabulka.find_all("tr")[1:]
              if len((sloupce := radek.find_all("td"))) >= 2]
    strany.pop(0)
    party_names, votes = zip(*strany)
    return list(party_names), list(votes)

def volby_2021(url: str, nazev_souboru: str) -> None:
    '''
    Stáhne a zpracuje výsledky voleb 2021 a uloží je do CSV souboru.
    Args:
        url (str): URL adresa s výsledky voleb.
        nazev_souboru (str): Název souboru, do kterého budou výsledky uloženy.
    Vraci:
        None: Funkce nevrací žádnou hodnotu, pouze provádí zpracování a ukládání dat.
    Vysledek:
        CSV soubor s kompletnimi informacemi napr.
        Cislo,Nazev obce,Volici v seznamu,Vydane obalky,Platne hlasy,Strana zelen�ch,atd
        569119,�avisov,406,310,308,4,0,2,27,14,0,9,0,1,19,82,0,0,0,37,21,88,3,1,-
    '''
    data = ziskej_nazvy_obci(url)
    prvni_odkazy = ziskej_odkazy(url)
    vysledky = []

    for odkaz in prvni_odkazy:
        informace = ziskej_informace_odkazu(odkaz)
        vysledky.append(informace)
        strany, hlasy = ziskej_info_strany(odkaz)
        vysledky.append(hlasy)
        print(f"Zpracovává se odkaz: {odkaz}")

    with open(nazev_souboru, 'w', newline='', encoding='utf-8') as csvfile:
        zapisovac = csv.writer(csvfile)
        zapisovac.writerow(['Cislo', 'Nazev obce', 'Volici v seznamu', 'Vydane obalky', 
                            'Platne hlasy'] + strany)
        for obec, informace, hlas in zip(data, vysledky[::2], vysledky[1::2]):
            cislo, nazev = obec
            volici, obalky, platne_hlasy = informace
            zapisovac.writerow([cislo, nazev, volici, obalky, platne_hlasy] + hlas)

    print(f"Data byla uložena do souboru {nazev_souboru}")

def spousteni_programu() -> None:
    '''
    Spustí program pro stahování dat z vybrané URL a uložení do souboru.

    Příklad spuštění: python program.py http://volby.cz/pls/ps2021/ps3 
    '''
    try:
        if len(sys.argv) != 3:
            raise ValueError('Pro spuštění chybí argumenty.' 
                             'Argumentem musí být zkopírovaná URL a název souboru.')
        if not sys.argv[1].startswith('http'):
            raise ValueError('Prvním argumentem musí být platná URL, ne název souboru.')

        url = sys.argv[1]
        nazev_souboru = sys.argv[2]

        if "volby.cz/pls/ps2021/ps3" not in url:
            raise ValueError('Zadaná adresa URL není platná.')

        response = requests.get(url)
        if response.status_code == 200:
            print(f'Probíhá stahování dat z vybrané URL: {url}')
            volby_2021(url, nazev_souboru)
            print(f'Ukládám data z vybraného URL: {url} do souboru {nazev_souboru}')
        else:
            print('Adresa URL je neplatná nebo nedostupná.')

    except ValueError as e:
        print(f'Chyba: {str(e)}')

if __name__ == "__main__":
    spousteni_programu()
        