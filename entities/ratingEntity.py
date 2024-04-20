class RatingEntity:

    def __init__(self, timePeriod, rating):
        self.timePeriod = timePeriod
        self.rating = rating

    def __str__(self):
        return f'Rating for {self.timePeriod} is {self.rating}'