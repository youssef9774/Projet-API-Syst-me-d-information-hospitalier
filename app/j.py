import json
from json2html import *
with open ("/Users/administrateur/Episen/flask_API/api_session+json/projet/patient_info.json") as f:
    d = json.load(f)
    scanOutput = json2html.convert(json=d)
    htmlReportFile ="/Users/administrateur/Episen/flask_API/api_session+json/projet/app/templates/data2.html"
    with open(htmlReportFile, 'w') as htmlfile:
        htmlfile.write(str(scanOutput))
        print("success")