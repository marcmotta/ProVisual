# test_provisual.py
"""
Tests for ProVisual module.
"""

import unittest
from provisual import ProVisual

class TestProVisual(unittest.TestCase):
    """Test cases for ProVisual class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProVisual()
        self.assertIsInstance(instance, ProVisual)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProVisual()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
