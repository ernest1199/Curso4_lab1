import sys
sys.path.append("../lab1")
from src.login_module import Login
from src.form_functionality import Form


print("A")
class TestExamples:
    
    def test_001_name_has_more_than_30_chars_message(self):
        form = Form()
        actual_message = form.enter_name("Ernesto Javier Garcia Cespedes")
        assert actual_message == 'name has more than 20 chars'

    def test_002_name_is_inavlid(self):
        form = Form()
        actual_message = form.enter_name("EG")
        assert actual_message == 'Invalid value'

    def test_003_age_is_invalid(self):
        form = Form()
        actual_message = form.enter_age("24")
        assert actual_message == 'Invalid value for field age'
        
#This test is failing for me 
    def test_004_enter_email(self):
        login = Login()
        login.email = ""
        actual_message = login.validate_user()
        assert actual_message == 'Email is mandatory'
#This test is failing for me
    def test_005_enter_email2(self):
        login = Login()
        login.email = " examplemail.com"
        actual_message = login.validate_user()
        assert actual_message == 'Invalid credentials'  


    def test_006_enter_email3(self):
        login = Login()
        login.email = "example@mail.com"
        actual_message = login.validate_user()
        assert actual_message == 'Valid email format'  

    def test_007_invalid_email(self):
        login = Login()
        login.email = "AAA"
        actual_message = login.validate_user()
        assert actual_message == 'Invalid email'


    def test_008_pass_empty(self):
        login = Login()
        login.password = 'Qwert1223'
        actual_message = login.validate_password()
        assert actual_message == 'Invalid password'

    def test_009_invalid_pass(self):
        login = Login()
        login.password = 'Qwert1223'
        actual_message = login.validate_password()
        assert actual_message == 'Invalid password'

    def test_010_valid_pass(self):
        login = Login()
        login.password = 'pass1234'
        actual_message = login.validate_password()
        assert actual_message == 'Valid password'

    def test_011_test_login(self):
        login = Login()
        login.email = 'example@mail.com'
        login.password = 'pass1234'
        actual_message = login.login()
        assert actual_message == 'Login success!'