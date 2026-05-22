from discount_service import DiscountService
from diawli import DiwaliStrategy
from holi import HoliStrategy


diwali_strategy = DiwaliStrategy()
holi_strategy = HoliStrategy()

discount_service = DiscountService(diwali_strategy)
discount_service.process()

discount_service.set_strategy(holi_strategy)
discount_service.process()
