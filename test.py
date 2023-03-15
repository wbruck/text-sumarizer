import speech_recognition as sr

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import re

r = sr.Recognizer()

hellow=sr.AudioFile('mix_1m50s-_audio-joiner.com_.wav')
with hellow as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio) # TODO - chage this to whisper so it works offline
    print(s)
except Exception as e:
    print("Exception: "+str(e))

###TODO -  can use GPT for this
# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# article = text
# summary = summarizer(article, max_length=200, min_length=100)

# print(summary)

import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")

text1= NER(text)

for word in text1.ents:
    print(word.text,word.label_)

def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print(sentiment_dict['neg']*100, "% 😡")
    print(sentiment_dict['neu']*100, "% 😑")
    print(sentiment_dict['pos']*100, "% 😇")
 
    print("Minutes of the meetings Overall Rated as", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
 
    else :
        print("Neutral")
 
 
   
# Driver code
if __name__ == "__main__" :
    sentiment_scores(text)