from models.CarCleaningGoods import CarCleaningGoods
from models.Brusher import Brusher
from models.Convenience import Convenience
from models.Detergent import Detergent
from models.Duster import Duster
from models.HighPressureWasher import HighPressureWasher
from models.Quality import Quality
from models.Size import Size
import sys
sys.path.insert(0, '../models')


class CarCleaningGoodsManager:
    def __init__(self, *args):
        self.goods = args

    @staticmethod
    def sort_by_price(goods, descending=False):
        return sorted(goods, key=lambda goods: goods.price, reverse=descending)

    @staticmethod
    def sort_by_price_ascending(goods):
        return CarCleaningGoodsManager.sort_by_price(goods)

    @staticmethod
    def sort_by_price_descending(goods):
        return CarCleaningGoodsManager.sort_by_price(goods, True)

    @staticmethod
    def sort_by_sales_per_day(goods, descending=False):
        return sorted(goods, key=lambda goods: goods.sales_per_day, reverse=descending)

    @staticmethod
    def sort_by_sales_per_day_ascending(goods):
        return CarCleaningGoodsManager.sort_by_sales_per_day(goods)

    @staticmethod
    def sort_by_sales_per_day_descending(goods):
        return CarCleaningGoodsManager.sort_by_sales_per_day(goods, True)

    def filter_by_quality(self, quality):
        return list(filter(lambda goods: goods.quality == quality, self.goods))

    def filter_by_name(self, name):
        return list(filter(lambda goods: goods.name == name, self.goods))

    def filter_by_producer(self, producer):
        return list(filter(lambda goods: goods.producer == producer, self.goods))

    def filter_by_country(self, country):
        return list(filter(lambda goods: goods.country == country, self.goods))


def main():

    goods = [CarCleaningGoods("Duster", "CrystalClean", "France", 30, 55, Quality.GOOD, ),
              Brusher("Brush", "Rock", "Poland", 10, 30, Quality.BAD, "light", Convenience.COMFORTABLE),
              Detergent("Detergent", "Mr.Clean", "Poland", 30, 60, Quality.GOOD, 1.5, "panel"),
              Duster("Duster", "CrystalClean", "France", 30, 55, Quality.GOOD, Size.L,"cotton", "blue"),
              HighPressureWasher("High Pressure Washer", "Kar", "Germany", 3, 5000, Quality.GOOD, 3)
              ]

    manager = CarCleaningGoodsManager(*goods)

    filteredList = manager.filter_by_name(0)
    for s in filteredList:
     print(s)
    print()

    sortedList = CarCleaningGoodsManager.sort_by_price_ascending(goods)
    for s in sortedList:
     print(s)
    print()

    sortedFilteredList = CarCleaningGoodsManager.sort_by_sales_per_day_descending(filteredList)
    for s in sortedFilteredList:
     print(s)


if __name__ == '__main__':
    main()