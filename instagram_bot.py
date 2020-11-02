from selenium import webdriver
from time import sleep
import conturi

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com')
        sleep(1)
        user_name = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(conturi.user_attacker)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(conturi.parola_attacker)
        accept_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        accept_btn.click()
        submit_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        submit_button.click()
        sleep(3)
        not_now = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
        sleep(1)
        not_now_2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_2.click()
        self.driver.get('https://www.instagram.com/direct/inbox')
        search_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')
        search_button.click()
        search_field = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')
        search_field.send_keys(conturi.user_victima)
        sleep(3)
        cerc = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]')
        cerc.click()
        next_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button')
        next_button.click()
        sleep(2)
        text_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        for i in range(0,5):
            text_input.send_keys('haha')
            sleep(1)
            send_text = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
            send_text.click()
        # text_input.send_keys('sal')
        # send_text = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        # send_text.click()

        # while True:
        #     try:
        #         verificare = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[47]/div')    
        #         text_input.send_keys('t e s t')
        #         sleep(1)
        #         send_text = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        #         send_text.click()
        #     except:
        #         print('astept raspuns')
        sleep(1)
        text_input.send_keys('haha you just got memed by a bot')
        send_text = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        send_text.click()


def main():
    my_bot = Bot()

main()

