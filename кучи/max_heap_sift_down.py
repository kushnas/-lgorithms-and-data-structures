def sift_down(heap, index, heap_size):
    """Сдвигает узел вниз по кучи для поддержания свойств кучи."""
    largest = index  # Инициализируем наибольший элемент как корень
    left = 2 * index + 1  # Индекс левого потомка
    right = 2 * index + 2  # Индекс правого потомка

    # Если левый дочерний элемент больше корня
    if left < heap_size and heap[left] > heap[largest]:
        largest = left

    # Если правый дочерний элемент больше текущего наибольшего
    if right < heap_size and heap[right] > heap[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]  # Обмен значениями

        # Рекурсивно сдвигаем вниз корень
        sift_down(heap, largest, heap_size)

def build_max_heap(array):
    """Создает максимальную кучу из неупорядоченного массива."""
    heap_size = len(array)
    # Начинаем с первого неполного узла и сдвигаем вниз
    for i in range(heap_size // 2 - 1, -1, -1):
        sift_down(array, i, heap_size)

import unittest

class TestBuildMaxHeap(unittest.TestCase):

    def test_empty_array(self):
        array = []
        build_max_heap(array)
        self.assertEqual(array, [])

    def test_single_element(self):
        array = [42]
        build_max_heap(array)
        self.assertEqual(array, [42])

    def test_already_max_heap(self):
        array = [9, 6, 4, 5, 5, 2, 3, 1, 1]
        build_max_heap(array)
        self.assertEqual(array, [9, 6, 4, 5, 5, 2, 3, 1, 1])

    def test_unsorted_array(self):
        array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        build_max_heap(array)
        self.assertEqual(array, [9, 6, 4, 5, 5, 3, 2, 1, 1])

    def test_reversed_array(self):
        array = [1 ,2, 3, 4, 5]
        build_max_heap(array)
        self.assertEqual(array, [5, 4, 3, 1, 2])

    def test_duplicates(self):
        array = [3, 3, 3, 3, 3]
        build_max_heap(array)
        self.assertEqual(array, [3, 3, 3, 3, 3])

if __name__ == "__main__":
    unittest.main()