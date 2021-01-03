from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from colorama import Fore, Back, Style
from colorama import init
import time
import random

if __name__ == '__main__':
    pass
else:
    print('Run this directly')
    exit(0)
init()
print("This script is used to know what social media account that an email have")
time.sleep(1)
print("")
print('You must have a FAST and STABLE internet connection to get accurate results')
time.sleep(1)
print("")

twitter_occupied = False
insta_occupied = False
facebook_occupied = False
github_occupied = False
amazon_occupied = False
adobe_occupied = False
email_compromised = False
errors = []
# references are looked at id, as params.
email = input('Enter the email of person to search for:: ').lower()

username = email.split('@')[0]
domain = email.split('@')[1]
password = 'Password123@'
delay = 5  # make a option to change delay this for more accuracy...

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
#driver = webdriver.Firefox()
print('-----------------------------------------')
print('Started')

#haveibeenpwnd
driver.get('https://haveibeenpwned.com/')
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Account"]')))
    driver.find_element_by_xpath('//*[@id="Account"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="searchPwnage"]').click()
    desired = '//*[@id="loading"][@style="display: none;"]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, desired)))
    h2_text = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/h2').text
    if h2_text == 'Good news — no pwnage found!':
        email_compromised = False
    else:
        email_compromised = True
except TimeoutException as e:
    errors.append('Pwned page has changed please look at page again and refactor code.')
if email_compromised:
    print(Fore.BLACK+Back.MAGENTA+'Email - Compromised Password Found')
elif not email_compromised:
    print(Fore.BLACK+Back.CYAN+'Email - Not Compromised')



#twitter
driver.get('https://twitter.com/i/flow/signup')  # need a delay for website to load.

WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Use email instead"]/parent::div')))
# print('Page is ready!')
link = driver.find_element_by_xpath('//span[text()="Use email instead"]/parent::div')
link.click()
time.sleep(3)

mail = driver.find_element_by_name('email')
mail.send_keys(email)
time.sleep(3)

try:
    notif = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/div/span')
    if notif.text == "Email has already been taken.":
        twitter_occupied = True
except:
    twitter_occupied = False


        # driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/label/div/div[2]/div/input').click()
        # driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input').click()
        # print('Got Twitter Login Page')

if twitter_occupied:
    print(Fore.BLACK+Back.GREEN+'Twitter - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Twitter - Email Not Found')





# #instagram
driver.get('https://www.instagram.com')
try:
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[1]/div/label/input')))
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[1]/div/label/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[2]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[2]/div/label/input').send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="slfErrorAlert"]')))
    alert = driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')

    if(alert.text == "The username you entered doesn't belong to an account. Please check your username and try again."):
        instagram_occupied = False
    else:
       instagram_occupied = True

except:
    errors.append('Instagram page has changed please look at page again and refactor code.')


if instagram_occupied:
    print(Fore.BLACK+Back.GREEN+'Instagram - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Instagram - Email Not Found')



#facebook
driver.get('https://www.facebook.com')
try:
    email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(Keys.RETURN)
    time.sleep(3)

   
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]')))
        alert = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]')
        if(alert.text == "Email yang Anda masukkan tidak cocok dengan akun mana saja. Buat sebuah akun."):
            facebook_occupied = False
        

    except:
        facebook_occupied = True
        

except:
    errors.append('Facebook page has changed please look at page again and refactor code.')


if facebook_occupied:
    print(Fore.BLACK+Back.GREEN+'Facebook - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Facebook - Email Not Found')




# github
driver.get('https://github.com/join')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="user_email"]')))
    email_input = driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="user_password"]').click()
    driver.find_element_by_xpath('//*[@id="user_email"]').click()
except TimeoutException:
    errors.append('Github page has changed please look at page again and refactor code.')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'error')))
    github_elmnt = driver.find_element_by_class_name('error')
    github_occupied = True
except TimeoutException:
    github_occupied = False
    errors.append('Github Timeout/ Element cannot be found anymore.')
if github_occupied:
    print(Fore.BLACK+Back.GREEN+'Github - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Github - Email Not Found')


#amazon
driver.get('https://www.amazon.co.uk/')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="nav-link-accountList"]')))
    driver.find_element_by_xpath('//*[@id="nav-link-accountList"]').click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="ap_email"]')))
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="continue"]').click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/h4')))
        amazon_element = driver.find_element_by_tag_name('h4')
        if amazon_element.text == 'There was a problem':
            amazon_occupied = False
        else:
            amazon_occupied = True
    except Exception as e:
        amazon_occupied = True
        errors.append('Amazon Timeout/ Element cannot be found anymore. Expected if account exists')
except Exception as e:
    errors.append('Amazon page has changed please look at page again and refactor code.')
if amazon_occupied:
    print(Fore.BLACK+Back.GREEN+'Amazon - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Amazon - Email Not Found')



#adobe
driver.get('https://auth.services.adobe.com/en_US/deeplink.html?deeplink=ssofirst&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FSunbreakWebUI1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Faccount.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%2526reauth%253Dtrue%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=SunbreakWebUI1&scope=AdobeID%2Copenid%2Cacct_mgmt_api%2Cgnav%2Csao.cce_private%2Csao.digital_editions%2Ccreative_cloud%2Cread_countries_regions%2Csocial.link%2Cunlink_social_account%2Cadditional_info.address.mail_to%2Cclient.scopes.read%2Cpublisher.read%2Cadditional_info.account_type%2Cadditional_info.roles%2Cadditional_info.social%2Cadditional_info.screen_name%2Cadditional_info.optionalAgreements%2Cadditional_info.secondary_email%2Cadditional_info.secondary_email_verified%2Cadditional_info.phonetic_name%2Cadditional_info.dob%2Cupdate_profile.all%2Csecurity_profile.read%2Csecurity_profile.update%2Cadmin_manage_user_consent%2Cadmin_slo%2Cpiip_write%2Cmps%2Clast_password_update%2Cupdate_email%2Caccount_cluster.read%2Caccount_cluster.update%2Cadditional_info.authenticatingAccount%2Creauthenticated&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2FSunbreakWebUI1%3Fredirect_uri%3Dhttps%253A%252F%252Faccount.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%2526reauth%253Dtrue%26response_type%3Dtoken&relay=a3a531b2-295f-4a4b-b482-b692d2b03c38&locale=en_US&flow_type=token&ctx_id=accmgmt&idp_flow_type=login&reauthenticate=force#/')
try:
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EmailPage-EmailField"]')))
    driver.find_element_by_xpath('//*[@id="EmailPage-EmailField"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="EmailPage-EmailField"]').send_keys(Keys.RETURN)

   
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/div/div/section/div/section/div/div/section[2]/section/form/section[1]/label')))
        alert = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div/section/div/section/div/div/section[2]/section/form/section[1]/label')
        if(alert.text == "Check your email address or create a new account"):
            adobe_occupied = False
        

    except:
        adobe_occupied=True

except:
    errors.append('Adobe page has changed please look at page again and refactor code.')


if adobe_occupied:
    print(Fore.BLACK+Back.GREEN+'Adobe - Email Found')
else:
    print(Fore.BLACK+Back.RED+'Adobe - Email Not Found')

print(" ")
print("Scan Ended")
print("-----------------------------------------")



driver.close()
driver.quit()
# # Forgot to close and alot of background process Firefox windows were running
