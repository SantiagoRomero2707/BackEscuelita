from .persistence import DatabasePersistence


class ChocolateResult:

    def __init__(self, total_to_spend, unit_cost, wrappers_promotion):
        self.total_to_spend = total_to_spend
        self.unit_cost = unit_cost
        self.wrappers_promotion = wrappers_promotion

    def chocolate_feast(self):
        chocolate = 0
        wrapper = 0
        while True:
            if self.total_to_spend == 0:
                if wrapper >= self.wrappers_promotion:
                    chocolate = chocolate+1
                    wrapper = wrapper - 1
                else:
                    DatabasePersistence.write_persistence(chocolate)
                    return chocolate
            else:
                self.total_to_spend = self.total_to_spend-self.unit_cost
                chocolate = chocolate+1
                wrapper = wrapper + 1
                continue

