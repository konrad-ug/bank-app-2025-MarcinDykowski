import unittest
from unittest.mock import Mock, patch, MagicMock
from src.personal_acount import PersonalAccount
from src.mongo_accounts_repository import MongoAccountsRepository

class TestMongoRepository(unittest.TestCase):
    
    @patch('src.mongo_accounts_repository.MongoClient')
    def test_save_all(self, mock_mongo_client):
        # Mock kolekcji
        mock_collection = MagicMock()
        mock_mongo_client.return_value.__getitem__.return_value.__getitem__.return_value = mock_collection
        
        repo = MongoAccountsRepository()
        account = PersonalAccount("Jan", "Kowalski", "12345678901")
        
        repo.save_all([account])
        
        mock_collection.delete_many.assert_called_once_with({})
        assert mock_collection.update_one.called