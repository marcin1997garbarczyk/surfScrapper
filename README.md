# Surfscrapper - Surf Forecast Algarve

The Surf Forecast Algarve project allows users to check surfing conditions along the coast of Portugal, particularly in the Algarve region. The program retrieves data from SurfForecast.com to provide up-to-date information on various surfing spots. (https://www.surf-forecast.com/breaks/Alfagar/forecasts/latest)
## Features

- **Data Retrieval**: The program fetches surfing condition data from SurfForecast.com for various beaches along the Algarve coast.
  
- **Displaying Top Spots**: Users can view the top spots for a specific day to choose the best beach for surfing.

- **Dynamic Adaptation to New Beaches**: The program is prepared to add new beaches to its database, ensuring it remains effective even with an increasing number of available surfing spots.

- **Returning Conditions for All Beaches**: Users can obtain information on surfing conditions for all beaches simultaneously.

- **Returning Conditions for a Specific Beach**: Users can also view conditions for a specific beach.

- **7-Day Forecast**: The program provides a forecast for the next 7 days for all beaches.

- **Results for a Specific Day and Time**: Users can select a specific day and time to check surfing conditions for that period.

## Usage

1. **Installation**: To run the program, install the required Python libraries using `pip install -r requirements.txt`.
   
2. **Execution**: Run the `main.py` file using `python main.py`.


## Example response of engine if we want to get best spots for today

"Name of beach Julias
Today condition is: 
- Rating for AM is 3
- Rating for PM is 2
- Rating for Night is 0

 Name of beach Burgau
Today condition is: 
- Rating for AM is 3
- Rating for PM is 1
- Rating for Night is 0

 Name of beach Barranco-da-Belharucas
Today condition is: 
- Rating for AM is 3
- Rating for PM is 0
- Rating for Night is 0"