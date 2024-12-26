def max_profit(prices):
    if not prices:
        return 0  # Если нет цен, прибыли тоже нет

    profit = 0
    min_price = prices[0]

    for current_price in prices[1:]:
        # Обновляем прибыль, если разница между текущей ценой и минимальной ценой больше
        profit = max(profit, current_price - min_price)
        # Обновляем минимальную цену
        min_price = min(current_price, min_price)

    return profit

import unittest

class TestMaxProfit(unittest.TestCase):

    def test_profit_example(self):
        self.assertEqual(max_profit([8, 9, 3, 7, 4, 16, 12]), 13)  
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)  
        self.assertEqual(max_profit([5, 4, 3, 2, 1]), 0)  
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)  
        self.assertEqual(max_profit([2, 4, 1]), 2)  
    def test_empty_price_list(self):
        self.assertEqual(max_profit([]), 0)  
    def test_single_element_price_list(self):
        self.assertEqual(max_profit([10]), 0)  

if __name__ == "__main__":
    unittest.main()