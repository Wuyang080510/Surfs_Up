import datetime as dt
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#setup database engine
engine=create_engine('sqlite:///hawaii.sqlite')
#reflect the database
Base=automap_base()
Base.prepare(engine, reflect=True)
#save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
#create a session link
session = Session(engine)
#setup Flask
app = Flask(__name__)
# add a root route
@app.route("/")
# add routing information for each of the other routes
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        
        Available Routes:
        
        /api/v1.0/precipitation
        
        /api/v1.0/stations
        
        /api/v1.0/tobs
        
        /api/v1.0/temp/start/end
        
        ''')

# create a new precipitation route
@app.route("/api/v1.0/precipitation")
# create the precipitation() function
def precipitation():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
                    filter(Measurement.date>=prev_year).all()
    # create a dictionary 
    precip = {date:prcp for date, prcp in precipitation}
    return jsonify(precip)
# create a new stations route
@app.route("/api/v1.0/stations")
# create the stations() function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
    
# def hello_world():
#     return 'Hello World'

# # <h1> Welcome to my website </h1>

# temperature = float(input("What is the temperature right now?"))

# def temp_warning(temperature):
#     if temperature >= 90:
#         print('High temperature warning')
#     elif temperature < 90 and temperature >=65: 
#         print('It is the right time to go out!')
#     else:
#         print('Too cold to go out!')
# temp_warning(temperature)