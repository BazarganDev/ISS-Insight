# ISS-Insight
Real-Time International Space Station (ISS) Tracker with Python

A python script to fetch TLE data of the ISS (ZARYA) satellite, calculate its position, predict its orbit and visualize its trajectory on a map. before running the code, let me walk you through some important key concepts:

## Key Concepts
### What is a TLE?
A Two-Line Element Set (TLE) is a standardized format used to describe the orbit of a satellite. It consists of two lines of data that include important orbital parameters, such as the satellite's position, velocity, and other relevant information at a specific time known as the epoch. See ["Two-line-element set"](https://en.wikipedia.org/wiki/Two-line_element_set) Wikipedia article for more information.

### What is a Geocentric Position?
A geocentric position refers to a viewpoint or coordinate system that is centered on the Earth. In astronomy, it describes a model where the Earth is considered the center of the universe, with celestial bodies like the Sun and planets orbiting around it. See ["Earth-centered, Earth-fixed coordinate system"](https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system) and ["Geocentric model"](https://en.wikipedia.org/wiki/Geocentric_model) Wikipedia articles for more information.

### What is a Subpoint Position?
In Astronomy, the subpoint position (or subsatellite point) of a satellite refers to the point on the Earth's surface that is directly beneath the satellite at any given moment. It is defined by its geographical coordinates, latitude and longitude (See ["Geodesy for the Layman" by U.S. Geological Survey](https://www.ngs.noaa.gov/PUBS_LIB/Geodesy4Layman/TR80003D.HTM#ZZ9)).
