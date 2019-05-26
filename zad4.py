class Node:
    def __init__(self, name):
        self.name = name
        self.cost = float('inf')
        self.previous = None
        self.visited = False


class Connect:
    def __init__(self, first, second, cost):
        self.first = first
        self.second = second
        self.cost = cost


nod = {
    'a': Node('a'),
    'b': Node('b'),
    'c': Node('c'),
    'd': Node('d'),
    'e': Node('e'),
    'f': Node('f'),
    'g': Node('g')
}

connecty = [
    Connect(nod['a'], nod['d'], 2),
    Connect(nod['a'], nod['c'], 1),
    Connect(nod['c'], nod['b'], 2),
    Connect(nod['c'], nod['e'], 3),
    Connect(nod['c'], nod['d'], 1),
    Connect(nod['b'], nod['f'], 3),
    Connect(nod['e'], nod['f'], 2),
    Connect(nod['d'], nod['g'], 1),
    Connect(nod['g'], nod['f'], 1)
]


def dijkstra(start_node, end_node):
    checked = []                                    # lista kolejności do przeszukania

    current = start_node                                 # startujemy od podanego noda
    current.cost = 0

    queue = [item for tag, item in nod.items()]     # do przeszukania
    queue.remove(current)

    while len(queue) > 0:                           # powtarzaj jeśli są jeszcze nody do odwiedzenia

        current.visited = True                      # oznaczenie bieżącego noda jako odwiedzony

        for connect in connecty:
            if connect.first.name == current.name:
                if not nod[connect.second.name].visited and connect.second.cost > current.cost + connect.cost:
                    nod[connect.second.name].previous = current
                    connect.second.cost = current.cost + connect.cost

                    checked.append(nod[connect.second.name])        # dodanie noda do kolejki do odwiedzenia

            if connect.second.name == current.name:
                if not nod[connect.first.name].visited and connect.first.cost > current.cost + connect.cost:
                    nod[connect.first.name].previous = current
                    connect.first.cost = current.cost + connect.cost

                    checked.append(nod[connect.first.name])        # dodanie noda do kolejki do odwiedzenia

        if len(checked) > 0:                    # podmienienie bieżącego noda z pierwszym w kolejce
            current = checked[0]
            checked.remove(current)
            queue.remove(current)

    way_flag = end_node
    way = []
    while way_flag.previous is not None:
        way.append(way_flag.name)
        way_flag = way_flag.previous
    way.append(way_flag.name)
    way.reverse()

    print("Way:  ", way)
    print("Cost: ", end_node.cost)


start_id = input("Start: ")
end_id = input("End: ")

start = nod[start_id]
end = nod[end_id]

dijkstra(start, end)
