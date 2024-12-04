import unittest
import unittest
from System.JustInvestSystem import JustInvestSystem

class TestPasswordChecker(unittest.TestCase):

    def setUp(self):
        """Set up a JustInvestSystem instance for testing."""
        self.system = JustInvestSystem()
        self.system.load_weak_passwords()  # Ensure the weak passwords file is loaded

    def test_valid_password(self):
        """Test a valid password that meets all requirements."""
        password = "Valid1@Pass"
        username = "testuser"
        self.assertTrue(self.system.check_password(password, username))

    def test_password_too_short(self):
        """Test a password that is too short."""
        password = "Short1@"
        username = "testuser"
        self.assertFalse(self.system.check_password(password, username))

    def test_password_too_long(self):
        """Test a password that is too long."""
        password = "This1@PasswordIsTooLong"
        username = "testuser"
        self.assertFalse(self.system.check_password(password, username))

    def test_no_uppercase(self):
        """Test a password with no uppercase letters."""
        password = "lowercase1@"
        username = "testuser"
        self.assertFalse(self.system.check_password(password, username))

    def test_no_lowercase(self):
        """Test a password with no lowercase letters."""
        password = "UPPERCASE1@"
        username = "testuser"
        self.assertFalse(self.system.check_password(password, username))

    def test_no_digit(self):
        """Test a password with no digits."""
        password = "NoDigitsHere@"
        username = "testuser"
        self.assertFalse(self.system.check_password(password, username))

    def test_no_special_char(self):
        """Test a password with no special characters."""
        password = "NoSpecialChar1"
        username = "testuser"
        self.assertFalse(self.system.check_password(password, username))

    def test_password_matches_username(self):
        """Test a password that matches the username."""
        password = "testuser"
        username = "testuser"
        self.assertFalse(self.system.check_password(password, username))

    def test_weak_password(self):
        """Test a password that is in the common weak passwords list."""
        # Assuming "password" is in the weak password list by default
        password = "password"
        username = "testuser"
        self.assertFalse(self.system.check_password(password, username))


if __name__ == '__main__':
    unittest.main()
