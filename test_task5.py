import unittest

import task5
from task5 import read_file,ORFfind,ORF100
class TestORF(unittest.TestCase):
    def test_read(self):
        with open('vector.fasta') as seq_file:
            self.t = read_file(seq_file)
        self.assertEqual(['ATGGCTCAGATTGAACGCTGGCGGCAGGCCTAAATGTTGGGTTAA'], self.t)
    def test_find(self):
        with open('vector.fasta') as seq_file:
            self.t = read_file(seq_file)
        self.tORF=ORFfind(self.t)
        self.assertEqual(['ATGGCTCAGATTGAACGCTGGCGGCAGGCCTAA'], self.tORF)
    def test_100(self):
        with open('vector.fasta') as seq_file:
            self.t =read_file(seq_file)
        self.tORF = ORFfind(self.t)
        self.tORF100=ORF100(self.tORF)
        self.assertEqual(['ATGGCTCAGATTGAACGCTGGCGGCAGGCCTAA'], self.tORF100)
    def tearDown(self):
        pass