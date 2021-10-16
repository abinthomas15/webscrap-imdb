import csv
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(source.text,'html.parser')

csv_file = open('scraped-imdb.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank','Movie-Name','Rating'])

movies = soup.find('tbody',class_='lister-list')

for movie in movies.find_all('tr'):
    name = movie.find('td',class_='titleColumn').a.text
    rank = movie.find('td',class_= 'titleColumn').get_text(strip=True).split('.')[0]
    rating = movie.find('td',class_='ratingColumn imdbRating').strong.text
    print(name)
    print(rank)
    print(rating)

    csv_writer.writerow([rank,name,rating])

csv_file.close()

