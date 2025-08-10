# test_campaignmanager.py
"""
Tests for CampaignManager module.
"""

import unittest
from campaignmanager import CampaignManager

class TestCampaignManager(unittest.TestCase):
    """Test cases for CampaignManager class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CampaignManager()
        self.assertIsInstance(instance, CampaignManager)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CampaignManager()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
