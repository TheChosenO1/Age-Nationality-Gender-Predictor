from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("index.html")


@app.route("/guess/<name>")
def age_gender_guessr(name):
    response1 = requests.get(f'https://api.agify.io?name={name}')
    content1 = response1.json()
    age = content1['age']
    response2 = requests.get(f'https://api.genderize.io?name={name}')
    content2 = response2.json()
    gender = content2['gender']
    response3 = requests.get(f'https://api.nationalize.io?name={name}')
    content3 = response3.json()
    nation = content3['country'][0]['country_id']
    response4 = requests.get(f'https://restcountries.eu/rest/v2/alpha/{nation}')
    content4 = response4.json()
    nationality = content4['name']
    return render_template("agify_genderize_index.html", name=name, age=age, gender=gender, nation=nationality)


if __name__ == "__main__":
    app.run(debug=True)
