from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.python.org/downloads/"
response = requests.get(url)
bs = BeautifulSoup(response.text, "lxml")

temp_version_list = bs.find_all('span', 'release-number')
temp_date_list = bs.find_all('span', 'release-date')
temp_url_download_list = bs.find_all('span', 'release-download')
temp_release_notes_list = bs.find_all('span', 'release-enhancements')

ver_list = []
date_list = []
url_download_list = []
release_notes_list = []

#Цикл начинается с 1, для отсечения первой строки таблицы, там не нужные данные
for i in range(1, len(temp_version_list)):
    version = temp_version_list[i].text
    ver_list.append(version)

    date = temp_date_list[i].text
    date_list.append(date)

    temp = temp_url_download_list[i].find('a', href=True)
    url_download_list.append('https://www.python.org' + temp['href'])

    temp = temp_release_notes_list[i].find('a', href=True)
    release_notes_list.append(temp['href'])
    i += 1

df = pd.DataFrame({'Release Version': ver_list,
                    'Release date' : date_list,
                    'URL for download': url_download_list,
                    'URL for notes': release_notes_list
                   })
    

df.to_excel('./generate/Release version python.xlsx', sheet_name='Release version python', index=True)
