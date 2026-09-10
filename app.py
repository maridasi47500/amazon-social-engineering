from flask import Flask, render_template, request, session, redirect
import string
import random
#from digital_makeup import Maquille

import re
#from codelang_detect import detect as detectprogramminglanguage
#from langdetect import detect as detectspokenlanguage, detect_langs
#from face_recognize import FaceRecognize
#from myplace import Myplace
#comment out if you use

##spell checker
#from spellchecker import SpellChecker
#from textblob import Word
#from autocorrect import Speller
#import speech_recognition as sr
#print(sr.__version__) #find the latest
#import spacy
#from flair.data import Sentence
#from flair.models import SequenceTagger
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from translate import Translator

#image to text
#from PIL import Image
#import pytesseract
#from sendemail import Sendemail


from bs4 import BeautifulSoup
import subprocess
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
