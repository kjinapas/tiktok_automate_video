from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator

def gen_quotes(number):
    text=''
    for i in range(number):
        url = "https://zenquotes.io/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quote = soup.find('h1').get_text()
        
        author = soup.find('p').get_text()
        quotes = quote[1:-1]
        full = quotes+' : '+author
        text =text+full+'\n\n'
        translated = GoogleTranslator(source='auto', target='th').translate(quotes)
        #full_text = f'"{quotes}"\n------------\n{translated}\n\nCredit.{author}'
        full_text = f'"{translated}"\n\nCredit.{author}'
    return full_text

def gen_quotes_v2(number):
    url = f"https://www.generatormix.com/random-inspirational-quotes?number={number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quote = soup.find_all('blockquote','text-left')
    quotes=[]
    for i in quote:
        txt = i.get_text()
        fullquotes = (str(txt).split("--"))
        translated = GoogleTranslator(source='auto', target='th').translate(fullquotes[0])
        full_text = f'"{translated}"\n\nCredit.{fullquotes[1]}'
        quotes.append(full_text)
             
    return quotes