from models.Quality import Quality


class CarCleaningGoods:

    def __init__(self,
                 name="", producer="",
                 country="", sales_per_day=0,
                 price=0.0, quality=Quality.BAD):

        self.name = name
        self.producer = producer
        self.country = country
        self.sales_per_day = sales_per_day
        self.price = price
        self.quality = quality

    def __str__(self):

        return ', '.join((f"{name} = {value}" for name, value in self.__dict__.items()))