from src.login_module import Login
from src.form_functionality import Form


class TestExamples:
    def test_001(self):
        form = Form()
        messsage = form.enter_name("fe")
        assert messsage == "Invalid value"
        #assert 2 + 2 == 5, "Houston we've got a problem"
