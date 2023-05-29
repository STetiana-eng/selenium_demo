import requests

class UserRegistratin:
    def __init__(self, name, lastName, email, password, repeatPassword):
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password
        self.repeatPassword = repeatPassword

    def user_registration(self):
        self.session = requests.session()
        self.user_register = UserRegistratin(name="www", lastName="First", email="feg@test.com", password="Qwerty12345",
                                             repeatPassword="Qwerty12345")
        self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_register.__dict__)
        assert result.json()["status"] == "ok"

class Userlogin(UserRegistratin):
    def __init__(self, name, lastName, email, password, repeatPassword, remember):
        UserRegistratin.__init__(self, name, lastName, email, password, repeatPassword)
        self.remember = remember

    # def user_login(self):
    #     self.user_login = Userlogin(UserRegistratin)
    #     result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_login.__dict__)
    #     assert result.json()["status"] == "ok"





class TestAutho:
    def test_setup_class(self):
        self. userreg = UserRegistratin


    def test_setup_method_login(self):
        self.session = requests.session()
        self.user_register()
        self.user_login = Userlogin
        result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_login.__dict__)
        assert result.json()["status"] == "ok"

    def test_user_registration(self):
        self.user_registration()


    # def test_delete_user(self):
    #     result = self.session.delete("https://qauto2.forstudy.space/api/users")
    #     assert result.json()["status"] == "ok"
