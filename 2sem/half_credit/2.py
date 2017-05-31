dfs_used = None
number_of_components = 1


def count_components_dfs():
    """
    Считает количество компонент связности в графе, заданном листом, с помощью обхода в глубину.
    @return: Возвращает число - количество компонент связности, а также записывает его в поле number_of_components
    """
    if dfs_used is None:  # Если мы ни разу не считали компоненты, чтобы in self.dfs_used ниже в проверке не вылетал :)
        dfs_used = set()

    n = 0
    for vertex in range(len(graph_as_list)):  # Для каждой вершины,
        if vertex not in dfs_used:  # если она не была обработана dfs, то
            dfs_list_graph(vertex)  # обрабатываем все вершины функцией dfs, начиная с vertex,
            n += 1  # и увеличиваем число компонент на 1
    number_of_components = n  # записываем результаты трудов
    return n