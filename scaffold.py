# -*- coding: utf-8 -*-

import sys
import os
print(sys.argv[1])


filename=sys.argv[1].lower() 
myclass=(filename).capitalize()
modelname=(filename).capitalize()
marouteget="\"/%s\"" % filename
maroutenew="\"/%s_new\"" % filename
maroutecreate="\"/%s_create\"" % filename
marouteget2="\\\"/%s\\\"" % filename
myhtml="my"+filename+"html"
myfavdirectory=filename
index = 2 
createtable=""
columns="("
formhtml="<form  enctype=\"multipart/form-data\" method=\"POST\">"
values="("
mysession="["
myparam=","
items=sys.argv
normalitems=[]
languages={
  "af": "Afrikaans",
  "ar": "Arabic",
  "bg": "Bulgarian",
  "bn": "Bengali",
  "ca": "Catalan",
  "cs": "Czech",
  "cy": "Welsh",
  "da": "Danish",
  "de": "German",
  "el": "Greek",
  "en": "English",
  "es": "Spanish",
  "et": "Estonian",
  "fa": "Farsi",
  "fi": "Finnish",
  "fr": "French",
  "gu": "Gujarati",
  "he": "Hebrew",
  "hi": "Hindi",
  "hr": "Croatian",
  "hu": "Hungarian",
  "id": "Indonesian",
  "it": "Italian",
  "ja": "Japanese",
  "kn": "Kannada",
  "ko": "Korean",
  "lt": "Lithuanian",
  "lv": "Latvian",
  "mk": "FYRO Macedonian",
  "ml": "Mali",
  "mr": "Marathi",
  "ne": "Nepali",
  "nl": "Dutch",
  "no": "Norwegian",
  "pa": "Punjabi",
  "pl": "Polish",
  "pt": "Portuguese",
  "ro": "Romanian",
  "ru": "Russian",
  "sk": "Slovak",
  "sl": "Slovenian",
  "so": "Somali language",
  "sq": "Albanian",
  "sv": "Swedish",
  "sw": "Swahili",
  "ta": "Tamil",
  "te": "Telugu",
  "th": "Thai",
  "tl": "Tagalog",
  "tr": "Turkish",
  "uk": "Ukrainian",
  "ur": "Urdu",
  "vi": "Vietnamese",
  "zh-cn": "Chinese (China)",
  "zh-tw": "Chinese Taiwan"
}
programmingl={
  "c": "C ",
  "cpp": "C++ ",
  "cs": "C# ",
  "cbl": "COBOL ",
  "css": "CSS ",
  "dart": "Dart ",
  "go": "Go ",
  "groovy": "Groovy ",
  "html": "HTML ",
  "java": "Java ",
  "js": "JavaScript ",
  "json": "JSON ",
  "kt": "Kotlin ",
  "php": "PHP ",
  "py": "Python ",
  "r": "R ",
  "rb": "Ruby ",
  "rs": "Rust ",
  "scala": "Scala ",
  "sh": "Shell ",
  "sol": "Solidity ",
  "sql": "SQL ",
  "swift": "Swift ",
  "ts": "TypeScript ",
  "xml": "XML ",
  "yaml": "YAML "
}
for x in items:
    normalitems.replace(":send_email","").replace(":image_to_text","").replace(":speech_to_text","").replace(":translate","").replace(":sentiment","").replace(":find_organization_group","").replace(":did_you_mean","").replace(":hidden","").replace(":detect_language","").replace(":detect_programming_language","").replace(":textarea","").replace(":find_email_phone","").replace(":sunglasses","").replace(":recognize_face","").replace(":maquille","").replace(":staff","").replace(":color","").replace(":password","").replace(":email","").replace(":datetime","").replace(":date","").replace(":time","").replace(":radio","").replace(":checkbox","").replace(":file","").replace(":references",""))
myfavouriteitem=normalitems[2]
referencesstr=""
postreferences=""
references=""

mylastrowid="""
"""
requestfiles="""
"""
sqltousles="""
"""
sqltousles2="""
"""
while index < (len(items)):

    try:
      print(index, items[index])
      hasfile=""
      referencesstr=""
      checkbox=""
      sentiment=""
      sendemail=""
      translate=""
      staff=""
      sunglasses=""
      did_you_mean=""
      find_org_group=""
      speech_to_text=""
      image_to_text=""
      find_email_phone=""
      color=""
      myemail=""
      mypassword=""
      mydate=""
      mytime=""
      hidden=""
      mydatetime=""
      maquille=""
      recognize_face=""
      textarea=""
      detect_programming_language=""
      detect_language=""
      radiobutton=""
      paramname=items[index]
      if ":translate" in paramname: 
          translate="yes"
      if ":find_organization_group" in paramname: 
          find_org_group="yes"
      if ":send_email" in paramname: 
          sendemail="yes"
      if ":image_to_text" in paramname: 
          image_to_text="yes"
      if ":speech_to_text" in paramname: 
          speech_to_text="yes"
      if ":sentiment" in paramname: 

          sentiment="yes"
      if ":did_you_mean" in paramname: 

          did_you_mean="yes"
      if ":email" in paramname: 

          myemail="yes"
      if ":hidden" in paramname: 
          hidden="yes"
      if ":color" in paramname: 
          color="yes"
      if ":date" in paramname: 
          mydate="yes"
      if ":time" in paramname: 
          mytime="yes"
      if ":datetime" in paramname: 
          mydatetime="yes"
      if ":password" in paramname: 
          mypassword="yes"

      if ":detect_language" in paramname: 
          detect_language="yes"
      if ":detect_programming_language" in paramname: 
          detect_programming_language="yes"
      if ":find_email_phone" in paramname: 
          find_email_phone="yes"
      if ":sunglasses" in paramname: 
          sunglasses="yes"
      if ":recognize_face" in paramname: 
          recognize_face="yes"
      if ":staff" in paramname: 
          staff="yes"
      if ":maquille" in paramname: 
          maquille="yes"
      if ":textarea" in paramname: 
          textarea="yes"
      if ":checkbox" in paramname: 
          checkbox="yes"
      if ":radio" in paramname: 
          radiobutton="yes"

      if ":file" in paramname: 
          hasfile="yes"
      if ":references" in paramname: 
          referencesstr="yes"
      paramname=normalitems[index]
      print(items[(index+1)])
    except:
      myparam=""
    index += 1
    myfieldtype="text"
    if radiobutton == "yes":
        myfieldtype="radio"
    if textarea == "yes":
        myfieldtype="textarea"
    if maquille == "yes":
        myfieldtype="file"
    if hidden == "yes":
        myfieldtype="hidden"
    if mydatetime == "yes":
        myfieldtype="datetime"
    if mytime == "yes":
        myfieldtype="time"
    if myemail == "yes":
        myfieldtype="email"
    if mypassword == "yes":
        myfieldtype="password"
    if mydate == "yes":
        myfieldtype="date"
    if color == "yes":
        myfieldtype="color"
    if staff == "yes":
        myfieldtype="textarea"
    if checkbox == "yes":
        myfieldtype="checkbox"
    if staff == "yes":
        mylastrowid+="""
        file_pointer = open("./samplescoreexample.ly")
        contents = file_pointer.read()
        contents=contents.replace("KEYSCOREHERE", request.form["key_signature"].replace(" "," \\\\")).replace("TIMESCOREHERE", request.form["time_signature"]).replace("CONTENTSCOREHERE", request.form["{columnname}"])
        file_pointer = open("./static/scores/{tablename}_{columnname}_sample_"+mylastrowid+".ly", "w")
        file_pointer.write(contents)
        file_pointer.close()
        file_pointer = open("./static/scores/{tablename}_{columnname}_sample_"+mylastrowid+".html", "w")
        file_pointer.write("<lilypond staffsize=34>"+contents+"</lilypond>")
        file_pointer.close()
        subprocess.run(["lilypond-book", "static/scores/{tablename}_{columnname}_sample_"+mylastrowid+".html", "-f", "html", "--output", "static/scores/samplescore{tablename}_{columnname}"+mylastrowid]) 

        try:
            f= open("static/scores/samplescore{tablename}_{columnname}"+mylastrowid+"/{tablename}_{columnname}_sample_"+mylastrowid+".html")
            s = f.read()
            soup = BeautifulSoup(s)
""".format(tablename=filename,columnname=paramname)

        mylastrowid+="""
            picvalue=dict({'pic': "static/scores/samplescoremyscore_mymusic"+mylastrowid+"/"+soup.find('img').get("src"), 'id': mylastrowid})
        except:
            picvalue=dict({'pic': "", "id": mylastrowid})
        print(picvalue)
"""
        mylastrowid+="""
        hello_there = query_db("update {tablename} set pic = :pic where id = :id",picvalue, one=True)
""".format(tablename=filename,columnname=paramname)
    if sendemail=="yes":
      myfieldtype="textarea"
      requestfiles+="""

        try:
            Sendemail(receiver_emails=[hey["receiver_email"]], receiver_names=[hey["receiver_name"]], filename=hey["pic"], message=hey["{paramname}"])
            
        except:
            print("error ouille")
""".format(paramname=paramname)
    if find_org_group=="yes":
      myfieldtype="textarea"
      postreferences+=", my_org_group=my_org_group"
      requestfiles+="""

        nlp = spacy.load("en_core_web_sm")
        my_org_group=""
        
        text = hey["{paramname}"]
        
        doc = nlp(text)
        
        try:
            for ent in doc.ents:
                print(ent.text, ent.label_)
                my_org_group += "<br>"+(ent.text + " " + ent.label_)
        except:
            print("error ouille")
        try:
            tagger = SequenceTagger.load("ner")
            sentence = Sentence(text)
            tagger.predict(sentence)
            my_org_group += "<br>"+sentence.get_spans('ner')
            print(sentence.get_spans('ner'))
        except:
            print("error ouille")
""".format(paramname=paramname)
    if translate=="yes":
      myfieldtype="textarea"
      postreferences+=", mytranslation=mytranslation"
      requestfiles+="""


        mytext=hey["{paramname}"]

        try:
            mylanguage=query_db("select x.short_name from language x where x.id = ?", [hey["language_id"]], one=True)["short_name"]
            translator = Translator(to_lang=mylanguage)
            mytranslation = translator.translate(mytext)


            print(mytranslation)

        except Exception as e:
            print("ereeeuuuuur!!! ooowow!",e)
""".format(paramname=paramname)
    if image_to_text=="yes":
      myfieldtype="file"
      postreferences+=", imagetotext=imagetotext"
      requestfiles+="""



        try:
            mylanguage=query_db("select x.short_name_three from language x where x.id = ?", [hey["language_id"]], one=True)["short_name_three"]

            imagetotext=pytesseract.image_to_string("./static/photos/"+hey["{paramname}"])
            print(imagetotext)

        except Exception as e:
            print("ereeeuuuuur!!! ooowow!",e)
""".format(paramname=paramname)
    if speech_to_text=="yes":
      myfieldtype="file"
      postreferences+=", mytts=mytts"
      requestfiles+="""

        r = sr.Recognizer()

        harvard = sr.AudioFile("./static/photos/"+hey["{paramname}"])
        with harvard as source:
           audio = r.record(source)


        try:
            mylanguage=query_db("select x.short_name from language x where x.id = ?", [hey["language_id"]], one=True)["short_name"]
            #mytts=r.recognize_bing(audio, language=mylanguage) 
            mytts=r.recognize_google(audio, language=mylanguage) 


            print(mytts)

        except Exception as e:
            print("ereeeuuuuur!!! ooowow!",e)
""".format(paramname=paramname)
    if detect_programming_language=="yes":
      myfieldtype="textarea"
      requestfiles+="""


        myprog=detectprogramminglanguage(hey["{paramname}"])

        try:
            hey["programminglanguage_id"]=query_db("select x.id from programminglanguage x where x.short_name = ?", [myprog], one=True)["id"]
            #hey["programming_language_id"]=query_db("select x.id from programming_language x where x.short_name = ?", [myprog], one=True)["id"]

        except Exception as e:
            print("ereeeuuuuur!!! ooowow!",e)
""".format(paramname=paramname)
    if sunglasses == "yes":
      myfieldtype="file"
      requestfiles+="""
        uploaded_file = request.files['{paramname}']
        char_set = string.ascii_uppercase + string.digits
        myfilename=''.join(random.sample(char_set*6, 8))+"."+uploaded_file.filename.
split('.')[-1]

        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', myfilename))



        hey["{paramname}"]=myfilename
        try:
            #x=subprocess.Popen(["/usr/bin/python3.9","addsunglasses.py",hey["{paramname}"]])
            x=subprocess.check_output(["/home/"+os.environ['USER']+"/miniconda3/bin/python3","addsunglasses.py",hey["pic"]])

        except Exception as e:
            print("ereeeuuuuur!!! ooowow!",e)
""".format(paramname=paramname)
    if find_email_phone == "yes":
      myfieldtype="textarea"
      requestfiles+="""
      email = re.findall(r'\S+@\S+', hey["{paramname}"])

      phone = re.findall(r'\d{10}', hey["{paramname}"])
      
      print("Email:", email)
      print("Phone:", phone)
""".format(paramname=paramname)
    if maquille == "yes":
      myfieldtype="file"
      requestfiles+="""
        uploaded_file = request.files['{paramname}']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))
        x=Maquille(uploaded_file.filename).find_landmarks()

        hey["{paramname}"]=uploaded_file.filename
""".format(paramname=paramname)
    if hasfile == "yes":
      myfieldtype="file"
      requestfiles+="""
        uploaded_file = request.files['{paramname}']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["{paramname}"]=uploaded_file.filename
""".format(paramname=paramname)
    if paramname == "password":
        myfieldtype = "password"
    if paramname == "email":
        myfieldtype = "email"
    if paramname == "telephone" or paramname == "phone":
        myfieldtype = "telephone"
        


    if sentiment == "yes":
        myfieldtype="textarea"
        postreferences+=", sentimentscores=sentimentscores"
        sqltousles+="""

        texttocheck=hey["{paramname}"]
        analyzer = SentimentIntensityAnalyzer()

        
        sentimentscores = analyzer.polarity_scores(texttocheck)
        
        print(sentimentscores)

""".format(paramname=paramname, tablename=filename)
    if did_you_mean == "yes":
        postreferences+=", did_you_mean=(did_you_mean1+' '+did_you_mean2+' '+did_you_mean3)"
        sqltousles+="""
        texttocheck=hey["{paramname}"]
        spell = SpellChecker()
        words = spell.split_words(texttocheck)

        did_you_mean1=[spell.correction(word) for word in words].join(" ")
        did_you_mean2=[Word(word).spellcheck()[0][0] for word in words].join(" ")
        try:
          language= query_db("select x.short_name from language x on x.id = ?", [hey["language_id"]],  one=True)["short_name"]
        except:
          language= "fr"
        check = Speller(lang=language)
        did_you_mean3=check(texttocheck)

""".format(paramname=paramname, tablename=filename)
    if recognize_face == "yes":
        references+=", tousles{paramname}=tousles{paramname}".format(paramname=paramname.replace("_id",""))
        sqltousles+="""
        tousles{paramname}= query_db("select * from {paramname}")
        knownpic{paramname}= []
        findpic{paramname}= query_db("select x.pic from {paramname} x where x.id = ?", [request.form["{paramname}_id"]], one=True)
        #findpic{paramname}= query_db("select x.pic from {paramname} x ) #optional compare photo with all users from the relational table
        #for x in findpic{paramname}:
        #    knownpic{paramname}.append(x["pic"])

        knownpic{paramname}.append(findpic{paramname}["pic"])
        unknownpic=hey["pic"]
        x=FaceRecognize(knownpic{paramname}, unknownpic).get_results()
        hey["recognized_face"]=str(x)

""".format(paramname=paramname.replace("_id",""), tablename=filename)
        sqltousles2+="""
    tousles{paramname}= query_db("select * from {paramname}")
""".format(paramname=paramname.replace("_id",""))
        formhtml+="\n<div class=\"field\"><label for=\"somefield{paramname}\">{paramname}</label><select id=\"somefield{paramname}\" name=\"{paramname}\"><option value=\"novalue\">no value</option>".format(myparam=myparam,paramname=paramname,mytype=myfieldtype,tablename=filename)
        formhtml+="\n{% "+"for some{paramname} in tousles{paramname}".format(myparam=myparam,paramname=paramname.replace("_id",""),mytype=myfieldtype)+" %}"
        formhtml+="\n<option value=\"{{ some"+paramname.replace("_id","")+"['id'] }}\">{{ some"+paramname.replace("_id","")+"['name'] }}</option>{% endfor %}"
        formhtml+="\n</select></div>"
    if referencesstr == "yes":
        references+=", tousles{paramname}=tousles{paramname}".format(paramname=paramname.replace("_id",""))
        sqltousles+="""
        tousles{paramname}= query_db("select * from {paramname}")
""".format(paramname=paramname.replace("_id",""))
        sqltousles2+="""
    tousles{paramname}= query_db("select * from {paramname}")
""".format(paramname=paramname.replace("_id",""))
        formhtml+="\n<div class=\"field\"><label for=\"somefield{paramname}\">{paramname}</label><select id=\"somefield{paramname}\" name=\"{paramname}\"><option value=\"novalue\">no value</option>".format(myparam=myparam,paramname=paramname,mytype=myfieldtype,tablename=filename)
        formhtml+="\n{% "+"for some{paramname} in tousles{paramname}".format(myparam=myparam,paramname=paramname.replace("_id",""),mytype=myfieldtype)+" %}"
        formhtml+="\n<option value=\"{{ some"+paramname.replace("_id","")+"['id'] }}\">{{ some"+paramname.replace("_id","")+"['name'] }}</option>{% endfor %}"
        formhtml+="\n</select></div>"

    elif myfieldtype == "textarea":
        formhtml+="\n<div class=\"field\"><label for=\"somefield{paramname}\">{paramname}</label><textarea id=\"somefield{paramname}1\" name=\"{paramname}\"></textarea>\n</div>".format(myparam=myparam,paramname=paramname,mytype=myfieldtype)
    elif radiobutton == "yes":
        formhtml+="\n<div class=\"field\"><label for=\"somefield{paramname}\">{paramname}</label><label for=\"somefield{paramname}1\"><input type=\"{mytype}\" id=\"somefield{paramname}1\" name=\"{paramname}\" value=\"1\"/>yes</label>\n<label for=\"somefield{paramname}2\"><input type=\"{mytype}\" id=\"somefield{paramname}2\" name=\"{paramname}\" value=\"0\"/>no</label></div>".format(myparam=myparam,paramname=paramname,mytype=myfieldtype)
    elif checkbox == "yes":
        formhtml+="\n<div class=\"field\"><input type=\"{mytype}\" id=\"somefield{paramname}\" name=\"{paramname}\" value=\"1\"/><label for=\"somefield{paramname}\">{paramname}</label></div>".format(myparam=myparam,paramname=paramname,mytype=myfieldtype)
    else:
        formhtml+="\n<div class=\"field\"><label for=\"somefield{tablename}{paramname}\">{paramname}</label><input type=\"{mytype}\" id=\"somefield{tablename}{paramname}\" name=\"{paramname}\"/></div>".format(myparam=myparam,paramname=paramname,mytype=myfieldtype,tablename=filename)


    mysession+="'{paramname}'{myparam}".format(myparam=myparam,paramname=paramname)
    columns+="{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
    values+=":{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
    createtable+="""        {paramname} text{myparam}
    """.format(myparam=myparam,paramname=paramname)
columns+=")"
values+=")"
mysession+="]"
mystr="""create table if not exists {filename}(
        id integer primary key autoincrement,
"""
mystr+=createtable
mystr+="  , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"


mystr+="""                );
"""
if filename == "language" or name == "languages":
    code={
  "ab": "abk",
  "aa": "aar",
  "af": "afr",
  "ak": "aka",
  "sq": "sqi",
  "am": "amh",
  "ar": "ara",
  "an": "arg",
  "hy": "hye",
  "as": "asm",
  "av": "ava",
  "ae": "ave",
  "ay": "aym",
  "az": "aze",
  "bm": "bam",
  "ba": "bak",
  "eu": "eus",
  "be": "bel",
  "bn": "ben",
  "bi": "bis",
  "bs": "bos",
  "br": "bre",
  "bg": "bul",
  "my": "mya",
  "ca": "cat",
  "ch": "cha",
  "ce": "che",
  "ny": "nya",
  "zh": "zho",
  "cu": "chu",
  "cv": "chv",
  "kw": "cor",
  "co": "cos",
  "cr": "cre",
  "hr": "hrv",
  "cs": "ces",
  "da": "dan",
  "dv": "div",
  "nl": "nld",
  "dz": "dzo",
  "en": "eng",
  "eo": "epo",
  "et": "est",
  "ee": "ewe",
  "fo": "fao",
  "fj": "fij",
  "fi": "fin",
  "fr": "fra",
  "fy": "fry",
  "ff": "ful",
  "gd": "gla",
  "gl": "glg",
  "lg": "lug",
  "ka": "kat",
  "de": "deu",
  "el": "ell",
  "kl": "kal",
  "gn": "grn",
  "gu": "guj",
  "ht": "hat",
  "ha": "hau",
  "he": "heb",
  "hz": "her",
  "hi": "hin",
  "ho": "hmo",
  "hu": "hun",
  "is": "isl",
  "io": "ido",
  "ig": "ibo",
  "id": "ind",
  "ia": "ina",
  "ie": "ile",
  "iu": "iku",
  "ik": "ipk",
  "ga": "gle",
  "it": "ita",
  "ja": "jpn",
  "jv": "jav",
  "kn": "kan",
  "kr": "kau",
  "ks": "kas",
  "kk": "kaz",
  "km": "khm",
  "ki": "kik",
  "rw": "kin",
  "ky": "kir",
  "kv": "kom",
  "kg": "kon",
  "ko": "kor",
  "kj": "kua",
  "ku": "kur",
  "lo": "lao",
  "la": "lat",
  "lv": "lav",
  "li": "lim",
  "ln": "lin",
  "lt": "lit",
  "lu": "lub",
  "lb": "ltz",
  "mk": "mkd",
  "mg": "mlg",
  "ms": "msa",
  "ml": "mal",
  "mt": "mlt",
  "gv": "glv",
  "mi": "mri",
  "mr": "mar",
  "mh": "mah",
  "mn": "mon",
  "na": "nau",
  "nv": "nav",
  "nd": "nde",
  "nr": "nbl",
  "ng": "ndo",
  "ne": "nep",
  "no": "nor",
  "nb": "nob",
  "nn": "nno",
  "oc": "oci",
  "oj": "oji",
  "or": "ori",
  "om": "orm",
  "os": "oss",
  "pi": "pli",
  "ps": "pus",
  "fa": "fas",
  "pl": "pol",
  "pt": "por",
  "pa": "pan",
  "qu": "que",
  "ro": "ron",
  "rm": "roh",
  "rn": "run",
  "ru": "rus",
  "se": "sme",
  "sm": "smo",
  "sg": "sag",
  "sa": "san",
  "sc": "srd",
  "sr": "srp",
  "sn": "sna",
  "sd": "snd",
  "si": "sin",
  "sk": "slk",
  "sl": "slv",
  "so": "som",
  "st": "sot",
  "es": "spa",
  "su": "sun",
  "sw": "swa",
  "ss": "ssw",
  "sv": "swe",
  "tl": "tgl",
  "ty": "tah",
  "tg": "tgk",
  "ta": "tam",
  "tt": "tat",
  "te": "tel",
  "th": "tha",
  "bo": "bod",
  "ti": "tir",
  "to": "ton",
  "ts": "tso",
  "tn": "tsn",
  "tr": "tur",
  "tk": "tuk",
  "tw": "twi",
  "ug": "uig",
  "uk": "ukr",
  "ur": "urd",
  "uz": "uzb",
  "ve": "ven",
  "vi": "vie",
  "vo": "vol",
  "wa": "wln",
  "cy": "cym",
  "wo": "wol",
  "xh": "xho",
  "ii": "iii",
  "yi": "yid",
  "yo": "yor",
  "za": "zha",
  "zu": "zul"
}
    for x in languages:
        mystr+="""         insert into {filename} (name, short_name, short_name_three) values ("{name}", "{shortname}", "{shortnamethree}");
""".format(filanem=filename, name=languages[x], shortname=x, shortnamethree=code[x]);
if filename == "programminglanguage" or filename == "programming_language":
    for x in programmingl:
        mystr+="""         insert into {filename} (name, short_name) values ("{name}", "{shortname}");
""".format(filanem=filename, name=programmingl[x], shortname=x);
selectall= "select * from {filename}"

delete="""delete from {filename} where id = ?",(myid,)"""
selectone="""select * from {filename} where id = ?",(myid,)"""
addone="""@app.route("/add_one_{filename}", methods=["GET","POST"])
def add_one_{filename}():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)""".format(filename=filename, mysession=mysession,columns=columns,values=values,references=references)
addone+=requestfiles.format(filename=filename, mysession=mysession,columns=columns,values=values,references=references)
addone+=sqltousles.format(filename=filename, mysession=mysession,columns=columns,values=values,references=references)

addone+="""
        one_user = query_db("insert into {filename} {columns} values {values}",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from {filename}')
""".format(filename=filename, mysession=mysession,columns=columns,values=values,references=references)
addone+=mylastrowid
if filename == "user":
    addone+="""
        last_user = query_db("select * from {filename} where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in {mysession}:
            session[x]=hey[x]

""".format(filename=filename, mysession=mysession,columns=columns,values=values)
addone+="""
        return render_template("{filename}form.html", {filename}s=user, one_user=one_user, the_title="add new {filename}"{references}{postreferences})
""".format(filename=filename, mysession=mysession,columns=columns,values=values,references=references)
addone+=sqltousles2
addone+="""
    user = query_db('select * from {filename}')
    one_user = query_db("select * from {filename} limit 1", one=True)
    return render_template("{filename}form.html", {filename}s=user, one_user=one_user, the_title="add new {filename}"{references})

""".format(filename=filename, mysession=mysession,columns=columns,values=values,references=references)
if filename == "user":
    addone+="""
@app.route("/{filename}_sign_out", methods=["GET","POST"])
def {filename}_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in {mysession}:
            session[x]=""
        return redirect("/")


@app.route("/{filename}_log_in", methods=["GET","POST"])
def {filename}_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from {filename} where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in {mysession}:
                session[x]=hey[x]
        except:
            return render_template("{filename}login.html")
    return render_template("{filename}login.html")
""".format(filename=filename,mysession=mysession,columns=columns,values=values)
if "lat" in items and "lon" in items:

    lieu="""

@app.route("/searchjobcity", methods=["POST"])
def trouver_lieu_city():
    leslieu=Myplace(request.form["lieu"]).trouver1()

    return dict({"city":leslieu[0], "code":leslieu[1], "region":leslieu[3], "departement":leslieu[2], "pays":leslieu[2], "latitude":leslieu[4], "longitude":leslieu[5]})
"""
else:
    lieu=""

with open("app.py", "a") as myfile:
    #myfile.write(addone.format(filename=filename,columns=columns,values=values)+lieu)
    myfile.write(addone+lieu)
with open("schema.sql", "a") as myfile:
    myfile.write(mystr.format(filename=filename))
with open("templates/base.html", "a") as myfile:
    myfile.write("<a href=\"/add_one_{filename}\"> add one {filename}</a>".format(filename=filename))

if "lat" in items and "lon" in items:
    maphtmlcode="""
<div id="monadresse">
</div>
<div id="autresoffres">
</div>

     <div class="field">

                                         <label for="monlieu1">lieu</label>


         <input type="text" name="lieu" id="monlieu1" placeholder="nom du lieu"/>


                 </div>

                <button id="loadmycity" type="button">chercher l'adresse</button>

<div id="chercherunjob" style="display:none;">
la carte est bien là ou est l'offre d'emploi?
</div>

                                                        <input type="hidden" value="" id="maregion1" name="region" />
                                                        <input type="hidden" value="" id="monpays1" name="pays" />


        <input type="hidden" value="" id="moncode1" name="code" />


        <input type="hidden" value="" id="maville1" name="ville" />


        <input type="hidden" value="" id="monrayon1" name="rayon" />

                                                         <input type="hidden" onchange="" name="job" value="informatique" id="monjob1" placeholder="nom du job"/>

"""
    maphtmlcode+=("<div id=\"imap\"><div id=\"map\" style=\"height:200px;width:100%;\" onclick=\"onMapClick(event);\"><!-- Ici s'affichera la carte --></div>")
    othermapjs=("{% block jsmap %}"+"<script src=\"https://code.jquery.com/jquery-4.0.0.js\" integrity=\"sha256-9fsHeVnKBvqh3FB2HYu7g2xseAZ5MlN6Kz/qnkASV8U=\" crossorigin=\"anonymous\"></script><script src=\"/static/js/{filename}mymap.js\" type=\"text/javascript\"></script>".format(filename=filename)+"{% endblock %}")
else:
    maphtmlcode=""
    othermapjs=""

with open("templates/"+filename+"form.html", "w") as myfile:
    myfile.write("{% extends 'base.html' %}{% block content %}"+formhtml+"<div class=\"actions\"><input type=\"submit\"/></div></form>" + "{% for x in "+filename+"s %}<p class=\"my"+myfavouriteitem+"\">{{"+ "x[\""+myfavouriteitem+"\"] }}</p>{% endfor %}"+maphtmlcode+"{% endblock %}{% block liens %}<a href=\"/\">bienvenue</a>"+"<a href=\"/add_one_{filename}\"> add one {filename}</a>".format(filename=filename)+"{% endblock %}"+othermapjs)



if filename == "user":
    with open("templates/"+filename+"login.html", "w") as myfile:
        myfile.write("{% extends 'base.html' %}{% block content %}<h1>signin</h1><form method=\"POST\"><div>\n<label>username</label><input name=\"username\"/><div>\n<label>username</label><input name=\"password\" type=\"password\"/></div><div class=\"actions\"><input type=\"submit\"/></div></form>" + "{% for x in "+filename+"s %}<p class=\"my"+myfavouriteitem+"\">{{"+ "x[\""+myfavouriteitem+"\"] }}</p>{% endfor %}"+"{% endblock %}{% block liens %}<a href=\"/\">bienvenue</a>"+"<a href=\"/add_one_{filename}\"> s'inscrire (add one {filename})</a>".format(filename=filename)+"{% endblock %}")
if "lat" in items and "lon" in items:
 
    mymap=open("./awesomemap.js","r")
    f=mymap.read().replace("{tablename}", filename)
    with open("static/js/"+filename+"mymap.js", "w") as myfile:
        myfile.write(f)


