class DayEntity:

    def __init__(self, dayName):
        self.dayName = dayName
        self.ratingsForDay = []

    def addRatingForTimePeriod(self, ratingEntity):
        self.ratingsForDay.append(ratingEntity)

    def __str__(self):
        return f'Day name : {self.dayName}'