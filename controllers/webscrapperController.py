from entities.beachEntity import BeachEntity
from services.forecastDataService import ForecastDataService
from services.webscrapperService import WebscrapperService

def runWebscrappingEngine():
    webscrapperService = WebscrapperService(False)
    name_of_beaches = webscrapperService.collectNameOfBitches('https://www.surf-forecast.com/breaks/Praiado-Amado/forecasts/latest/six_day')

    beachEntities = []
    for idx, beachName in enumerate(name_of_beaches):
        beachEntity = BeachEntity(beachName)
        webscrapperService.scrapeRatingForBeach(f'https://www.surf-forecast.com/breaks/{beachName}/forecasts/latest/six_day', beachEntity)
        beachEntities.append(beachEntity)

    forecastDataService = ForecastDataService(beachEntities)
    # Index for day is count from today +n
    # Today = 0
    # Tommorow = 1 ... n+1
    forecastDataService.showThreeBestSpotsForDay(indexOfDay=0)
