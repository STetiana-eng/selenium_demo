import requests

class UserRegistratin:
    def __init__(self, name, lastName, email, password, repeatPassword):
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password
        self.repeatPassword = repeatPassword



class Userlogin():
    def __init__(self, email, password, remember):
        self.email = email
        self.password = password
        self.remember = remember


class TestAutho:
    def setup_class(self):
        self.session = requests.session()

    def test_user_registration(self):
        self.user_register = UserRegistratin(name="Nwqweweq", lastName="First", email="nerwfdf@test.com",password="Qwerty12345", repeatPassword="Qwerty12345")
        result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_register.__dict__)
        assert result.json()["status"] == "ok"

    def test_user_login(self):
        self.user_login = Userlogin(email="oneq@test.com", password="Qwerty12345", remember=False)
        result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_login.__dict__)
        assert result.json()["status"] == "ok"

    def test_delete_user(self):
        result = self.session.delete("https://qauto2.forstudy.space/api/users")
        assert result.json()["status"] == "ok"

