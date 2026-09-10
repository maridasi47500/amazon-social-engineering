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
@app.route("/add_one_scoretosend", methods=["GET","POST"])
def add_one_scoretosend():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into scoretosend (title_score,composer,myscore,pic,time_signature,key_signature,receiver_name,receiver_email,message) values (:title_score,:composer,:myscore,:pic,:time_signature,:key_signature,:receiver_name,:receiver_email,:message)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from scoretosend')


        file_pointer = open("./samplescoreexample.ly")
        contents = file_pointer.read()
        contents=contents.replace("KEYSCOREHERE", request.form["key_signature"].replace(" "," \\")).replace("TIMESCOREHERE", request.form["time_signature"]).replace("CONTENTSCOREHERE", request.form["myscore"])
        file_pointer = open("./static/scores/scoretosend_myscore_sample_"+mylastrowid+".ly", "w")
        file_pointer.write(contents)
        file_pointer.close()
        file_pointer = open("./static/scores/scoretosend_myscore_sample_"+mylastrowid+".html", "w")
        file_pointer.write("<lilypond staffsize=34>"+contents+"</lilypond>")
        file_pointer.close()
        subprocess.run(["lilypond-book", "static/scores/scoretosend_myscore_sample_"+mylastrowid+".html", "-f", "html", "--output", "static/scores/samplescorescoretosend_myscore"+mylastrowid]) 

        try:
            f= open("static/scores/samplescorescoretosend_myscore"+mylastrowid+"/scoretosend_myscore_sample_"+mylastrowid+".html")
            s = f.read()
            soup = BeautifulSoup(s)

            picvalue=dict({'pic': "static/scores/samplescoremyscore_mymusic"+mylastrowid+"/"+soup.find('img').get("src"), 'id': mylastrowid})
        except:
            picvalue=dict({'pic': "", "id": mylastrowid})
        print(picvalue)

        hello_there = query_db("update scoretosend set pic = :pic where id = :id",picvalue, one=True)

        return render_template("scoretosendform.html", scoretosends=user, one_user=one_user, the_title="add new scoretosend")


    user = query_db('select * from scoretosend')
    one_user = query_db("select * from scoretosend limit 1", one=True)
    return render_template("scoretosendform.html", scoretosends=user, one_user=one_user, the_title="add new scoretosend")

