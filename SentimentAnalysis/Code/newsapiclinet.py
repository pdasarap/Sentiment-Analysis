import requests
import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('wordnet')


def dataGenerate(): 

    sourceList = ["bbc-news", "usa-today", "the-washington-post", "abc-news", "cnn"]
    srcLen = len(sourceList)-1
    indlx = random.randint(0, l)
    
    print("CurrntWebSource : ", sourceList[indlx])

    query_params = {
          "sources": sourceList[ind1x],
          "apiKey": "73d62a92c1e746a6b0549b4b59676689"
    }
    urlMain = "https://newsapi.org/v2/everything"
    # Getting data as json
    resp = requests.get(urlMain, params=query_params)

    jsonData = resp.json()['articles']
    respons = []
    for j in jsonData:
        respons.append(j['title'])

    stopwords = set(stopwords.words('english'))

    procData = []
    import re
    regx = '[^a-zA-Z]'

    for r in respons:
        list = word_tokenize(r)
        for val in list:
            val = re.sub(regx, '', val)
            if (val.lower() not in stopwords and len(val) > 3):
                procData.append(val.lower())

    stmt = " ".join(procData)
    return stmt

if __name__ == "__main__":
    dataGenerate()



