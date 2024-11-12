from abc import ABC, abstractmethod

class User(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """
    def __init__(self, userName, passWord):
        self.userName = userName
        self.role = self.__class__.__name__
        self.passWord=passWord
    # These operations already have implementations.
        
    #Gets the username of the 
    def getUserName(self) ->str:
        return self.userName
    
    def getRole(self) ->str:
        return self.role
    
    def display_info(self):
        """Template method that displays user info."""
        print(f"User: {self.userName}")
        print(f"Role: {self.role}")
        # print("Permissions:")
        # for permission in self.get_permissions():
        #     print(f"- {permission}")

    # Abstract method for each concrete subclass  to implement 
    @abstractmethod
    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass

    