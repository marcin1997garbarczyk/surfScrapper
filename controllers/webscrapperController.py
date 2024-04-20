from entities.beachEntity import BeachEntity
from services.forecastDataService import ForecastDataService
from services.webscrapperService import WebscrapperService

def runWebscrappingEngine():
    webscrapperService = WebscrapperService(isHourlyMode=True)
    name_of_beaches = getNameOfBeachesInAlgarve(webscrapperService)
    beachEntities = buildBeachEntitiesFromWebsite(webscrapperService, name_of_beaches)
    workWithBeachEntitiesData(beachEntities)

def getNameOfBeachesInAlgarve(webscrapperService):
    return webscrapperService.collectNameOfBeaches('https://www.surf-forecast.com/breaks/Praiado-Amado/forecasts/latest')

def buildBeachEntitiesFromWebsite(webscrapperService, name_of_beaches):
    beachEntities = []
    for index, beachName in enumerate(name_of_beaches):
        # if(index > 3):
        #     break
        beachEntity = BeachEntity(beachName)
        webscrapperService.scrapeRatingForBeach(f'https://www.surf-forecast.com/breaks/{beachName}/forecasts/latest', beachEntity)
        beachEntities.append(beachEntity)

    return beachEntities

def workWithBeachEntitiesData(beachEntities):
    forecastDataService = ForecastDataService(beachEntities)
    # Index for day is count from today +n
    # Today = 0
    # Tommorow = 1 ... n+1
    forecastDataService.showThreeBestSpotsForDay(indexOfDay=1)