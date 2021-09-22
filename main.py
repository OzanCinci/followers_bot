import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
print("Login your information")
username = input("username: ")
pw = input("password: ")


class Instagram_bot:

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.driver = webdriver.Chrome()

    def Sign_In(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(3)

        userName = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        pW = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')

        userName.send_keys(self.user_name)
        pW.send_keys(self.password)
        time.sleep(1)

        button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
        button.click()
        time.sleep(1)

    def skipp(self):
        time.sleep(4)
        if self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button'):
            button1 = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/div/div/button')
            button1.click()
            time.sleep(4)

        if self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]'):
            button2 = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div/div[3]/button[2]')
            button2.click()
            time.sleep(4)

    def getProfile(self):
        time.sleep(1)
        profile_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a')
        profile_button.click()

    def getFollowers(self):
        time.sleep(3)
        button_followers = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        button_followers.click()
        time.sleep(3)

        dialog = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[2]')
        time.sleep(2)

        count = len(self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[2]/ul/div').find_elements_by_tag_name('li'))

        action = webdriver.ActionChains(self.driver)

        while True:
            for i in range(10):
                dialog.click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(2)
            new_count = len(self.driver.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/ul/div').find_elements_by_tag_name('li'))
            if count != new_count:
                count = new_count
            else:
                break

        takip = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[2]/ul/div').find_elements_by_tag_name('li')
        with open("takipciler.txt", "w", encoding='UTF-8') as file:
            for takipci in takip:
                G = takipci.find_element_by_tag_name(
                    'a').get_attribute('href')[26:]
                G = G[:-1]
                file.write(G+'\n')

        time.sleep(2)
        closeing_button = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[1]/div/div[2]/button')
        closeing_button.click()

    def getFollowing(self):
        time.sleep(2)
        following_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[3]')
        following_button.click()
        time.sleep(3)

        dialog = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[3]/ul')
        time.sleep(2)

        count = len(self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[3]/ul/div').find_elements_by_tag_name('li'))

        action = webdriver.ActionChains(self.driver)

        while True:
            for i in range(10):
                dialog.click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(2)
            new_count = len(self.driver.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[3]/ul/div').find_elements_by_tag_name('li'))
            if count != new_count:
                count = new_count
            else:
                break

        takip = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[3]/ul/div').find_elements_by_tag_name('li')
        with open("takip_edilenler.txt", "w", encoding='UTF-8') as file:
            for takipci in takip:
                G = takipci.find_element_by_tag_name(
                    'a').get_attribute('href')[26:]
                G = G[:-1]
                file.write(G+'\n')

        time.sleep(2)
        closeing_button = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[1]/div/div[2]/button')
        closeing_button.click()

    def diff(self):
        with open("takip_edilenler.txt", "r", encoding="UTF-8") as file_takip_edilen:
            with open("takipciler.txt", "r", encoding="UTF-8") as file_takipci:
                liste_takiciler = file_takipci.readlines()
                liste_takip_edilen = file_takip_edilen.readlines()
                with open("diff.txt", "w", encoding="UTF-8") as difference:
                    for takip_ettigin in liste_takip_edilen:
                        if takip_ettigin not in liste_takiciler:
                            difference.write(
                                takip_ettigin[:-1]+' seni takip etmiyor.\n')

    def Closer(self):
        time.sleep(2)
        self.driver.close()


app = Instagram_bot(username, pw)
app.Sign_In()
app.skipp()
app.getProfile()
app.getFollowers()
app.getFollowing()
app.diff()
app.Closer()
