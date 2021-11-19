from selenium import webdriver
#creating a login page object.

class login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktest="Logout"

#need to implement action methods for above locator
# created the constructor to initialize the drivers
#mentioned driver will come from actual driver testcase
    def __init__(self,driver):
        self.driver=driver

#mention action methods for mentioned locators
    def setUserName(self,username):
         self.driver.find_element_by_id(self.textbox_username_id).clear()
         self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassWord(self,password):
         self.driver.find_element_by_id(self.textbox_password_id).clear()
         self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self): #not passing any arguments as its click action
         self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self): #not passing any arguments as its click action
         self.driver.find_element_by_link_text(self.link_logout_linktest).click()



