from models.CarCleaningGoods import CarCleaningGoods
from models.Quality import Quality
from models.Size import Size


class Duster(CarCleaningGoods):

    def __init__(self,

                 name="", producer="",
                 country="", sales_per_day=0,
                 price=0.0, quality=Quality.BAD, size=Size.L, material="", color=""):

        super(Duster, self).__init__(
            name, producer,
            country, sales_per_day,
            price, quality

        )

        self.size = size
        self.material = material
        self.color = color