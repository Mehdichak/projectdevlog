import requests

URL1 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&q=date_heure%3E%3D%222020-05-30T22:00:00Z%22&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
r = requests.get(URL1)
print(r)
open("LongTermData.csv","wb").write(r.content)

URL2 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
r = requests.get(URL2)
print(r)
open("ShortTermData.csv","wb").write(r.content)