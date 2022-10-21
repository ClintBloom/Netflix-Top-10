import requests
from bs4 import BeautifulSoup


def netflix_data_search():

    data = []
    website = 'https://top10.netflix.com/'
    page = requests.get(website)
    soup = BeautifulSoup(page.content, "html.parser")

    titles = soup.find('tbody')
    for i in titles.children:
        data.append([[f'{list(i)[0].text}:'], [list(i)[1].text], [list(i)[2].text], [list(i)[3].text]])
        #data.append(f'{list(i)[0].text} {list(i)[1].text} {list(i)[2].text} {list(i)[3].text}')
    return data
