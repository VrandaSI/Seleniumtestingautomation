from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def scroll():
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 3):
        driver.execute_script("window.scrollTo(0, {});".format(i))
    for i in range(total_height, 1, -3):
        driver.execute_script("window.scrollTo(0, {});".format(i))


PATH = "C:\\Users\VRANDA\Downloads\chromedriver_win32.zip\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.thesparksfoundationsingapore.org")
print("Testing", driver.title)

driver.maximize_window()
time.sleep(10)

print("\nCase 1: Logo Verification\n")
try:
    driver.find_element(by=By.XPATH, value="//img[@src='/images/logo_small.png']")
    time.sleep(3)
    print(" Logo exists\n")
except NoSuchElementException:
    print(" Logo Does Not Exist\n")


print("Case 2: Navigation Bar Appearance\n")
try:
    driver.find_element(by=By.ID, value="link-effect-3")
    time.sleep(3)
    print("Navigation Bar Appears\n")
except NoSuchElementException:
    print(" Navigation Bar Does Not Appear\n")


print("Case 3: Expert Mentors Page Content Verification\n")
try:
    driver.find_element(by=By.LINK_TEXT, value="About Us").click()
    time.sleep(3)
    driver.find_element(by=By.LINK_TEXT, value="Expert Mentors").click()
    time.sleep(3)
    driver.find_element(by=By.TAG_NAME, value='h3')
    print("Expert Mentors Page Exist\n")

except NoSuchElementException:
    print(" Expert Mentors Page Does Not Exist\n")


print("Case 4: Workshops Page Verification\n")
try:
    driver.find_element(by=By.LINK_TEXT, value='Programs').click()
    time.sleep(3)
    driver.find_element(by=By.LINK_TEXT, value="Workshops").click()
    time.sleep(3)
    driver.find_element(by=By.LINK_TEXT, value='LEARN MORE').click()
    time.sleep(3)
    print("Workshops Page Exists\n")

except NoSuchElementException:
    print(" Workshops Page Does Not Exist\n")


print("Case 5: Links App Page Verification\n")
try:
    driver.find_element(by=By.LINK_TEXT, value="LINKS App").click()
    time.sleep(3)
    print(" Links App Page Exists\n")

except NoSuchElementException:
    print(" Links App Page Does Not Exist\n")
time.sleep(3)
handles = driver.window_handles

for i in handles:
    driver.switch_to.window(i)

    # close specified web page
    if driver.title == "Frames & windows":
        time.sleep(2)
        driver.close()
time.sleep(3)


print("Case 6: Map Authentication\n")
try:
    driver.find_element(by=By.LINK_TEXT, value="Contact Us").click()
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value="map-agileits")
    time.sleep(5)
    print(" Map Exists\n")

except NoSuchElementException:
    print(" Map Does Not Exist\n")



print("Case 7: Student Externships Program Verification\n")
try:
    driver.find_element(by=By.LINK_TEXT, value="Student Externships Program").click()
    time.sleep(3)
    driver.find_element(by=By.TAG_NAME, value='h3')
    time.sleep(3)
    scroll()
    time.sleep(0.5)
    print(" Student Externships Page Is Undone\n")

except NoSuchElementException:
    print(" Student Externships Page Is Done\n")


print("Case 8: Navigation Bar Widgets Verification\n")
try:
    driver.find_element(by=By.LINK_TEXT, value="Programs").click()
    time.sleep(1)
    driver.find_element(by=By.LINK_TEXT, value="LINKS").click()
    time.sleep(1)
    driver.find_element(by=By.LINK_TEXT, value="Join Us").click()
    time.sleep(1)
    driver.find_element(by=By.LINK_TEXT, value="Contact Us").click()
    time.sleep(1)
    print(" Navigation Bar Widget Exists\n")

except NoSuchElementException:
    print(" Navigation Bar Widget Does Not Exist")


print("Case 9: Facebook Widget Authentication\n")
try:
    driver.find_element(by=By.LINK_TEXT, value="About Us").click()
    time.sleep(3)
    driver.find_element(by=By.LINK_TEXT, value="News").click()
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value='fb-page')
    time.sleep(5)
    print(" Facebook Widget Exists\n")


except NoSuchElementException:
    print(" Facebook Widget Does Not Exist")


print("Case 10: Copyright Notice Appearance\n")
try:
    driver.find_element(by=By.CLASS_NAME, value='copyright-wthree')
    time.sleep(3)
    print(" Copyright Notice Appears\n")

except NoSuchElementException:
    print(": Copyright Notice Does Not Appear\n")


print("Tested for 6 pages and 10 elements \n")
time.sleep(3)
