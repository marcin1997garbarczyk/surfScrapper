
class ForecastDataService:

    def __init__(self, beachEntities):
        self.beachEntities = beachEntities


    def showRatingForBeaches(self, beachCollection = None):
        if(beachCollection is None):
            beachCollection = self.beachEntities

        for beachEntity in beachCollection:
            print(beachEntity)

    def showConditionForTodayForBeaches(self, collectionOfBeaches = None, indexOfDay = 0):
        if(collectionOfBeaches is None):
            collectionOfBeaches = self.beachEntities
        for beachEntity in collectionOfBeaches:
            print(f'\n Beach: {beachEntity.nameOfBeach}')
            if(not beachEntity.daysWithRatings):
                continue
            dayEntity = beachEntity.daysWithRatings[indexOfDay]
            print(f'Condition for {dayEntity.dayName}:')
            for ratingEntity in dayEntity.ratingsForDay:
                print(f'- {ratingEntity}')

    def showThreeBestSpotsForDay(self, indexOfDay = 0):
        sortedBeaches = []
        highestNumberInRating = 0

        for beachEntity in self.beachEntities:
            if(not beachEntity.daysWithRatings):
                continue
            dayEntity = beachEntity.daysWithRatings[indexOfDay]
            for ratingEntity in dayEntity.ratingsForDay:
                if(int(ratingEntity.rating) >= int(highestNumberInRating)):
                    highestNumberInRating = int(ratingEntity.rating)
                    if(len(sortedBeaches) == 0 or (len(sortedBeaches) > 0  and sortedBeaches[0].nameOfBeach != beachEntity.nameOfBeach)):
                        sortedBeaches.insert(0, beachEntity)

        newCollectionOfSortedBeaches = sortedBeaches[:3]
        self.showConditionForTodayForBeaches(newCollectionOfSortedBeaches, indexOfDay)
