from surfScrapperApi.surfScrapperEngine.entities.dayEntity import DayEntity


class BeachEntity:

    def __init__(self, nameOfBeach):
        self.nameOfBeach = nameOfBeach
        self.daysWithRatings = []

    def addDayWithRatings(self, dayEntity):
        existingDay = self.getDayWithRating(dayEntity.dayName)
        if(not existingDay):
            self.daysWithRatings.append(dayEntity)
            print(f'Added day entity {dayEntity.dayName}')

    def getDayWithRating(self, dayName):

        foundRecord = False
        dayEntityToFound = ''
        for dayWithRating in self.daysWithRatings:
            if(dayWithRating.dayName == dayName):
                foundRecord = True
                dayEntityToFound = dayWithRating

        if(foundRecord == True):
            return dayEntityToFound
        else:
            newEntity = DayEntity(dayName)
            self.daysWithRatings.append(newEntity)
            return newEntity


    def __str__(self):
        beachString = f'{self.nameOfBeach} \n'
        for dayEntity in self.daysWithRatings:
            beachString = beachString + f'Day: {dayEntity.dayName} \n'
            for ratingEntity in dayEntity.ratingsForDay:
                beachString = beachString + f'Rating: {ratingEntity} \n'
        return beachString