# ISS Insight 🛰️
Real-Time International Space Station (ISS) Tracker with Python

A Python script that fetches TLE data of the ISS (ZARYA) satellite, calculates its position, predicts its orbit and visualizes its trajectory on an interactive map. Thanks to [Celestrak](https://celestrak.org/) We can access to the TLE data of satellites, including International Space Station.

If you are curious about the project or interested, read more on the blog: [Project: ISS Insight](https://bazargandev.github.io/iss_insight.html)

## Libraries
Required libraries:
- `Skyfield` ([Documentation](https://rhodesmill.org/skyfield/))
- `Folium` ([Documentation](https://python-visualization.github.io/folium/latest/index.html))
- `Selenium` ([Documentation](https://www.selenium.dev/documentation/))
- `Datetime` ([Documentation](https://docs.python.org/3/library/datetime.html))
- `Time` ([Documentation](https://docs.python.org/3/library/time.html))
- `OS` ([Documentation](https://docs.python.org/3/library/os.html))

## Running the Script
- Clone the project
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

## To-Do
- [X] Fix bugs
- [ ] Add docstring for each function
