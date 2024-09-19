from surfScrapperApi.surfScrapperEngine.entities.beachEntity import BeachEntity
from surfScrapperApi.surfScrapperEngine.services.forecastDataService import ForecastDataService
from surfScrapperApi.surfScrapperEngine.services.webscrapperService import WebscrapperService
from django.core.serializers import serialize

webscrapperService = WebscrapperService(isHourlyMode=True)

def scrapeAndFormatThreeBestBeaches(name_of_beaches):
    beachEntities = scrapeDataAndConvertToBeachEntities(name_of_beaches)
    forecastDataService = ForecastDataService(beachEntities)
    return forecastDataService.getThreeBestSpotsForDay(indexOfDay=0)

def scrapeAndUploadAllBeachesToDb(beachModel):
    name_of_beaches = getNameOfBeachesInAlgarve()
    beachEntities = scrapeDataAndConvertToBeachEntities(name_of_beaches)
    forecastDataService = ForecastDataService(beachEntities)
    forecastDataService.uploadBeachesToDb(beachModel=beachModel, indexOfDay=0)
    forecastDataService.uploadBeachesToDb(beachModel=beachModel, indexOfDay=1)

def getSortedBeachesInJSON(beachModel, indOfDay = 0):
    return serialize("json", beachModel.objects.filter(indexOfDay=indOfDay).order_by('totalScore').reverse())

def getNameOfBeachesInAlgarve():
    return webscrapperService.collectNameOfBeaches('https://www.surf-forecast.com/breaks/Praiado-Amado/forecasts/latest')

def scrapeDataAndConvertToBeachEntities(name_of_beaches):
    beachEntities = []
    for index, beachName in enumerate(name_of_beaches):
        beachEntity = BeachEntity(beachName)
        webscrapperService.scrapeRatingForBeach(f'https://www.surf-forecast.com/breaks/{beachName}/forecasts/latest', beachEntity)
        beachEntities.append(beachEntity)

    return beachEntities
