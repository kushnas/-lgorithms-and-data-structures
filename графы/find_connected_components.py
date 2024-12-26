def dfs(graph, v, visited, component):
    visited[v] = True  # Отмечаем текущую вершину как посещённую
    component.append(v)  # Добавляем вершину в текущую компоненту

    # Рекурсивно посещаем все соседние вершины
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def find_connected_components(graph):
    visited = [False] * len(graph)  # Массив для отслеживания посещённых вершин
    components = []  # Список для хранения компонент связности

    for v in range(len(graph)):
        if not visited[v]:  # Если вершина не посещена
            component = []  # Создаём новую компоненту 
            dfs(graph, v, visited, component)  # Запускаем DFS
            components.append(component)  # Добавляем компоненту в список

    return components


if __name__ == "__main__":
    graph = [
        [1, 2],    
        [0, 2],  
        [0, 1],    
        [3],       
        [5],       
        [5]        
    ]

    components = find_connected_components(graph)
    print("Компоненты связности:", components)