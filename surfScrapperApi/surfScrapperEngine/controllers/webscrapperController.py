from surfScrapperApi.surfScrapperEngine.entities.beachEntity import BeachEntity
from surfScrapperApi.surfScrapperEngine.services.forecastDataService import ForecastDataService
from surfScrapperApi.surfScrapperEngine.services.webscrapperService import WebscrapperService


def sendEmailToSubscribers(db):
    # pass
    new_cur = db.cursor()
    subscribers = new_cur.execute("SELECT isActive FROM Subscribers ")
    print(subscribers)

def getBestSpotsForTommorow():
    webscrapperService = WebscrapperService(isHourlyMode=True)
    name_of_beaches = getNameOfBeachesInAlgarve(webscrapperService)
    beachEntities = buildBeachEntitiesFromWebsite(webscrapperService, name_of_beaches)
    print(f'Beach entities 9 len: {len(beachEntities)}')
    return filterBeachEntitiesToThreeBest(beachEntities)

def getNameOfBeachesForApi():
    webscrapperService = WebscrapperService(isHourlyMode=True)
    name_of_beaches = getNameOfBeachesInAlgarve(webscrapperService)
    return name_of_beaches

def getNameOfBeachesInAlgarve(webscrapperService):
    return webscrapperService.collectNameOfBeaches('https://www.surf-forecast.com/breaks/Praiado-Amado/forecasts/latest')

def buildBeachEntitiesFromWebsite(webscrapperService, name_of_beaches):
    beachEntities = []
    for index, beachName in enumerate(name_of_beaches):
        beachEntity = BeachEntity(beachName)
        print(f'Bede pytac o link https://www.surf-forecast.com/breaks/{beachName}/forecasts/latest')
        webscrapperService.scrapeRatingForBeach(f'https://www.surf-forecast.com/breaks/{beachName}/forecasts/latest', beachEntity)
        beachEntities.append(beachEntity)
        print(f'wielkosc beachEntities {len(beachEntities)}')

    return beachEntities

def filterBeachEntitiesToThreeBest(beachEntities):
    forecastDataService = ForecastDataService(beachEntities)
    # Index for day is count from today +n
    # Today = 0
    # Tommorow = 1 ... n+1
    print(f'Beach Entities {beachEntities}')
    return forecastDataService.getThreeBestSpotsForDay(indexOfDay=0)