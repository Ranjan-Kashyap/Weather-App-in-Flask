import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=dc8b45026ce8014fa039ad267e449c6e'
        r = requests.get(url.format(city)).json()
        weather = {
                    'city': city,
                    'temperature': r['main']['temp'],
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                  }
        return render_template('index.html', weather=weather)
    else:
        return render_template('index.html')
            
if __name__ == '__main__':
    app.run(debug=True)