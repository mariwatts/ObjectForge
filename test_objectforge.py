# test_objectforge.py
"""
Tests for ObjectForge module.
"""

import unittest
from objectforge import ObjectForge

class TestObjectForge(unittest.TestCase):
    """Test cases for ObjectForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ObjectForge()
        self.assertIsInstance(instance, ObjectForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ObjectForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
