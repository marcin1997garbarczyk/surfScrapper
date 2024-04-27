from numpy.core.defchararray import isnumeric


class ForecastDataService:

    def __init__(self, beachEntities):
        self.beachEntities = beachEntities


    def showRatingForBeaches(self, beachCollection = None):
        if(beachCollection is None):
            beachCollection = self.beachEntities

        for beachEntity in beachCollection:
            print(beachEntity)

    def showConditionForTodayForBeaches(self, collectionOfBeaches = None, indexOfDay = 0):
        flatStructureForString = ''
        if(collectionOfBeaches is None):
            collectionOfBeaches = self.beachEntities
        for beachEntity in collectionOfBeaches:
            # print(f'\n Beach: {beachEntity.nameOfBeach}')
            flatStructureForString += f'<br/> Beach: {beachEntity.nameOfBeach} '
            if(not beachEntity.daysWithRatings):
                continue
            dayEntity = beachEntity.daysWithRatings[indexOfDay]

            flatStructureForString += f'<br/> Condition for {dayEntity.dayName}:'
            # print(f'Condition for {dayEntity.dayName}:')
            for ratingEntity in dayEntity.ratingsForDay:
                flatStructureForString += f'<br/>{ratingEntity}'
                # print(f'- {ratingEntity}')
        return flatStructureForString

    def getThreeBestSpotsForDay(self, indexOfDay = 0):
        sortedBeaches = []
        highestNumberInRating = 0

        for beachEntity in self.beachEntities:
            if(not beachEntity.daysWithRatings):
                continue
            dayEntity = beachEntity.daysWithRatings[indexOfDay]
            for ratingEntity in dayEntity.ratingsForDay:
                if(isnumeric(ratingEntity.rating) and int(ratingEntity.rating) >= int(highestNumberInRating)):
                    highestNumberInRating = int(ratingEntity.rating)
                    if(len(sortedBeaches) == 0 or (len(sortedBeaches) > 0  and sortedBeaches[0].nameOfBeach != beachEntity.nameOfBeach)):
                        sortedBeaches.insert(0, beachEntity)

        newCollectionOfSortedBeaches = sortedBeaches
        flatStructureForRatings = self.showConditionForTodayForBeaches(newCollectionOfSortedBeaches, indexOfDay)
        return flatStructureForRatings.split('Beach:')[1:]
