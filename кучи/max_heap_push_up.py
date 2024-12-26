def push(heap, data):
    heap.append(data)
    up(heap, heap[len(heap)-1])
def up(heap, index):
    while index > 0:
        parent = (index - 1) // 2 
        if heap[parent] < heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
        else:
            break

if __name__ == "__main__":
    max_heap = []
    push(max_heap, 10)
    push(max_heap, 20)
    push(max_heap, 15)
    push(max_heap, 30)
    push(max_heap, 40)

    print("Куча после вставок:", max_heap)  