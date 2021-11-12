import sys
import unittest
from ComputeSum import computeSum

class SumMethod(unittest.TestCase):

    def __init__(self, testName, args):
        super(SumMethod, self).__init__(testName)
        self.args = args
      
    def test_a(self):
        self.assertEqual(computeSum(self.args), 6)
  
    def test_b(self):        
        self.assertEqual(computeSum(self.args), 3)
  
    def test_c(self):        
        self.assertEqual(computeSum(self.args), 3)

    def test_d(self):        
        self.assertEqual(computeSum(self.args), 18)
  
    def test_3(self):        
        self.assertEqual(computeSum(self.args), "Exactly 3 numbers are required")
  
    def test_char(self):        
        self.assertEqual(computeSum(self.args), "All inputs must be numeric")
  
if __name__ == '__main__':
    args1 = [1,2,3]
    args2 = [2,13,1] 
    args3 = [2,1,14] 
    args4 = [2,1,15] 
    args5 = [1,2]
    args6 = [1,2,'a'] 

    suite = unittest.TestSuite()
    suite.addTest(SumMethod("test_a", args1))
    suite.addTest(SumMethod("test_b", args2))
    suite.addTest(SumMethod("test_c", args3))
    suite.addTest(SumMethod("test_d", args4))
    suite.addTest(SumMethod("test_3", args5))
    suite.addTest(SumMethod("test_char", args6))
    unittest.TextTestRunner(verbosity=2).run(suite)
