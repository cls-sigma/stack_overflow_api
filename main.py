from fastapi import FastAPI

app = FastAPI()
import pickle
import pandas as pd
#from tensorflow import keras
#model = tf.keras.models.load_model('./folder_with_model/')
import nltk
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
english=words.words()

from nltk.tokenize import RegexpTokenizer, word_tokenize, wordpunct_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

with open("rare1.txt", "r") as h:
  rare1=h.read()
rare1=rare1.split(',')


def process(doc):
  #Tokenisation
  tok=RegexpTokenizer(r'\w+')
  doc=tok.tokenize(doc)

  #Supression des stopwords
  doc=[i for i in doc if i not in stop_words]

  #Supression des mots à moins de 3 caractères
  doc=[i for i in doc if len(i)>=3]

  #Lemmatisation
  txt=WordNetLemmatizer()
  doc=[txt.lemmatize(i) for i in doc]

  #Ne garder que les mots anglais
  doc=[i for i in doc if i in english]

  #Ne concerver que les caractères alphanumériques
  doc=[i for i in doc if i.isalpha() ]

  #Supression des mots rares
  doc=[i for i in doc if i not in rare1]

  #Supression des mots qui se repetent de trop

  #Supression des doublons
  doc=pd.Series(doc).value_counts()
  doc=list(doc.index)
  #ou bien on peu faire
  #doc=[i for i in set(doc)]
  
  try:

     doc1=' '.join(doc)
  except:
     doc1=' '.join(['Not' ,'text'])

  return doc1



with open("classes.txt", "r") as h:
  clas=h.read()
clas=clas.split(',')
model=pickle.load(open('stack_model.pkl', 'rb'))

def out(sentence):
    sentence=process(sentence)
    predict=model.predict([sentence])
    output=[]
    for i, j in zip(predict[0], clas):
      if i==1:
        output.append(j)
      else:
        pass
    return output

  
@app.post("/tags")
async def predict(doc: str):
    pred=out(doc)
    return {"Tags": pred}
