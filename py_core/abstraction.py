class users:
    username="admin";
    __passwords="admin";
    
    def __init__(self, username, password):
        self.username = username
        self.__passwords = password
        
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.__passwords
    
user=users("hunk","secret_key")
print(user.get_username())
print(user.get_password())