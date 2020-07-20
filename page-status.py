# TASK:
# Simple python script to check whether or not the page is up and running and that the data is loading in properly.
# If it is up and data is loaded properly, return true, and return false otherwise.
# https://datastudio.google.com/u/0/reporting/fc733b10-9744-4a72-a502-92290f608571/page/70YCB


# This program assumes your internet connection is relatively fast
# This program assumes the loading of the filter at that bottom of the table correlates to the successful loading of data
# This program assumes that the data studio report content, filters remain unchanged (otherwise changes to this test will be required)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from webdriver_manager.chrome import ChromeDriverManager

test_url = "https://datastudio.google.com/u/0/reporting/fc733b10-9744-4a72-a502-92290f608571/page/70YCB" #This is the Data-studio link we will be testing
#The first test will involve checking whether the title of the report appears
correct_first_line = 'This dashboard shows the results of Google Cloud Inter-Region latency and throughput benchmarks. '
#The second test will check whether one of the filters on the first table. first page has loaded
correct_second_line = 'sending_region'
#The third test will check whether one of the filteres on the second table, first page has loaded
correct_third_line = 'sending_thread_count: 32'
#The fourth test will check whether one of the filters on the last table, second page has loaded
correct_fourth_line = 'metric: Average Latency'
#The fifth test will check whether one of the filters on the last table, third page has loaded
correct_fifth_line = 'ip_type: internal'

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3") #hides uneccesary messages
options.add_argument("headless") #prevents a giant pop-up browser from appearing on screen
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def execute_test():
    #Declaring Test Results as Global Variables
    global first_line
    global second_line
    global third_line
    global fourth_line
    global fifth_line
    try:
        #Running URL on Chrome Driver
        driver.get(test_url)
        #Allow for Loading Time
        time.sleep(3)
        #Execute First Test
        first_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(20) > canvas-component > div > div > div > div > textbox > div > div:nth-child(1) > div:nth-child(1) > font > font').text
    except NoSuchElementException:
        print("Loading Failed")
        return False
    #Reload Webpage
    driver.get(test_url)
    time.sleep(5)
    #Execute Second and Third Tests
    try:
        second_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(10) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text
        third_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(19) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div.content-holder.ng-scope > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 2, Test 3 Failed to Execute")
        return False
    #Enter Next Page
    driver.find_element_by_css_selector('#reporting-app-header > md-toolbar > div > div.ng-scope.flex > page-navigation > div > div > div.ng-scope > div > span.navBtn.nextBtn').click()
    time.sleep(5)
    #Execute Fourth Test
    try:
        fourth_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(29) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 4 Failed to Execute")
        return False
    #Enter Next Page
    driver.find_element_by_css_selector('#reporting-app-header > md-toolbar > div > div.ng-scope.flex > page-navigation > div > div > div.ng-scope > div > span.navBtn.nextBtn').click()
    time.sleep(5)
    #Execute Fifth Test
    try:
        fifth_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(28) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 5 Failed to Execute")
        return False
    driver.quit()

def confirm_page():
    if first_line != correct_first_line:
        print("Test 1 Failed")
        return False
    if second_line != correct_second_line:
        print("Test 2 Failed")
        return False
    if third_line != correct_third_line:
        print("Test 3 Failed")
        return False
    print("Page is Up and Running!")
    if fourth_line != correct_fourth_line:
        print("Test 4 Failed")
        return False
    if fifth_line != correct_fifth_line:
        print("Test 5 Failed")
        return False
    return True

execute_test()
confirm_page()