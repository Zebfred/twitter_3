from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests 
import openaq

api = openaq.OpenAQ()
#>>> status, body = api.cities()
#>>> status

def create_app():
    app = Flask(__name__)

    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    #stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#have the database know about the app
DB.init_app(app)

#DB = SQLAlchemy(APP)


@APP.route('/', methods = ["GET"])

#function
def root():
    re_str = ''
    cities = Record.query.filter(Record.value >= 10).all()

    for data in cities:
        at_risk = re_str + str(data) + '<br />'
    return '<body>' + re_str + '</body>'
    """Base view."""
    return str(at_risk)



'''        r=requests.get('https://dog.ceo/api/breeds/image/random/'+str(number))
    else:
        raise ValueError('Max Number of Dogs Returned is 50')
    pics=r.json()['message']
    return pics
'''



#second route
@APP.route("/part2")
 
#function for 2nd risk    
def city_list():
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    date_value = [(body.get('results')[n].get('date').get('utc'),body.get('results')[n].get('value')) for n in range(0,100)]

    
''' 
def listCities():
    r=requests.get('https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25')
    b=r.json()
    cities=[]

    for key, value in b['message'].items():
        if len(value)==0:
            cities.append(key)
        else:
            for city in value:
                full= city + ' ' + key
                cities.append(full)
    return cities
'''



class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return 'TODO - write a nice representation of Records'


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    DB.session.commit()
    return 'Data refreshed!'



if __name__ == "__main__":
    APP.run()
