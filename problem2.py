from System.JustInvestSystem import PasswordFile
import hashlib
import secrets

def test():
    # Initialize Password File
    password_file = PasswordFile()
    
    # Test Case: Salt (use a fixed salt for consistency in tests)
    salt = "00f34d4d643279adffa1fb6bd0000896"  # Fixed salt for test consistency
    
    # Test Case: Hash Password
    hashed_password = password_file.hash_password("P@ssw0rd!123", salt)
    
    # Test Case: User already exists (make sure no record exists initially)
    assert password_file.get_record('testUser') is None, "Test Case Failed, user already exists"
    
    # Test Case: Add Record
    password_file.add_record("testUser", salt, hashed_password, "Client")
    
    # Test Case: Get Record
    retrieved_record = password_file.get_record("testUser")
    
    # Assertion: Correct the key from 'user_id' to 'username'
    assert retrieved_record == {
        'username': 'testUser',  # Changed 'user_id' to 'username'
        'salt': salt,
        'hashed_password': hashed_password,
        'role': 'Client'
    }, f"Test Case Failed: {retrieved_record}"
    
    print("Test Case Passed")

if __name__ == '__main__':
    test()
