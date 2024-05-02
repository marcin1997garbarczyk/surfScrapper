from numpy.core.defchararray import isnumeric
import numpy as np

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
        beachWithRankingPoints = {}
        beachEntitiesCollection = {}

        for beachEntity in self.beachEntities:
            if(not beachEntity.daysWithRatings):
                continue
            dayEntity = beachEntity.daysWithRatings[indexOfDay]
            summaryOfRating = 0
            for ratingEntity in dayEntity.ratingsForDay:
                if(isnumeric(ratingEntity.rating) == False):
                    continue
                summaryOfRating = summaryOfRating + int(ratingEntity.rating)

            print(f'Beach {beachEntity.nameOfBeach} has score {summaryOfRating}')

            beachWithRankingPoints[beachEntity.nameOfBeach] = summaryOfRating
            beachEntitiesCollection[beachEntity.nameOfBeach] = beachEntity

        # print(beachWithRankingPoints)
        keys = list(beachWithRankingPoints.keys())
        values = list(beachWithRankingPoints.values())
        sorted_value_index = np.argsort(values)
        sorted_collection_of_beaches = {keys[i]: values[i] for i in sorted_value_index}
        # print(sorted_collection_of_beaches)

        for beachName in sorted_collection_of_beaches.keys():
            sortedBeaches.insert(0, beachEntitiesCollection[beachName])



        newCollectionOfSortedBeaches = sortedBeaches
        flatStructureForRatings = self.showConditionForTodayForBeaches(newCollectionOfSortedBeaches, indexOfDay)
        return flatStructureForRatings.split('Beach:')[1:]


    def uploadBeachesToDb(self, beachModel, indexOfDay = 0):
        sortedBeaches = []
        beachWithRankingPoints = {}
        beachEntitiesCollection = {}

        for beachEntity in self.beachEntities:
            if(not beachEntity.daysWithRatings):
                continue
            dayEntity = beachEntity.daysWithRatings[indexOfDay]
            summaryOfRating = 0
            for ratingEntity in dayEntity.ratingsForDay:
                if(isnumeric(ratingEntity.rating) == False):
                    continue
                summaryOfRating = summaryOfRating + int(ratingEntity.rating)

            print(f'Beach {beachEntity.nameOfBeach} has score {summaryOfRating}')

            beachWithRankingPoints[beachEntity.nameOfBeach] = summaryOfRating
            beachEntitiesCollection[beachEntity.nameOfBeach] = beachEntity

        keys = list(beachWithRankingPoints.keys())
        values = list(beachWithRankingPoints.values())
        sorted_value_index = np.argsort(values)
        sorted_collection_of_beaches = {keys[i]: values[i] for i in sorted_value_index}


        for beachName in sorted_collection_of_beaches.keys():
            sortedBeaches.insert(0, beachEntitiesCollection[beachName])
            textForHtml = ''
            beachEntity = beachEntitiesCollection[beachName]
            textForHtml += f'Beach: {beachEntity.nameOfBeach} '
            if(not beachEntity.daysWithRatings):
                continue
            dayEntity = beachEntity.daysWithRatings[indexOfDay]

            textForHtml += f'<br/> Condition for {dayEntity.dayName}:'
            for ratingEntity in dayEntity.ratingsForDay:
                textForHtml += f'<br/>{ratingEntity}'

            try:
                obj = beachModel.objects.get(name=beachName)
            except(TypeError, ValueError, OverflowError, beachModel.DoesNotExist):
                obj = beachModel()
                obj.name = beachName
            obj.textForHtml = textForHtml
            obj.totalScore = beachWithRankingPoints[beachName]
            obj.save()




        newCollectionOfSortedBeaches = sortedBeaches
        flatStructureForRatings = self.showConditionForTodayForBeaches(newCollectionOfSortedBeaches, indexOfDay)
        return flatStructureForRatings.split('Beach:')[1:]

