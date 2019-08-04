from selenium import webdriver


# driver.find_element_by_xpath('//*[@id="navId"]/li/a[text()="数据查询"]').click()

class Alms_Login(object):
    def __init__(self, url, username, password):
        self.url=url,
        self.username=username,
        self.password=password

    def login(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')

        driver = webdriver.Chrome(options=option)
        driver.maximize_window()
        url = self.url.tostring()
        driver.get(url)

        driver.find_element_by_id("txtAccount_I").send_keys(self.username)
        driver.find_element_by_id("txtPwd_I").send_keys(self.password)
        driver.find_element_by_id("btnLogin").click()


if __name__ == '__main__':
    Alms_Login(
        url='http://191.168.6.6:8180/xalms/login.action',
        username='xqa',
        password='123456'
    ).login()
