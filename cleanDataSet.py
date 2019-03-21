import re
import pandas as pd
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords

def reviewToWords(rawReview, stops):
    words = (re.sub('[^a-zA-Z]+', " ", rawReview)).lower().split()
    words = [str(r) for r in words]
    words = [w for w in words if not w in stops]
    sentence = " ".join(words)
    return sentence

if __name__ == "__main__":
    reviews = []
    stops = list(stopwords.words('english'))
    train = pd.read_csv('labeledTrainData.tsv', header=0, delimiter='\t', quoting=3)
    for i in range(len(train)):
        rawData = bs(train["review"][i],features="html.parser").encode('utf-8')
        reviews.append(reviewToWords(rawData, stops))
    print len(reviews)