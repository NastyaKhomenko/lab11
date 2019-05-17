from models.CarCleaningGoods import CarCleaningGoods
from models.Quality import Quality


class HighPressureWasher(CarCleaningGoods):

    def __init__(self,

                 name="", producer="",
                 country="", sales_per_day=0,
                 price=0.0, quality=Quality.BAD, power=0):

        super(HighPressureWasher, self).__init__(
            name, producer,
            country, sales_per_day,
            price, quality

        )

        self.power = power