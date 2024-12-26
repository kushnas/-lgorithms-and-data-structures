def dfs(graph, v, visited, parent):
    visited[v] = True  # Отмечаем текущую вершину как посещённую

    # Рекурсивно посещаем все соседние вершины
    for neighbor in graph[v]:
        if not visited[neighbor]:  # Если сосед не посещён
            if dfs(graph, neighbor, visited, v):  # Рекурсивный вызов
                return True
        elif neighbor != parent:  # Если сосед посещён и не является родителем
            return True  # Найден цикл

    return False  # Цикл не найден

def has_cycle(graph):
    n = len(graph)
    visited = [False] * n  # Массив для отслеживания посещённых вершин

    for v in range(n):
        if not visited[v]:  # Если вершина не посещена
            if dfs(graph, v, visited, -1):  # Запускаем DFS без родителя
                return True  # Цикл найден

    return False  # Если цикл не найден

# Пример использования
if __name__ == "__main__":
    # Представим граф в виде списка смежности
    graph = [
        [1, 2],  # Вершина 0
        [0, 2],  # Вершина 1
        [0, 1],  # Вершина 2 (образует цикл)
        [4],     # Вершина 3
        [3],     # Вершина 4
    ]

    if has_cycle(graph):
        print("Цикл найден в графе.")
    else:
        print("Цикл не найден в графе.")