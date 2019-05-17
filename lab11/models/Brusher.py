from models.CarCleaningGoods import CarCleaningGoods
from models.Convenience import Convenience
from models.Quality import Quality


class Brusher(CarCleaningGoods):

    def __init__(self,

                 name="", producer="",
                 country="", sales_per_day=0,
                 price=0.0, quality=Quality.BAD, stiffness="", convenience=Convenience.COMFORTABLE):

        super(Brusher, self).__init__(
            name, producer,
            country, sales_per_day,
            price, quality

        )

        self.stiffness = stiffness
        self.convenience = convenience