<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>


    <style>
      body{
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  background: #34495e;
}
.box{
  width: 300px;
  padding: 40px;
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translate(-50%,-50%);
  background: #f3eded;
  text-align: center;
}

.box h1{
  color: white;
  text-transform: uppercase;
  font-weight: 500;
}
.box input[type = "text"],.box input[type = "password"]{
  border:0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #3498db;
  padding: 14px 10px;
  width: 200px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
}
.box input[type = "text"]:focus,.box input[type = "password"]:focus{
  width: 280px;
  border-color: #2ecc71;
}
.box input[type = "submit"],.box input[type = "submit"]{
  border:0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #2ecc71;
  padding: 14px 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}
.box input[type = "submit"]:hover{
  background: #2ecc71;
}


.box2 input[type = "submit"],.box2 input[type = "submit"]{
  border:0;
  background: none;
  display: block;
  margin: 200px auto;
  text-align: center;
  border: 2px solid #2ecc71;
  padding: 14px 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}
.box2 input[type = "submit"]:hover{
  background: #2ecc71;
}
      </style>
    <meta charset="utf-8">
    <title>َAnimated Login Form</title>
    <link rel="stylesheet" type="text/css" href="{{url_for('static',filename='style.css')}}">
  </head>
  <body>

<form class="box" action="/log" method="POST">
  

  <h1 style="color: brown"> Analyse </h1>
  M / Ms {{utilisateur.Fonction}} {{utilisateur.Login}} .
  <h1>HEMATOLOGIE ( Sang Total )</h1>
				
			</div>


<br>Votre fonction: {{utilisateur.Fonction}} </br>
Identifiant: {{utilisateur.Id}} </br>
Sexe: {{utilisateur.Gender}} </br>
Age: {{utilisateur.Age}}</br>
<h1>Numeration Formule SANGUINE</h1>
Hématies {{utilisateur.Hématies}} T/I</br>
Hémoglobine {{utilisateur.Hémoglobine}} g/100 ml</br>
Hématocrite {{utilisateur.Hématocrite}}  % </br>
Lymphocytes K {{utilisateur.Lymphocytes}} </br>
TCMH {{utilisateur.TCMH}} pg </br>
CCMH {{utilisateur.CCMH}} g/100 ml </br>
Leucocytes {{utilisateur.Leucocytes}} G/I </br>
Poly Neutrophiles {{utilisateur.Neutrophiles}} % </br>
Lymphocytes {{utilisateur.Lymphocytes}} % </br>
<h1> Biochimie Sanguine</h1>
Creatininie {{utilisateur.Creatininie}} mg/i</br>
Potassium K {{utilisateur.Potassium}} </br>
MDRD {{utilisateur.Avaler}} ml/min/1.73 m</br>
<h1>Hormonologie Sanguine</h1>
TSH {{utilisateur.TSH}} mUI/L</br>

<h1> Resultat</h1>
Resultat Cancer {{utilisateur.Resultat}} </br>


  
</form>


<form class="box2" action="/out" method="POST">
  <input type="submit" name="retour2" value="logout"/>
</form>





  </body>
</html>
