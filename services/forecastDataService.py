
class ForecastDataService:

    def __init__(self, beachEntities):
        self.beachEntities = beachEntities


    def showRatingForBeaches(self, beachCollection = None):
        if(beachCollection is None):
            beachCollection = self.beachEntities

        for beachEntity in beachCollection:
            print(beachEntity)

    def showConditionForTodayForBeaches(self, collectionOfBeaches = None):
        if(collectionOfBeaches is None):
            collectionOfBeaches = self.beachEntities
        for beachEntity in collectionOfBeaches:
            print(f'\n Name of beach {beachEntity.nameOfBeach}')
            print('Tommorow condition is: ')
            if(not beachEntity.daysWithRatings):
                continue
            dayEntity = beachEntity.daysWithRatings[0]
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
                    sortedBeaches.insert(0, beachEntity)
                    highestNumberInRating = int(ratingEntity.rating)

        newCollectionOfSortedBeaches = sortedBeaches[:3]
        self.showConditionForTodayForBeaches(newCollectionOfSortedBeaches)
