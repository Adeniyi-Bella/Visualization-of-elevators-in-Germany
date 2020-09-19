*** Vizualizing elevator service states at german railway stations

** Problem statement
Elevators are an essential mean to support pysically disabled persons accessing different levels in a built asset. Especially in railway stations, well-performing elevators are of high importance as they get used by a large

-number of passengers departuring or arriving with luggage. Due to high usage and the associated wear and tear, not all elevators are always in service and can assist travellers.

** Programming task

-Write a script that visualizes the service state of elevators at german railway stations.

-Grab the data representing the current state from https://data.deutschebahn.com/ and https://developer.deutschebahn.com/store/. Search for a suitable RESTful API about the elevator states.

-Query and extract the relevant data of all elevators.
Use the GeoPandas package to visualize all elevators in germany. You can also use GIS software. Show a green symbol if the elevator is in service, otherwise mark it red.

** Optional extensions

-Build a simple FLASK server around the data extraction and create an HTML frontend that shows the user additional information.
