import allure


class Test01():
    def test_01(self):
        print("aaaa")
        assert 1
    @allure.step(title="测试登陆的流程")
    def test_02(self):
        allure.attach("登陆","输入用户名")
        print("bbbb0")
        allure.attach("登陆","输入密码")
        print("bbbb1")
        allure.attach("登陆","点击登陆")
        print("bbb22")
        assert 1
