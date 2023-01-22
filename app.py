from flask import Flask , render_template
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db = SQLAlchemy(app)

class city(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(50))

@app.route('/')
def index():   
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c3ff3a97703002f33ed37f7ef07b814f'
    city = 'Mumbai'
    r = requests.get(url.format(city)).json()
    
    
    weather = {
        'city': city,
        'temprature': r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
        }
    print(weather)
    return render_template('weather.html')
    



if __name__ == "__main__":
    app.run()