import requests
import re
import os
import csv

###############################################################################
# Najprej definirajmo nekaj pomožnih orodij za pridobivanje podatkov s spleta.
###############################################################################

# definiratje URL glavne strani bolhe za oglase z mačkami
cats_frontpage_url = 'http://www.bolha.com/zivali/male-zivali/macke/'
# mapa, v katero bomo shranili podatke
cat_directory = 'cat_data'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'frontpage.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'cat_data.csv'


def download_url_to_string(url):
    '''This function takes a URL as argument and tries to download it
    using requests. Upon success, it returns the page contents as string.'''
    try:
        # del kode, ki morda sproži napako
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        # koda, ki se izvede pri napaki
        print('Nisem dosegel strani:' + url)
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        return ''
    # nadaljujemo s kodo če ni prišlo do napake
    return r.text


def save_string_to_file(text, directory, filename):
    '''Write "text" to the file "filename" located in directory "directory",
    creating "directory" if necessary. If "directory" is the empty string, use
    the current directory.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(url, directory, frontpage_filename):
    '''Save "cats_frontpage_url" to the file
    "cat_directory"/"frontpage_filename"'''
    save_string_to_file(download_url_to_string(url),
                        directory,
                        frontpage_filename)

###############################################################################
# Po pridobitvi podatkov jih želimo obdelati.
###############################################################################


def read_file_to_string(directory, filename):
    '''Return the contents of the file "directory"/"filename" as a string.'''
    with open(os.path.join(directory, filename), 'r') as dat:
        return dat.read()

# Definirajte funkcijo, ki sprejme niz, ki predstavlja vsebino spletne strani,
# in ga razdeli na dele, kjer vsak del predstavlja en oglas. To storite s
# pomočjo regularnih izrazov, ki označujejo začetek in konec posameznega
# oglasa. Funkcija naj vrne seznam nizov.


def page_to_ads(content):
    regex = re.compile(
        r'<div class="ad[ a-z]*?">(.*?)<div class="clear">', re.DOTALL
        )
    return [x.group(0) for x in re.finditer(regex,
                                            content)]

# Definirajte funkcijo, ki sprejme niz, ki predstavlja oglas, in izlušči
# podatke o imenu, ceni in opisu v oglasu.


def get_dict_from_ad_block(ad):
    '''Build a dictionary containing the name, description and price
    of an ad block.'''
    ad_name = re.compile(r'<h3><a title="(.*?)" href=')
    ad_description = re.compile(r'</a></h3>\s+(.*?)\s+?</?div>', re.DOTALL)
    ad_price = re.compile(r'<div class="price">(<span>)?(?P<cena>.*?)(</span>)?</div>')
    return {'name': re.search(ad_name, ad).group(1), 'description': re.search(ad_description, ad).group(1), 'price': re.search(ad_price, ad).groupdict()['cena']}

# Definirajte funkcijo, ki sprejme ime in lokacijo datoteke, ki vsebuje
# besedilo spletne strani, in vrne seznam slovarjev, ki vsebujejo podatke o
# vseh oglasih strani.


def ads_from_file(directory, filename):
    '''Parse the ads in filename/directory into a dictionary list.'''
    return [get_dict_from_ad_block(ad) for ad in page_to_ads(read_file_to_string(directory, filename))]

###############################################################################
# Obdelane podatke želimo sedaj shraniti.
###############################################################################


def write_csv(fieldnames, rows, directory, filename):
    '''Write a CSV file to directory/filename. The fieldnames must be a list of
    strings, the rows a list of dictionaries each mapping a fieldname to a
    cell-value.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None

# Definirajte funkcijo, ki sprejme neprazen seznam slovarjev, ki predstavljajo
# podatke iz oglasa mačke, in zapiše vse podatke v csv datoteko. Imena za
# stolpce [fieldnames] pridobite iz slovarjev.


def write_cat_ads_to_csv(TODO):
    return TODO

l = page_to_ads(read_file_to_string(cat_directory, frontpage_filename))
d = get_dict_from_ad_block(l[0])
s = ads_from_file(cat_directory, frontpage_filename)
