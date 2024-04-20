
class ForecastDataService:

    def __init__(self, beachEntities):
        self.beachEntities = beachEntities


    def showAllRatingsForAllBeaches(self):
        for beachEntity in self.beachEntities:
            print(beachEntity)