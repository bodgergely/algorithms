import unittest


class graph:
    def __init__(self, directed=False):
        self.nodes = set()
        self.nedges = 0
        self.adj_list = dict()
        self.directed = directed
    def add_edge(self, x, y):
        self.nodes.add(x)
        self.nodes.add(y)
        self._add_edge(x, y)
        if not self.directed:
            self._add_edge(y, x)
    def _add_edge(self, x, y):
        adj_list = self.adj_list
        self.nedges += 1
        if x not in adj_list:
            adj_list[x] = [y]
        else:
            adj_list[x].append(y)
    def _add_node(x):
        self.nodes.add(x)
    def print(self):
        for x, neighbors in self.adj_list.items():
            for y in neighbors:
                 print("{} -> {}".format(x, y))
        print("node count:", len(self.nodes), "edge count:", self.nedges)


class graph_test(unittest.TestCase):
    def test_basic(self):
        g = graph(directed=False)
        g.add_edge(1,2)
        g.add_edge(1,3)
        self.assertEqual(len(g.nodes), 3)
        self.assertEqual(g.nedges, 4)

if __name__ == "__main__":
    g = graph()
    g.add_edge(1,3)
    g.add_edge(4,2)
    g.print()

    unittest.main()


