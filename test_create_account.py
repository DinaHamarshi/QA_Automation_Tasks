import pytest
import pytest_html
from baseclass import Basic_Test

class CreateAccountTests(Basic_Test):

    @pytest.mark.parametrize("FirstName, LastName, Email, Password, ConfirmPass", 
                             [
                                 ("ulqem", "qjejftqls", "qeieeltk@gmail.com", "#$ecq9tlkieop789$z", "#$ecq9tlkieop789$z"), #positive scenario
                                 ("Dina", "Hamarshi", "dina2024@gmail.com", "abc456iop789$", "abc4568974561"), #unmatched confirm password
                                 ("Dina", "Hamarshi", "dina2024gmail.com", "abc456iop789$", "abc456iop789$"), #invalid email format
                                 ("Dina", "Hamarshi", "dina2024@gmail.com", "456798", "456789") #invalid password

                             ])
    
    def test_create_account(self, FirstName, LastName, Email, Password, ConfirmPass):
        
        self.create_account_method(FirstName, LastName, Email, Password, ConfirmPass)
        title = "My Account"
        assert title == self.driver.title, "Account Creation Failed!" 

    