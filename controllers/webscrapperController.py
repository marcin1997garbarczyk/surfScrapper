from entities.beachEntity import BeachEntity
from services.forecastDataService import ForecastDataService
from services.webscrapperService import WebscrapperService

def runWebscrappingEngine():
    webscrapperService = WebscrapperService(False)
    name_of_beaches = webscrapperService.collectNameOfBitches('https://www.surf-forecast.com/breaks/Praiado-Amado/forecasts/latest/six_day')

    # print(name_of_beaches)
    beachEntities = []
    for beachName in name_of_beaches:
        beachEntity = BeachEntity(beachName)
        webscrapperService.scrapeRatingForBeach(f'https://www.surf-forecast.com/breaks/{beachName}/forecasts/latest/six_day', beachEntity)
        beachEntities.append(beachEntity)

    forecastDataService = ForecastDataService(beachEntities)
    forecastDataService.showAllRatingsForAllBeaches()
