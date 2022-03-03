import requests 
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

#import csv

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods = ['GET','POST'])
def index():
    r = request.form.get('url')
    page = requests.get(r)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    quotes=[]  # a list to store quotes
    table = soup.find('div', attrs = {'id':'all_quotes'}) 

    if request.method == 'POST':
        for row in table.findAll('div',
                                attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
            quote = {}
            quote['theme'] = row.h5.text
            #quote['url'] = row.a['href']
            #quote['img'] = row.img['src']
            quote['lines'] = row.img['alt'].split(" #")[0]
            #quote['author'] = row.img['alt'].split(" #")[1]
            quotes.append(quote)

        print(quotes)

    return render_template('index.html',quotes = quotes) 




''' 
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
'''