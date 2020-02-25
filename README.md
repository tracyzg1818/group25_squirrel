# Django Squirrel Tracker
#### Group Project for IEOR_E4501 Tools for Analytics at Columbia University

## Technology
The project is created with:
* Django version: 3.0.3
* Python version: 3.6

## Table of Contents
* Web Page Functions
* Main Features
* Web Links

## Web Page Functions
Our project Squirrel_Tracker is a simple but useful tool to track information of squirrels in Central Park of NYC. Using **Django** web development framework, we develop an App called 'sightings', which has the following functions:

* View the positions of all the squirrels in the central park
* View descriptive statistics of squirrel attributes.
* Edit their attribute details
* Add new squirrel records

## Main Features
Here are the main features of the Squirrel Tracker:
  - Management Commands: 
      - Import_squirrel_data.py : a command that imports the data from the 2018 census file
      - Export_squirrel_data.py : a command that exports existing squirrel data in CSV format
  - View 1: 
      - a map that displays 100 squirrel coordinates
  - View 2: 
      - a view that lists all squirrel IDs with links to edit each 
  - View 3: 
      - a view to update a particular squirrel sighting
  - View 4: 
      - a view to add a new squirrel into the squirrel list
  - View 5: 
      - a view that shows general statistics about the squirrels

## Web Links
- To view the coordinates of squirrels: https://static-smoke-253520.appspot.com/map/
- To modify squirrel records in the database: https://static-smoke-253520.appspot.com/sightings/
