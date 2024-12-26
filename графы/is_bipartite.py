from collections import deque

def is_bipartite(graph):
    # Храним цвет каждой вершины. 0 и 1 - два цвета, -1 - еще не раскрашена
    color = {}
    
    # Обходим все вершины графа
    for vertex in graph:
        if vertex not in color:  # Если вершина еще не раскрашена
            queue = deque([vertex])
            color[vertex] = 0  # Начнем с цвета 0

            while queue:
                current = queue.popleft()

                # Проверяем соседей текущей вершины
                for neighbor in graph[current]:
                    if neighbor not in color:  # Если сосед не раскрашен
                        # Присваиваем противоположный цвет
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:  # Конфликт
                        return False

    return True


if __name__ == "__main__":
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }

    if is_bipartite(graph):
        print("Граф является двудольным.")
    else:
        print("Граф не является двудольным.")