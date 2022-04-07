from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

links_file = pd.read_excel('whatsapp_groups.xlsm')
PATH = "D:\THE\Projects\WhatsApp\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Type Your Message Here
message = 'Hello everyone! please join my channel.'

driver.get('https://web.whatsapp.com/')
print(driver.title)

time.sleep(15)

# Type The name of the person or the group you want to send a message to
user_name = 'google nerds' # Example: I created a group with myself and called it "google nerds"
                        # so the messages get sent there

# I choose the first 3 links in the excel sheet only, you can ofcourse specify more.
for i in range(3):

    group_link = links_file.iloc[i,1]
    # Search For The person's name and click enter
    user = driver.find_element_by_xpath(f'//span[@title="{user_name}"]')
    user.click()

    # Search for the text box and type the message, then send enter
    time.sleep(1)
    message_box = driver.find_element_by_xpath('//div[@title="Type a message"]')
    time.sleep(1)

    message_box.send_keys(group_link)
    time.sleep(1)
    message_box.send_keys(Keys.RETURN)

    link_text = driver.find_element_by_xpath(f'//a[@title="{group_link}"]')
    link_text.send_keys(Keys.RETURN)

    join_group = driver.find_element_by_xpath('//div[@class="_20C5O _2Zdgs"]')
    join_group.send_keys(Keys.RETURN)

time.sleep(30)