import requests
from bs4 import BeautifulSoup

from surfScrapperApi.surfScrapperEngine.entities.ratingEntity import RatingEntity


class WebscrapperService:

    def __init__(self, isHourlyMode):
        self.isHourlyMode = isHourlyMode
        if(self.isHourlyMode == False):
            self.urlSuffix = '/six_day'
        else:
            self.urlSuffix = ''

    def collectNameOfBeaches(self, url):
        r = requests.get(f'{url}{self.urlSuffix}')
        soup = BeautifulSoup(r.content, 'html5lib')

        soupDays = soup.find('span', class_='third_step_span')
        # print(soupDays.find_all('option'))
        beachesArray = []
        for value in soupDays.find_all('option'):
            valueInStr = str(value)
            indexOfStart = valueInStr.index('"')
            indexOfEnd = valueInStr.rfind('"')
            # print(valueInStr[indexOfStart+1:indexOfEnd])
            beachesArray.append(valueInStr[indexOfStart+1:indexOfEnd])

        return beachesArray[1:]

    def scrapeRatingForBeach(self, url, beachEntity):
        r = requests.get(f'{url}{self.urlSuffix}')
        soup = BeautifulSoup(r.content, 'html5lib')

        soupDays = soup.find('tr', class_='forecast-table-days')
        soupTime = soup.find('tr', class_='forecast-table-time')
        soupRating = soup.find('tr', class_='forecast-table-rating')

        if(not soupRating):
            return
        soupRatingWithCells = soupRating.find_all('td', class_='forecast-table__cell')
        soupDaysWithCells = soupDays.find_all('td', class_='forecast-table__cell')
        soupTimeWithCells = soupTime.find_all('td', class_='forecast-table__cell')

        startingPeriodOfTime = soupTimeWithCells[0].getText()
        daysPeriodToCount = self.calculateHowMuchPeriodOfDaysIsThere(startingPeriodOfTime)

        counterForDays = 0

        # print(soupTimeWithCells)
        indexForDays = 0

        for idx, tempElement in enumerate(soupRatingWithCells):
            if(counterForDays > 7):
                break

            timeForSurf = soupTimeWithCells[idx].getText()
            dayForSurf = soupDaysWithCells[counterForDays].getText()
            ratingForSurf = soupRatingWithCells[idx].getText()

            ratingEntity = RatingEntity(timeForSurf, ratingForSurf)
            currentDay = beachEntity.getDayWithRating(dayForSurf)
            # print(currentDay)
            currentDay.addRatingForTimePeriod(ratingEntity)



            numberForModulo = 3
            if(self.isHourlyMode == True):
                numberForModulo = 7
            if(idx == daysPeriodToCount or (indexForDays % numberForModulo == 0 and idx != 0)):
                counterForDays += 1
                indexForDays = 0

            indexForDays += 1

    def calculateHowMuchPeriodOfDaysIsThere(self, startingPeriodOfTime):
        daysPeriodToCount = 0
        if(self.isHourlyMode == True):
            startingPeriodOfTime = startingPeriodOfTime.encode('ascii', 'ignore').decode("utf-8")
            if (startingPeriodOfTime == '1AM'):
                daysPeriodToCount = 7
            elif (startingPeriodOfTime == '4AM'):
                daysPeriodToCount = 6
            elif (startingPeriodOfTime == '7AM'):
                daysPeriodToCount = 5
            elif (startingPeriodOfTime == '10AM'):
                daysPeriodToCount = 4
            elif (startingPeriodOfTime == '1PM'):
                daysPeriodToCount = 3
            elif (startingPeriodOfTime == '4PM'):
                daysPeriodToCount = 2
            elif (startingPeriodOfTime == '7PM'):
                daysPeriodToCount = 1
            elif (startingPeriodOfTime == '10PM'):
                daysPeriodToCount = 0
        else:
            if (startingPeriodOfTime == 'AM'):
                daysPeriodToCount = 2
            elif (startingPeriodOfTime == 'PM'):
                daysPeriodToCount = 1
            elif (startingPeriodOfTime == 'Night'):
                daysPeriodToCount = 0
        # print(f'daysforperiod {daysPeriodToCount}')
        return daysPeriodToCount
