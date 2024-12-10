from .User import User
from datetime import datetime, time
class Teller(User):


    def __init__(self, username,passWord):
        super().__init__(username,passWord)

    
    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass

    def is_business_hours():
        """Check if the current time is within business hours (9:00 AM to 5:00 PM)."""
        now = datetime.now().time()
        start_time = time(9, 0)  # 9:00 AM
        end_time = time(17, 0)   # 5:00 PM
        return start_time <= now <= end_time