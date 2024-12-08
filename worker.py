import requests
import psycopg
from datetime import datetime
import logging

def fetch_data():
    # api_token = 'insert Api key'

    path = 'https://api.weather.gov/gridpoints/TOP/31,81/forecast' # + 'api_token' ....
    r = requests.get(path).json()
    data = r['properties']['periods']

    number = data[0]['number'] # number of the observation
    observation_time = data[0]['name']
    is_daytime = data[0]['isDaytime']
    temperature = data[0]['temperature']
    temperature_unit = data[0]['temperatureUnit']
    wind_speed = data[0]['windSpeed']
    wind_direction = data[0]['windDirection']
    icon_url = data[0]['icon']
    short_forecast = data[0]['shortForecast']
    detailed_forecast = data[0]['detailedForecast']


    # open db
    try:
        conn = psycopg.connect(dbname = 'weather', user = 'postgres', host = 'localhost', password = 'itsshowtime')
        print('Opened DB successfully')

    except:
        print(datetime.now(), "Unable to connect to the database")
        logging.exception("Unable to open the database")
        return
    else:
        # cur = conn.cursor(cursor_factory = psycopg.extras.DictCursor) # como sale en el video
        cur = conn.cursor()

    # write data into the DB
    cur.execute("""INSERT INTO station_reading(number, observation_time, is_daytime, temperature, temperature_unit, wind_speed, wind_direction, icon_url, short_forecast, detailed_forecast)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (number, observation_time, is_daytime, temperature,
                                                                         temperature_unit, wind_speed, wind_direction, icon_url, short_forecast, detailed_forecast))


    conn.commit()
    cur.close()
    conn.close()

    print("Data Written", datetime.now())


fetch_data()





