import unittest
from routes import shortest_path,validate


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.edges=[{"from":"A","to":"B","cost":2},{"from":"B","to":"C","cost":3},{"from":"A","to":"C","cost":9}]
    def test_shortest_path(self):
        self.assertEqual(shortest_path(self.edges,"A","C")["path"],["A","B","C"])
    def test_cost(self):
        self.assertEqual(shortest_path(self.edges,"A","C")["cost"],5)
    def test_same_node(self):
        self.assertEqual(shortest_path(self.edges,"A","A")["cost"],0)
    def test_unreachable(self):
        self.assertIsNone(shortest_path(self.edges,"C","A")["path"])
    def test_unknown_node(self):
        with self.assertRaises(ValueError): shortest_path(self.edges,"Z","A")
    def test_negative_edge(self):
        with self.assertRaises(ValueError): validate([{"from":"A","to":"B","cost":-1}])
    def test_nan_edge(self):
        with self.assertRaises(ValueError): validate([{"from":"A","to":"B","cost":float("nan")}])
    def test_directed(self):
        self.assertIsNone(shortest_path(self.edges,"B","A")["path"])


if __name__=="__main__":
    unittest.main()
