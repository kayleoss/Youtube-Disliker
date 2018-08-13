from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

links = []

def initiate():
    driver.get("https://accounts.google.com/signin/v2/identifier?uilel=3&service=youtube&passive=true&hl=en&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26next%3D%252Fchannel%252FUCXN7UjITifV7EF1XgJdTOVQ%252Fvideos%26action_handle_signin%3Dtrue%26app%3Ddesktop&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(1)
    driver.find_element_by_id("identifierId").send_keys("") # Your Youtube Login Email
    driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("") # Your Youtube Login Password
    driver.find_element_by_name("password").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.get("https://www.youtube.com/channel/UCXN7UjITifV7EF1XgJdTOVQ/videos")
    for i in range(5):
        driver.execute_script("window.scrollBy(0, 2500)")
        time.sleep(1)

def grab_vid_links():
    print("GETTING ALL THEIR YOUTUBE VIDEOS' LINKS...")
    href_elements = driver.find_elements_by_css_selector("a.yt-simple-endpoint.ytd-grid-video-renderer[href]")

    for href in href_elements:
        global links
        links.append(href.get_attribute("href"))


def dislike_vids():
    print("DISLIKING ALL THEIR YOUTUBE VIDEOS...")
    for link in links:
        driver.get(link)
        time.sleep(1)
        try:
            driver.find_element_by_css_selector("button[aria-label~='dislike']").click()
        except:
            print("disliking this video did not work")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 500)")
        time.sleep(2)
        try:
            driver.find_element_by_css_selector("yt-formatted-string#simplebox-placeholder").click()
            time.sleep(1)
            driver.find_element_by_css_selector(".textarea-container > #textarea").send_keys("This is really bad.") #Enter a bad comment under their video?
            time.sleep(1)
            driver.find_element_by_css_selector("paper-button[aria-label~='Comment']").click()
        except:
            print("commenting on this video did not work")
    driver.quit()
    print("TASK COMPLETE :)")


if __name__ == "__main__":
    initiate()
    grab_vid_links()
    dislike_vids()
