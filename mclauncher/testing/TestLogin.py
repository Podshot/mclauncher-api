import getpass
import uuid
from mclauncher.implementation.login import YDLogin

if __name__ == "__main__":
    username = raw_input("Username: ")
    password = getpass.getpass("Password: ")
    YDLogin.YDPasswordLogin(username, password, str(uuid.uuid4()))

    
    
