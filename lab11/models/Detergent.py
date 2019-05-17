from models.CarCleaningGoods import CarCleaningGoods
from models.Quality import Quality


class Detergent(CarCleaningGoods):

    def __init__(self,

                 name="", producer="",
                 country="", sales_per_day=0,
                 price=0.0, quality=Quality.BAD, capacity=0.0, appliance=""):

        super(Detergent, self).__init__(
            name, producer,
            country, sales_per_day,
            price, quality

        )

        self.capacity = capacity
        self.appliance = appliance