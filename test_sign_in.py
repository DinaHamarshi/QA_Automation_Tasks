import pytest
import pytest_html
from baseclass import Basic_Test

class SignInTests(Basic_Test):

    @pytest.mark.parametrize("Email, Password", 
                             [
                                 ("dina2024@gmail.com", "abc456iop789$"), #positive scenario
                                 ("dina2024gmail.com", "abc456iop789$"), #invalid email format
                                 ("dina2024@gmail.com", "456798"), #incorrect password
                                 ("dina2024@gmail.com", "") #empty password field
                             ])
    
    def test_sign_in(self, Email, Password):
        
        self.sign_in_method(Email, Password)
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/", "Signing-In Failed!"
 
