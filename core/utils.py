from .models import Artikel, Kategori, Artikel_Kategori, Hasil_Kategori
import requests
from bs4 import BeautifulSoup
from pygini import gini
import numpy as np

def get_categories(category):
    dict_of_titles = {}
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmlimit=max&cmtitle=Category:{category}&format=json"
    response = requests.get(url)  # Send the GET request

    # Check for successful response
    if response.status_code == 200:
        data = response.json()  # Convert the response content to JSON
        page_titles = []

        # Extract categories from the response (assuming "categorymembers" exists)
        if "query" in data and "categorymembers" in data["query"]:
            for member in data["query"]["categorymembers"]:
                page_titles.append(member["title"])
        else:
            return []  # Return empty list if no category members found
        dict_of_titles[category] = page_titles
        
        list_of_words_count = []
        list_of_bluelinks_count = []
        # Populate Artikel and Kategori models
        for title in page_titles:
            pageid, word_count, bluelinks_count = get_content(title)
            # print(f"Title: {title}, Page ID: {pageid}, Word Count: {word_count}, Bluelinks Count: {bluelinks_count}")
            if pageid is not None:
                # Save or update Artikel
                artikel_obj, created = Artikel.objects.update_or_create(
                    id_artikel=pageid,
                    defaults={'judul': title, 'word_count': word_count, 'bluelinks_count': bluelinks_count}
                )

                list_of_words_count.append(word_count)
                list_of_bluelinks_count.append(bluelinks_count)
                
                # Save or update Kategori
                kategori_obj, created = Kategori.objects.get_or_create(nama_kategori=category)

                # Save or update Artikel_Kategori
                Artikel_Kategori.objects.update_or_create(id_artikel=artikel_obj, nama_kategori=kategori_obj)

        kategori_obj = Kategori.objects.get(nama_kategori=category)
        gini_1, gini_2 = gini_computes(list_of_words_count, list_of_bluelinks_count)

        # Save or update Hasil_Kategori
        Hasil_Kategori.objects.update_or_create(
            id_kategori=kategori_obj,
            defaults={'words_gini_score': gini_1, 'bluelinks_gini_score': gini_2}
        )
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return []  # Return empty list in case of errors


    return dict_of_titles

#Fungsi untuk melakukan pembersihkan trailing HTML
def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    return soup.get_text()


# Fungsi untuk mendapatkan konten artikel
def get_content(article):
    url = f'https://en.wikipedia.org/w/api.php?action=parse&page={article}&format=json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pageid = data['parse']['pageid']
        page = data['parse']['text']['*']
        num_links = len(data['parse']['links'])

        # Melakukan pembersihan konten dari trailing HTML
        cleaned_extract_column = clean_html(page)
        page_word_count = len(cleaned_extract_column.split())
        return pageid, page_word_count, num_links

    else:
        return None, None, None

def gini_computes(list_word, list_links):
    gini_of_words_count = gini(np.array(list_word, dtype=np.float64))
    gini_of_bluelinks_count = gini(np.array(list_links, dtype=np.float64))
    return gini_of_words_count, gini_of_bluelinks_count