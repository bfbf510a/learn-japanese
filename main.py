import requests
import cutlet
from googletrans import Translator
from bs4 import BeautifulSoup

word = ""
kana = ""
eng_meaning = ""

response = requests.post("https://www.coolgenerator.com/random-japanese-words-generator")
html = response.text
soup = BeautifulSoup(html, "html.parser")

vocab_element = soup.select_one(".content-list li:first-child .font-18 span")
meaning_element = soup.select_one(".content-list li:first-child .grey span")

if vocab_element and meaning_element:
    vocab = vocab_element.text.strip()
    eng_meaning = meaning_element.text.strip()
    word, kana = vocab.split("[")
    kana = kana.rstrip("]")
    # print("Word:", word.strip())
    # print("Kana:", kana.strip())
    # print("Meaning:", eng_meaning)
else:
    print("Unable to retrieve the Japanese vocabulary word.")

katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False
romaji = katsu.romaji(word)

translator = Translator()
result = translator.translate(str(word),
                              src='ja',
                              dest='zh-tw')
zch_meaning = result.text

print("Vocabulary: ", word)
print("Kana: ", kana)
print("Romaji: ", romaji)
print("Meaning: ", zch_meaning, ", ", eng_meaning)
