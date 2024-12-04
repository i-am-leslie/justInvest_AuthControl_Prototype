import unittest
from unittest.mock import patch, mock_open
from System.JustInvestSystem  import JustInvestSystem, PasswordFile


class TestJustInvestSystemLogin(unittest.TestCase):
    def setUp(self):
        """Set up the system instance for each test."""
        self.system = JustInvestSystem()

    # @patch("builtins.open", new_callable=mock_open, read_data="testuser1:salt1234567890abcdef:1234abcdhashed:Client\n")
    # def test_successful_login(self, mock_file):
    #     """Test login with correct credentials."""
    #     # Mock password file behavior
    #     password_file = PasswordFile()
    #     hashed_password = password_file.hash_password("password123", "salt1234567890abcdef")
        
    #     # Simulate correct credentials in the mocked password file
    #     with patch.object(password_file, "get_record", return_value={
    #         "username": "testuser1",
    #         "salt": "salt1234567890abcdef",
    #         "hashed_password": hashed_password,
    #         "role": "Client"
    #     }):
    #         role = self.system.login("testuser1", "password123")
    #         self.assertEqual(role, "Client", "Login should succeed and return the user's role.")

    @patch("builtins.open", new_callable=mock_open, read_data="testuser1:salt1234567890abcdef:1234abcdhashed:Client\n")
    def test_failed_login_incorrect_password(self, mock_file):
        """Test login with incorrect password."""
        password_file = PasswordFile()
        with patch.object(password_file, "get_record", return_value={
            "username": "testuser1",
            "salt": "salt1234567890abcdef",
            "hashed_password": "incorrecthashedpassword",
            "role": "Client"
        }):
            role = self.system.login("testuser1", "wrongpassword")
            self.assertIsNone(role, "Login should fail with incorrect password.")

    @patch("builtins.open", new_callable=mock_open, read_data="testuser1:salt1234567890abcdef:1234abcdhashed:Client\n")
    def test_failed_login_nonexistent_user(self, mock_file):
        """Test login with a non-existent user."""
        password_file = PasswordFile()
        with patch.object(password_file, "get_record", return_value=None):
            role = self.system.login("nonexistentuser", "password123")
            self.assertIsNone(role, "Login should fail for non-existent users.")

    def test_get_record_file_not_found(self):
        """Test behavior when the password file does not exist."""
        password_file = PasswordFile("nonexistent_file.txt")
        with self.assertRaises(FileNotFoundError):
            password_file.get_record("testuser1")


if __name__ == "__main__":
    unittest.main()
