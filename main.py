from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstaBot():

    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwdInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwdInput.send_keys(self.password)
        passwdInput.submit()
        time.sleep(3)

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        followbtn = self.browser.find_element_by_css_selector('button')
        web_uname = self.browser.find_elements_by_css_selector('h1')[1]
        uname = web_uname.text
        if (followbtn.text == 'Following'):
            print("You're already following " + uname)
        else:
            followbtn.click()

            print("You have followed " + uname + " successfully.")

    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        followbtn = self.browser.find_element_by_css_selector('button')
        web_uname = self.browser.find_elements_by_css_selector('h1')[1]
        uname = web_uname.text
        if (followbtn.text == 'Following'):
            followbtn.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
            print("Unfollowed " + uname+ " successfully.")
        else:
            print("You are not following " + uname)

    def getUserFollowers(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)

        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break

        return followers

        def closeBrowser(self):
            self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()
