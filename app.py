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
        """Welcome to the Climate Analysis API!<br/>"""
        f"Available Routes:<br/>" 
        
        f"/api/v1.0/precipitation<br/>" 
        
        f"/api/v1.0/stations <br/>" 
        
        f"/api/v1.0/tobs<br/>" 
        
        f"/api/v1.0/temp/start/end"
        )

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
    return jsonify(stations)

# create a new temperature route
@app.route("/api/v1.0/tobs")
# create the temp_monthly() function 
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.date>=prev_year).\
    filter(Measurement.station == 'USC00519281').all()
    temps = list(np.ravel(results))
    return jsonify(data=temps)

# create routes for temperatures statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        results=session.query(*sel).\
            filter(Measurement.date>=start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    
    results = session.query(*sel).filter(Measurement.date >=start).filter(Measurement.date <=end).all()
    temps = list(np.ravel(results))

    return jsonify(temps)

if __name__ == "__main__":
    app.run(debug=True)



