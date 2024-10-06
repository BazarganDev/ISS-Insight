# ISS-Insight
Real-Time International Space Station (ISS) Tracker with Python

A python script to fetch TLE data of the ISS (ZARYA) satellite, calculate its position, predict its orbit and visualize its trajectory on an interactive map. Thanks to [Celestrak](https://celestrak.org/) We can access to the TLE data of satellites, including International Space Station. before running the code, let me walk you through some important key concepts. I'm indeed not a specialist in satellites though, therefore I will provide these information with their sources. Please take your time and read these concepts. By understanding these concepts, you will understand the logic behind the script very easily:

## Key Concepts
### What is a TLE?
A Two-Line Element Set (TLE) is a standardized format used to describe the orbit of a satellite. It consists of two lines of data that include important orbital parameters, such as the satellite's position, velocity, and other relevant information at a specific time known as the epoch (Source: ["Two-line-element set"](https://en.wikipedia.org/wiki/Two-line_element_set)).

### What is a Geocentric Position?
A geocentric position refers to a viewpoint or coordinate system that is centered on the Earth. In astronomy, it describes a model where the Earth is considered the center of the universe, with celestial bodies like the Sun and planets (or even satellites) orbiting around it (Source: ["Earth-centered, Earth-fixed coordinate system"](https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system) and ["Geocentric model"](https://en.wikipedia.org/wiki/Geocentric_model)).

### What is a Subpoint Position?
In Astronomy, the subpoint position (or subsatellite point) of a satellite refers to the point on the Earth's surface that is directly beneath the satellite at any given moment. It is defined by its geographical coordinates, latitude and longitude (Source: ["Geodesy for the Layman" by U.S. Geological Survey](https://www.ngs.noaa.gov/PUBS_LIB/Geodesy4Layman/TR80003D.HTM#ZZ9)). This point is significant because it represents the satellite's ground track, which is the path that the satellite appears to trace over the Earth's surface as it orbits (Source: ["Satellite Communications" by Dennis Roddy](https://books.google.com/books/about/Satellite_Communications_Fourth_Edition.html?id=2KEt_hFyjwgC)).

### What is International Date Line (IDL)?
The International Date Line is an imaginary line that runs from the North Pole to the South Pole, primarily along the 180th meridian in the Pacific Ocean. It serves as the boundary between two consecutive calendar dates, meaning when you cross it, you either gain or lose a day depending on the direction you are traveling (Source: ["The international date line, explained"](https://www.livescience.com/44292-international-date-line-explained.html) and ["International Date Line"](https://www.britannica.com/topic/International-Date-Line)).

## A very important block of code
I can tell that by far the most important part of the code is this block below:
```python3
orbit_coordinates = [(sat_lan, sat_lon)]
if abs(future_sat_lon - orbit_coordinates[-1][1]) > 180:
    future_sat_lon += 360 if future_sat_lon < orbit_coordinates[-1][1] else -360
```
### Code Breakdown
- Line 1: The `orbit_coordinates` list holds the trajectory points.
- Line 2: `future_sat_lon` variable represents the future longitude of the ISS at a specific time and `orbit_coordinates[-1][1]` accesses the last recorded longitude from a list of previous coordinates. This line calculates the absolute difference between the current future longitude (`future_sat_lon`) and the last recorded longitude. If this difference exceeds 180 degrees, it indicates that the satellite has crossed the IDL.
- Line 3: If `future_sat_lon` is less than the last recorded longitude, it indicates that the satellite has crossed from the eastern hemisphere to the western hemisphere (or vice versa). To correct this jump: 1) If `future_sat_lon` is less than `orbit_coordinates[-1][1]`, it adds 360 degrees to `future_sat_lon`, effectively wrapping it around from negative to positive. 2) If `future_sat_lon` is greater, it subtracts 360 degrees, bringing it back into the range of -180 to +180.

### Why does it matter?
When tracking a satellite's position over time, you may encounter situations where the longitude values can "jump" significantly due to the way longitude is measured. Longitude is expressed in degrees, ranging from -180 to +180 or 0 to 360. The International Date Line (IDL) is located at approximately 180 degrees longitude. Crossing this line can cause a sudden change in the longitude value, which can be problematic for visualizing paths on a map. In general, handling the IDL problem matters in terms of:
- Visualization: If you don't adjust for these jumps, the path drawn on a map could appear discontinuous or erratic, making it difficult to understand the satellite's actual trajectory.
- Data Integrity: Ensuring that longitude values are consistent helps maintain data integrity, especially when plotting or analyzing satellite paths.

## Libraries
Required libraries:
- `Skyfield` ([Documentation](https://rhodesmill.org/skyfield/)) for satellite data processing
- `Folium` ([Documentation](https://python-visualization.github.io/folium/latest/index.html)) for mapping
- `Selenium` ([Documentation](https://www.selenium.dev/documentation/)) for automation
- `Datetime` ([Documentation](https://docs.python.org/3/library/datetime.html)) for retrieving UTC date and time
- `Time` ([Documentation](https://docs.python.org/3/library/time.html)) for timing

## Running the Script
- Clone the project (It is recommended to clone it to the Desktop)
`git clone https://github.com/BazarganDev/ISS-Insight.git`
- Install required modules
`pip install -r requirements.txt`
- Run the script and wait for the map to launch
`python3 tracker.py`

## Output
![Screenshot_1](https://github.com/user-attachments/assets/1027863f-fe7a-46ee-abb6-daef4b6a12a3)
![Screenshot_2](https://github.com/user-attachments/assets/4ee308a3-41b1-4bb0-b02a-e394f090444b)

## Updates
The project still have some room for improvement. So if you have any thoughts to improve the source code, feel free to create a pull request. If you have any suggestions or thinking about collaboration, let me know in the issues section.
