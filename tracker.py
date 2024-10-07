""" Project Description

ISS Insight: Real-Time International Space Station Tracker

This script tracks the International Space Station (more specifically, it tracks ZARYA module of the ISS)
and displays its current position by visualizing its trajectory on the map.
It also predicts the ISS's orbit for the next 90 minutes.

Author: Mohammad Bazargan
Source: https://github.com/BazarganDev/ISS-Insight
"""

# Import necessary modules
from datetime import datetime, timedelta
from skyfield.iokit import parse_tle_file
from skyfield.api import load, Topos
from selenium import webdriver
import folium
import time
import os



# Constants
TLE_FILENAME = "data_files/iss_zarya_tle.tle"
TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE"
MAP_FILENAME = "map/tracker_map.html"
MAP_ZOOM_START = 2
ORBIT_DURATION_MINUTES = 90
UPDATE_INTERVAL_SECONDS = 60

# Initialize a timescale object to handle time-related calculations.
time_scale = load.timescale()

# If the ISS (ZARYA) TLE file is missing and is outdated, download the latest data.
tle_filename = "data_files/iss_zarya_tle.tle"
url = "https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE"

if not load.exists(tle_filename) or load.days_old(tle_filename) > 1.0:
    try:
        load.download(url, filename=tle_filename)
    except:
        print("ERROR: Failed to download the TLE data.\nQuitting the program.")
        quit()

# Loading satellite data from the TLE file.
with load.open(tle_filename) as f:
    satellites = list(parse_tle_file(f, time_scale))

# Index ISS (ZARYA) by NORADID number.
satellite = {sat.model.satnum: sat for sat in satellites}[25544]

############################################################################################

# Create a blank map and save it as an HTML file.
folium.Map(location=[0,0], zoom_start=2).save("map/tracker_map.html")

# Launch a local browser (in this case, Firefox).
driver = webdriver.Firefox()

# Load the blank map.
try:
    driver.get("file:///home/mammadbaz/Desktop/ISS Insight/map/tracker_map.html")
except:     # I made sure that this error wont be occurred by creating an empty map.
    print("ERROR: Map file does not exists.\n")
    quit()

# Auto Tracking
# Continuously update the satellite's position and pinpoint its position on the map.
while True:
    # Get current UTC time.
    t_now = datetime.utcnow()
    t = time_scale.utc(t_now.year, t_now.month, t_now.day, t_now.hour, t_now.minute, t_now.second)

    # Calculate current satellite position.
    geocentric_pos = satellite.at(t)        # Geocentric Position: Position of the satellite in the vincity of the Earth from its center of mass.
    sub_pos = geocentric_pos.subpoint()     # Subpoint Position: Position of the satellite projected onto the Earth's surface.
    sat_lat = sub_pos.latitude.degrees      # Satellite Latitude
    sat_lon = sub_pos.longitude.degrees     # Satellite Longitude

    # Create a new map.
    iss_map = folium.Map(location=[sat_lat, sat_lon], zoom_start=2)

    # Pinpoint the satellite's current position on the map.
    folium.Marker(location=[sat_lat, sat_lon], tooltip=f"ISS (Lat: {sat_lat}, Lon: {sat_lon})", popup="International Space Station (ZARYA)", icon=folium.Icon(color="red", icon="satellite", prefix="fa")).add_to(iss_map)

    orbit_coordinates = [(sat_lat, sat_lon)]
    for i in range(1, 91):      # ISS completes one orbit around the Earth in approximately 90 minutes.
        # Predict the orbit of the satellite by predicting its future poitions.
        future_time = t + timedelta(minutes=i)
        future_geocentric_pos = satellite.at(future_time)
        future_sub_pos = future_geocentric_pos.subpoint()
        future_sat_lat = future_sub_pos.latitude.degrees
        future_sat_lon = future_sub_pos.longitude.degrees
        # Longitude Adjustment
        # Check for large jumps in longitude, handling the International Date Line (IDL) problem.
        if abs(future_sat_lon - orbit_coordinates[-1][1]) > 180:
            future_sat_lon += 360 if future_sat_lon < orbit_coordinates[-1][1] else -360
		# Add the fixed coordinates to the list of orbit coordinates.
        orbit_coordinates.append((future_sat_lat, future_sat_lon))

    # Connect the predicted coordinates to each other to create the orbit.
    folium.PolyLine(locations=orbit_coordinates, color="black", weight=1, dash_array="5").add_to(iss_map)
    iss_map.save("map/tracker_map.html")      # Save the map in HTML format.
    driver.refresh()
    time.sleep(60)		# Update the map every minute.

driver.close()
