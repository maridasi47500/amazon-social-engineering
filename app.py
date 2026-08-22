from flask import Flask, render_template, request, session, redirect
from myplace import Myplace
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
@app.route("/add_one_personne", methods=["GET","POST"])
def add_one_personne():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslespays_region_linguistique= query_db("select * from pays_region_linguistique")

        one_user = query_db("insert into personne (hack_id,pic,nomcomplet,prenom,nomfamille,suffixe,titre,fm,phone,email,pays_region_linguistique_id,description) values (:hack_id,:pic,:nomcomplet,:prenom,:nomfamille,:suffixe,:titre,:fm,:phone,:email,:pays_region_linguistique_id,:description)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from personne')


        return render_template("personneform.html", personnes=user, one_user=one_user, the_title="add new personne", touslespays_region_linguistique=touslespays_region_linguistique)


    touslespays_region_linguistique= query_db("select * from pays_region_linguistique")

    user = query_db('select * from personne')
    one_user = query_db("select * from personne limit 1", one=True)
    return render_template("personneform.html", personnes=user, one_user=one_user, the_title="add new personne", touslespays_region_linguistique=touslespays_region_linguistique)

@app.route("/add_one_pays_region_linguistique", methods=["GET","POST"])
def add_one_pays_region_linguistique():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into pays_region_linguistique (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from pays_region_linguistique')


        return render_template("pays_region_linguistiqueform.html", pays_region_linguistiques=user, one_user=one_user, the_title="add new pays_region_linguistique")


    user = query_db('select * from pays_region_linguistique')
    one_user = query_db("select * from pays_region_linguistique limit 1", one=True)
    return render_template("pays_region_linguistiqueform.html", pays_region_linguistiques=user, one_user=one_user, the_title="add new pays_region_linguistique")

@app.route("/add_one_format_de_message", methods=["GET","POST"])
def add_one_format_de_message():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslespersonne= query_db("select * from personne")

        one_user = query_db("insert into format_de_message (personne_id,texte,description) values (:personne_id,:texte,:description)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from format_de_message')


        return render_template("format_de_messageform.html", format_de_messages=user, one_user=one_user, the_title="add new format_de_message", touslespersonne=touslespersonne)


    touslespersonne= query_db("select * from personne")

    user = query_db('select * from format_de_message')
    one_user = query_db("select * from format_de_message limit 1", one=True)
    return render_template("format_de_messageform.html", format_de_messages=user, one_user=one_user, the_title="add new format_de_message", touslespersonne=touslespersonne)

@app.route("/add_one_company", methods=["GET","POST"])
def add_one_company():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry_region_linguistique= query_db("select * from country_region_linguistique")

        one_user = query_db("insert into company (name,country_region_linguistique_id) values (:name,:country_region_linguistique_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from company')


        return render_template("companyform.html", companys=user, one_user=one_user, the_title="add new company", touslescountry_region_linguistique=touslescountry_region_linguistique)


    touslescountry_region_linguistique= query_db("select * from country_region_linguistique")

    user = query_db('select * from company')
    one_user = query_db("select * from company limit 1", one=True)
    return render_template("companyform.html", companys=user, one_user=one_user, the_title="add new company", touslescountry_region_linguistique=touslescountry_region_linguistique)

@app.route("/add_one_texte_reseau_sociaux", methods=["GET","POST"])
def add_one_texte_reseau_sociaux():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslespersonne= query_db("select * from personne")

        one_user = query_db("insert into texte_reseau_sociaux (nom_social_media,personne_id,content) values (:nom_social_media,:personne_id,:content)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from texte_reseau_sociaux')


        return render_template("texte_reseau_sociauxform.html", texte_reseau_sociauxs=user, one_user=one_user, the_title="add new texte_reseau_sociaux", touslespersonne=touslespersonne)


    touslespersonne= query_db("select * from personne")

    user = query_db('select * from texte_reseau_sociaux')
    one_user = query_db("select * from texte_reseau_sociaux limit 1", one=True)
    return render_template("texte_reseau_sociauxform.html", texte_reseau_sociauxs=user, one_user=one_user, the_title="add new texte_reseau_sociaux", touslespersonne=touslespersonne)

@app.route("/add_one_texte_reseau_sociaux_company", methods=["GET","POST"])
def add_one_texte_reseau_sociaux_company():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescompany= query_db("select * from company")

        one_user = query_db("insert into texte_reseau_sociaux_company (nom_social_media,company_id,content) values (:nom_social_media,:company_id,:content)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from texte_reseau_sociaux_company')


        return render_template("texte_reseau_sociaux_companyform.html", texte_reseau_sociaux_companys=user, one_user=one_user, the_title="add new texte_reseau_sociaux_company", touslescompany=touslescompany)


    touslescompany= query_db("select * from company")

    user = query_db('select * from texte_reseau_sociaux_company')
    one_user = query_db("select * from texte_reseau_sociaux_company limit 1", one=True)
    return render_template("texte_reseau_sociaux_companyform.html", texte_reseau_sociaux_companys=user, one_user=one_user, the_title="add new texte_reseau_sociaux_company", touslescompany=touslescompany)

@app.route("/add_one_activities", methods=["GET","POST"])
def add_one_activities():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslespersonne= query_db("select * from personne")

        one_user = query_db("insert into activities (personne_id,name) values (:personne_id,:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from activities')


        return render_template("activitiesform.html", activitiess=user, one_user=one_user, the_title="add new activities", touslespersonne=touslespersonne)


    touslespersonne= query_db("select * from personne")

    user = query_db('select * from activities')
    one_user = query_db("select * from activities limit 1", one=True)
    return render_template("activitiesform.html", activitiess=user, one_user=one_user, the_title="add new activities", touslespersonne=touslespersonne)

@app.route("/add_one_human_traits", methods=["GET","POST"])
def add_one_human_traits():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into human_traits (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from human_traits')


        return render_template("human_traitsform.html", human_traitss=user, one_user=one_user, the_title="add new human_traits")


    user = query_db('select * from human_traits')
    one_user = query_db("select * from human_traits limit 1", one=True)
    return render_template("human_traitsform.html", human_traitss=user, one_user=one_user, the_title="add new human_traits")

@app.route("/add_one_hack", methods=["GET","POST"])
def add_one_hack():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into hack (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from hack')


        return render_template("hackform.html", hacks=user, one_user=one_user, the_title="add new hack")


    user = query_db('select * from hack')
    one_user = query_db("select * from hack limit 1", one=True)
    return render_template("hackform.html", hacks=user, one_user=one_user, the_title="add new hack")

@app.route("/add_one_hackhavehumantraits", methods=["GET","POST"])
def add_one_hackhavehumantraits():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        tousleshack= query_db("select * from hack")

        tousleshuman_traits= query_db("select * from human_traits")

        one_user = query_db("insert into hackhavehumantraits (hack_id,human_traits_id) values (:hack_id,:human_traits_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from hackhavehumantraits')


        return render_template("hackhavehumantraitsform.html", hackhavehumantraitss=user, one_user=one_user, the_title="add new hackhavehumantraits", tousleshack=tousleshack, tousleshuman_traits=tousleshuman_traits)


    tousleshack= query_db("select * from hack")

    tousleshuman_traits= query_db("select * from human_traits")

    user = query_db('select * from hackhavehumantraits')
    one_user = query_db("select * from hackhavehumantraits limit 1", one=True)
    return render_template("hackhavehumantraitsform.html", hackhavehumantraitss=user, one_user=one_user, the_title="add new hackhavehumantraits", tousleshack=tousleshack, tousleshuman_traits=tousleshuman_traits)

