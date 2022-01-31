
from urllib import response
import flask  
import json
from flask.globals import session
from flask.helpers import url_for
from flask import redirect, url_for , globals , make_response
from app import app
from flask import render_template
from flask import request
import json
from json2html import *
import sqlite3
import pdfkit


app.secret_key = "hello"



def db():
    with open('medecin.json') as f:
        data = json.load(f)
    return data
    


    

def db2():
    with open('patient.json') as f:
        data2 = json.load(f)
    return data2

@app.route('/log_pat', methods = ['POST'])  
def cnx_patient():
    if request.method == 'POST':
        login = request.form['login']
        mdp= request.form['mdp']
        nom = request.form['nom']
        prenom= request.form['prenom']
        age = request.form['age']
        gender = request.form['gender']
        nationality = request.form['nationalité']
        adresse= request.form['Adresse']
        identity = request.form['identité']
        vitale= request.form['vitale']
        phone= request.form['Phone']
        user={"login":login,"mdp":mdp,"nom": nom,"prenom": prenom,"age": age,"gender": gender,"nationalité": nationality,"Adresse": adresse,"identité": identity,"vitale": vitale,"Phone": phone}
        data2=db2()
        if login in data2 and mdp==data2[login]["mdp"]:
            return render_template('user2.html', utilisateur=user)
        else:
            
            
            return render_template('erreur.html', title='Erreur', utilisateur=user)

#@app.route('/log', methods = ['POST'])  
#def cnx_Medecin_sql():

  
 #   login = flask.request.form.get('login')
  #  mdp = flask.request.form.get('mdp')
   # user = {"login":login,"MDP":mdp}
    #with sqlite3.connect("med.db") as con:
     #   cur = con.cursor()
      #  res = cur.execute("SELECT* FROM med where Login= ?;", [login])
        #con.commit() #fonction qui inscrit ce qu'on a mis dans le curseur
    
       # rows = res.fetchall(); 
            
            
        #user={"Id": rows[0][0], "MDP":rows[0][1], "login": rows[0][2]}
        #if rows: 
            #if rows[0][2]==login: 
           #     return render_template('user.html', title='Sign in',utilisateur=user)
          #  if login == "":
         #       return render_template('erreur.html', title='Erreur') 

        #con.close()

        # connexion medecin avec JSON 

@app.route('/log', methods = ['POST'])  
def cnx_medecin():
    if request.method == 'POST':
        login = request.form['login']
        mdp= request.form['mdp']
        user={"login":login,"mdp":mdp}
        data=db()
        if login in data and mdp==data[login]["mdp"]:
            return render_template('user.html', utilisateur=user)
        else:
            
            
            return render_template('erreur.html', title='Erreur', utilisateur=user)
    


@app.route('/')
def index():
    return render_template('in1.html')



#inscription medecin avec sql 
#@app.route('/inscri2', methods=['POST'])
#def inscription_medecin_sql():
  
    #login = flask.request.form.get('login')
    #mdp = flask.request.form.get('mdp')
    #with sqlite3.connect("med.db") as con:
      #  cur = con.cursor()
     #   cur.execute("INSERT INTO med(login, MDP) VALUES (?,?)", (login,mdp))
        #con.commit() #fonction qui inscrit ce qu'on a mis dans le curseur
    #con.close()
     
    #return render_template('index2.html', title='Sign in')
    
# Inscription medecin avec json
@app.route('/inscri2', methods=['POST'])
def inscription_medecin():
  
    if request.method != 'POST':
        return
    login = request.form['login']
    mdp= request.form['mdp']
    confirm = request.form['mdp2']
    infos={"login":login,"mdp":mdp,"mdp2":confirm}
    if 'user' in session:
        session['user']=login
    if confirm!="" and confirm== mdp:
        with open('medecin.json','r') as f1:
            users=json.load(f1)
        users[login]={"login": login,"mdp": mdp}
        
        with open('medecin.json','w') as f2:
            json.dump(users, f2, indent=4)
        print("Inscription réalisée avec succès")

        return render_template('index2.html', title='Sign in', utilisateur=infos)
    else:
        return render_template('erreur.html', title='Erreur')


@app.route('/inscri2_pat', methods=['POST'])
def inscription_patient_json():
  
    if request.method != 'POST':
        return
    login = request.form['login']
    mdp= request.form['mdp']
    confirm = request.form['mdp2']
    infos={"login":login,"mdp":mdp,"mdp2":confirm}
    if 'user' in session:
        session['user']=login
    if confirm!="" and confirm== mdp:
        with open('patient.json','r') as f1:
            users=json.load(f1)
        users[login]={"login": login,"mdp": mdp}
        
        with open('patient.json','w') as f2:
            json.dump(users, f2, indent=4)
        print("Inscription réalisée avec succès")

        return render_template('login_pat.html', title='Sign in', utilisateur=infos)
    else:
        return render_template('erreur.html', title='Erreur')
        
    

         

@app.route('/page', methods = ['POST'])
def identification():
    if request.method == 'POST':
        login = request.form['login']
        pswd = request.form['pswd']
        user = {"login":login,"pswd":pswd}  
        
        if 'submit' in request.form:
            with sqlite3.connect("Sick_BD.db") as con:
                cur = con.cursor()
            res= cur.execute("SELECT* FROM SANG where Login= ?;", [login])
            rows = res.fetchall(); 
            
            
            user={"Id": rows[0][0], "Gender":rows[0][1], "Age": rows[0][2], "Yellow_fingers": rows[0][3], "Anxiety": rows[0][4], "Fatigue": rows[0][5], "Allergy": rows[0][6], "Respiration": rows[0][7], "Alcool": rows[0][8], "Toux":rows[0][9], "Smoking":rows[0][10], "Chronic_disease": rows[0][11], "Essouflement":rows[0][12], "Avaler":rows[0][13],"Douleur_thoracique":rows[0][14], "Cancer_des_poumons":rows[0][15], "Login":rows[0][16], "Fonction": rows[0][18]}
            if rows: 
                if rows[0][16]==login:
                    return render_template('ana.html', title='Réussi', utilisateur=user)
                return render_template('erreur.html', title='Erreur', utilisateur=user)
            con.close()
            
        
            
@app.route('/Recherche', methods = ['POST'])
def identification_med():
    if request.method == 'POST':
        login = request.form['login']
        pswd = request.form['pswd']
        user = {"login":login,"pswd":pswd}  
        
        if 'submit' in request.form:
            with sqlite3.connect("Sick_BD.db") as con:
                cur = con.cursor()
            res= cur.execute("SELECT* FROM SANG where Login= ?;", [login])
            rows = res.fetchall(); 
            
            
            user={"Id": rows[0][0], "Gender":rows[0][1], "Age": rows[0][2], "Yellow_fingers": rows[0][3], "Anxiety": rows[0][4], "Fatigue": rows[0][5], "Allergy": rows[0][6], "Respiration": rows[0][7], "Alcool": rows[0][8], "Toux":rows[0][9], "Smoking":rows[0][10], "Chronic_disease": rows[0][11], "Essouflement":rows[0][12], "Avaler":rows[0][13],"Douleur_thoracique":rows[0][14], "Cancer_des_poumons":rows[0][15], "Login":rows[0][16], "Fonction": rows[0][18]}
            if rows: 
                if rows[0][16]==login:
                    return render_template('ana.html', title='Réussi', utilisateur=user)
                return render_template('erreur.html', title='Erreur', utilisateur=user)
            con.close()
            
    
        
@app.route('/ins', methods=['POST'])
def inscrip_med():
    return render_template('index3.html')

@app.route('/ins_patt', methods=['POST'])
def inscrip_pat():
    return render_template('ins_pat.html')


@app.route('/an', methods=['POST'])
def pts2():
    return render_template('pt.html')

@app.route('/ins_pat2', methods=['POST'])
def in_pt():
    return render_template('ins_pat.html')


@app.route("/user")
def user():
    if "user" in session:
        global login
        login = session["user"]
    return  render_template("user.html")

         
   

    
@app.route('/retour', methods = ['POST'])
def retoure():
    
    return render_template("index2.html")

@app.route('/ret', methods = ['POST'])
def retoure2():
    
    return render_template("index2.html")

@app.route('/med', methods = ['POST'])
def medecin():
    
    return render_template("index2.html")

@app.route('/pat', methods = ['POST'])
def loginpatient():
    
    return render_template("login_pat.html")

@app.route('/show', methods = ['POST'])
def show():
    
    return render_template("data2.html")

@app.route('/cor', methods = ['POST'])
def show2():
    
    return render_template("data4.html")

@app.route('/analyse', methods = ['POST'])
def analyse():
    
    return render_template("recherche.html")
    
@app.route('/ps', methods = ['POST'])
def succ():
    
    return render_template("login_pat.html")

@app.route('/ps1', methods = ['POST'])
def succ2():
    
    return render_template("index2.html")


@app.route('/an', methods = ['POST'])
def analyse_show():
    
    return render_template("pt.html")

@app.route('/ok', methods = ['POST'])
def ok_1():
    
    return render_template("in1.html")



@app.route('/form_pat', methods = ['POST'])
def form_patient():
    
    return render_template("patient_formulaire.html")



@app.route('/quitter', methods = ['POST'])
def pas_info():
     if request.method != 'POST':
        return
     with open ("/Users/administrateur/Episen/flask_API/api_session+json/projet/patient_info.json") as f:
         d = json.load(f)
         scanOutput = json2html.convert(json=d)
         htmlReportFile ="/Users/administrateur/Episen/flask_API/api_session+json/projet/app/templates/data2.html"
         with open(htmlReportFile, 'w') as htmlfile:
             htmlfile.write(str(scanOutput))
             print("success")
    
     return render_template("in1.html")


@app.route('/send', methods = ['POST'])
def analyse_patt():
     if request.method != 'POST':
        return
     with open ("/Users/administrateur/Episen/flask_API/api_session+json/projet/analyse.json") as f:
         d = json.load(f)
         scanOutput = json2html.convert(json=d)
         htmlReportFile ="/Users/administrateur/Episen/flask_API/api_session+json/projet/app/templates/data3.html"
         with open(htmlReportFile, 'w') as htmlfile:
             htmlfile.write(str(scanOutput))
             print("success")
    
     return render_template("in1.html")
       
@app.route('/cor1', methods = ['POST'])
def cor_patient():
     if request.method != 'POST':
        return
     with open ("/Users/administrateur/Episen/flask_API/api_session+json/projet/patient.json") as f:
         d = json.load(f)
         scanOutput = json2html.convert(json=d)
         htmlReportFile ="/Users/administrateur/Episen/flask_API/api_session+json/projet/app/templates/data4.html"
         with open(htmlReportFile, 'w') as htmlfile:
             htmlfile.write(str(scanOutput))
             print("success")
    
     return render_template("conv.html")

@app.route('/out', methods = ['POST'])
def logout():
    session.clear()
    if 'user' in session:
         session.pop("user", None)
    return render_template("index2.html")



@app.route('/patient1', methods=['POST'])
def patient():
  
    if request.method != 'POST':
        return
    nom = request.form['nom']
    prenom= request.form['prenom']
    age = request.form['age']
    gender = request.form['gender']
    nationality = request.form['nationalité']
    adresse= request.form['adresse']
    identity = request.form['identité']
    vitale= request.form['vitale']
    phone= request.form['Phone']
    with open('patient_info.json','r') as f1:
        users=json.load(f1)
    users["users"].append({"nom": nom,"prenom": prenom,"age": age,"gender": gender,"nationalité": nationality,"adresse": adresse,"identité": identity,"vitale": vitale,"Phone": phone})
        
    with open('patient_info.json','w') as f2:
        json.dump(users, f2, indent=4)
    print("Inscription réalisée avec succès")

    return render_template('success.html', title='Sign in')


@app.route('/analyse_patt', methods=['POST'])
def patient_information():
  
    if request.method != 'POST':
        return
    nom = request.form['nom']
    prenom= request.form['prenom']
    age = request.form['age']
    gender = request.form['gender']
    nationality = request.form['nationalité']
    city= request.form['Adresse']
    identity = request.form['identité']
    vitale= request.form['vitale']
    phone= request.form['Phone']
    
    users = {"nom": nom,"prenom": prenom,"age": age,"gender": gender,"nationalité": nationality,"Adresse": city,"identité": identity,"vitale": vitale,"Phone": phone}
     
    with open('analyse.json','w') as f2:
        json.dump(users, f2, indent=4)
    print("Inscription réalisée avec succès")

    return render_template('success_pat.html', title='Sign in')




    