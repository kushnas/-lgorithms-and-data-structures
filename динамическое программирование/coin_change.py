def coin_change(coins, amount):
    coins.sort(reverse=True)  # Сортируем монеты по убыванию
    count = 0  # Счетчик монет

    for coin in coins:
        if amount <= 0:
            break  # Если сумма достигнута, заканчиваем цикл
        
        num_coins = amount // coin  # Сколько раз можем использовать текущую монету
        count += num_coins  # Увеличиваем счетчик
        amount -= num_coins * coin  # Уменьшаем оставшуюся сумму

    return count if amount == 0 else -1  # Если сумма достигнута, возвращаем количество монет, иначе -1


import unittest

class TestCoinChange(unittest.TestCase):

    def test_example_cases(self):
        # Тестируем стандартные примеры
        self.assertEqual(coin_change([1, 2, 5], 11), 3)  # 5 + 5 + 1
        self.assertEqual(coin_change([2, 5], 3), -1)      # Невозможно составить сумму
        self.assertEqual(coin_change([1], 0), 0)          # Для суммы 0
        self.assertEqual(coin_change([1], 2), 2)          # 1 + 1
        self.assertEqual(coin_change([1, 5, 10, 25], 31), 3)  # 25 + 5 + 1

    def test_no_possible_combination(self):
        self.assertEqual(coin_change([5, 3], 7), -1)      # Невозможно составить сумму

    def test_large_values(self):
        self.assertEqual(coin_change([25, 10, 5, 1], 100), 4)  # 25 + 25 + 25 + 25
        self.assertEqual(coin_change([10, 5, 1], 18), 5)      # 10 + 5 + 1 + 1 + 1

    def test_single_coin(self):
        self.assertEqual(coin_change([1], 1), 1)              # 1 = 1
        self.assertEqual(coin_change([1], 5), 5)              # 5 = 1 + 1 + 1 + 1 + 1
        self.assertEqual(coin_change([1], 3), 3)              # 3 = 1 + 1 + 1

    def test_multiple_same_coins(self):
        self.assertEqual(coin_change([1, 1, 1, 1], 4), 4)    # 1 + 1 + 1 + 1
        self.assertEqual(coin_change([2, 2, 2], 6), 3)        # 2 + 2 + 2

    def test_with_non_collectable_amount(self):
        self.assertEqual(coin_change([3, 5], 7), -1)          # Невозможно составить 7
        self.assertEqual(coin_change([2, 4], 3), -1)          # Невозможно составить 3

if __name__ == "__main__":
    unittest.main()