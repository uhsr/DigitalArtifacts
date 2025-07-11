# test_digitalartifacts.py
"""
Tests for DigitalArtifacts module.
"""

import unittest
from digitalartifacts import DigitalArtifacts

class TestDigitalArtifacts(unittest.TestCase):
    """Test cases for DigitalArtifacts class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalArtifacts()
        self.assertIsInstance(instance, DigitalArtifacts)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalArtifacts()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
