import unittest

import task4
from task4 import List, Stack, Queue
class TestForList(unittest.TestCase):
    def test_init(self):
        self.t = task4.List()
        self.assertEqual("[]", str(self.t.list))
    def test_add(self):
        self.t = task4.List()
        self.t.add(3)
        self.assertEqual("[3]", str(self.t.list))

    def test_delete(self):
        self.t = task4.List()
        self.t.add(3)
        self.t.add(5)
        self.t.delete(3)
        self.assertEqual("[5]", str(self.t.list))

    def test_insert(self):
        self.t = task4.List()
        self.t.add(3)
        self.t.add(5)
        self.t.insert(10,1)
        self.assertEqual("[3, 10, 5]", str(self.t.list))
    def test_length(self):
        self.t = task4.List()
        self.t.add(3)
        self.t.add(5)
        l=self.t.length()
        self.assertEqual("2", str(l))
    def test_find(self):
        self.t = task4.List()
        self.t.add(3)
        self.t.add(5)
        ob = self.t.find(0)
        self.assertEqual("3", str(ob))
    def tearDown(self):
        pass


class TestForStack(unittest.TestCase):

    def test_init(self):
        self.t = task4.Stack()
        self.assertEqual("[]", str(self.t.stack))

    def test_push(self):
        self.t = task4.Stack()
        self.t.push(3)
        self.t.push(4)
        self.assertEqual("[3, 4]", str(self.t.stack))

    def test_pull(self):
        self.t = task4.Stack()
        self.t.push(3)
        self.t.push(4)
        self.t.push(8)
        self.t.pull()
        self.assertEqual("[3, 4]", str(self.t.stack))

    def test_length(self):
        self.t = task4.Stack()
        self.t.push(3)
        self.t.push(4)
        self.t.push(8)
        l=self.t.length()
        self.assertEqual("3", str(l))
    def tearDown(self):
        pass


class TestForQueue(unittest.TestCase):

    def test_init(self):
        self.t = task4.Queue()
        self.assertEqual("[]", str(self.t.queue))

    def test_push(self):
        self.t = task4.Queue()
        self.t.push(3)
        self.t.push(4)
        self.t.push(5)
        self.assertEqual("[5, 4, 3]", str(self.t.queue))

    def test_pull(self):
        self.t = task4.Queue()
        self.t.push(3)
        self.t.push(4)
        self.t.push(8)
        self.t.pull()
        self.assertEqual("[8, 4]", str(self.t.queue))

    def test_length(self):
        self.t = task4.Queue()
        self.t.push(3)
        self.t.push(4)
        self.t.push(8)
        l = self.t.length()
        self.assertEqual("3", str(l))

    def tearDown(self):
        pass