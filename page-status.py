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

correct_first_line = 'This dashboard shows the results of Google Cloud Inter-Region latency and throughput benchmarks. ' #The first test will involve checking whether the title of the report appears
correct_second_line = 'sending_region' #The second test will check whether one of the filters on the first table. first page has loaded
correct_third_line = 'sending_thread_count: 32' #The third test will check whether one of the filteres on the second table, first page has loaded
correct_fourth_line = 'sending_region' #The fourth test will check whether one of the filters on the first table, second page has loaded
correct_fifth_line = 'sending_region' #The fifth test will check whether one of the filters on the second table, second page has loaded
correct_sixth_line = 'sending_region' #The sixth test will check whether one of the filters on the third table, second page has loaded
correct_seventh_line = 'sending_region' #The seventh test will check whether one of the filters on the first table, third page has loaded
correct_eighth_line = 'sending_region' #The eighth test will check whether one of the filters on the second table, third page has loaded
correct_ninth_line = 'sending_region' #The ninth test will check whether one of the filters on the third table, third page has loaded

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3") #hides uneccesary messages
options.add_argument("headless") #prevents a giant pop-up browser from appearing on screen
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def execute_test():
    global first_line #Declaring Test Results as Global Variables
    global second_line
    global third_line
    global fourth_line
    global fifth_line
    global sixth_line
    global seventh_line
    global eighth_line
    global ninth_line
    try:
        driver.get(test_url) #Running URL on Chrome Driver
        time.sleep(3) #Allow for Loading Time
        #Execute First Test
        first_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(20) > canvas-component > div > div > div > div > textbox > div > div:nth-child(1) > div:nth-child(1) > font > font').text
    except NoSuchElementException:
        print("Loading of Report Failed")
        return False
    driver.get(test_url) #Reload Webpage
    time.sleep(5)
    #Execute Second Test
    try:
        second_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(10) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 2 Failed to Execute")
        return False
    #Execute Third Test
    try:
        third_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(19) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div.content-holder.ng-scope > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 3 Failed to Execute")
        return False
    #Enter Next Page
    driver.find_element_by_css_selector('#reporting-app-header > md-toolbar > div > div.ng-scope.flex > page-navigation > div > div > div.ng-scope > div > span.navBtn.nextBtn').click()
    time.sleep(5)
    #Execute Fourth Test
    try:
        fourth_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(11) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 4 Failed to Execute")
        return False
    #Execute Fifth Test
    try:
        fifth_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(21) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 5 Failed to Execute")
        return False
    #Execute Sixth Test
    try:
        sixth_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(28) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 6 Failed to Execute")
        return False
    #Enter Next Page
    driver.find_element_by_css_selector('#reporting-app-header > md-toolbar > div > div.ng-scope.flex > page-navigation > div > div > div.ng-scope > div > span.navBtn.nextBtn').click()
    time.sleep(5)
    #Execute Seventh Test
    try:
        seventh_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(11) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 7 Failed to Execute")
        return False
    #Execute Eighth Test
    try:
        eighth_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(22) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 8 Failed to Execute")
        return False
    #Execute Ninth Test
    try:
        ninth_line = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(30) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text
    except NoSuchElementException:
        print("Test 9 Failed to Execute")
        return False
    driver.quit()

def confirm_page():
    state = 0
    if first_line != correct_first_line:
        print("Report Failed to Meet Loading Requirements")
        state += 1
    if second_line != correct_second_line:
        print("Table 1 on Page 1 Encountered a Disruption")
        state += 1
    if third_line != correct_third_line:
        print("Table 2 on Page 1 Encountered a Disruption")
        state += 1
    if fourth_line != correct_fourth_line:
        print("Table 1 on Page 2 Encountered a Disruption")
        state +=1
    if fifth_line != correct_fifth_line:
        print("Table 2 on Page 2 Encountered a Disruption")
        state +=1
    if sixth_line != correct_sixth_line:
        print("Table 3 on Page 2 Encountered a Disruption")
        state +=1
    if seventh_line != correct_seventh_line:
        print("Table 1 on Page 3 Encountered a Disruption")
        state +=1
    if eighth_line != correct_eighth_line:
        print("Table 2 on Page 3 Encountered a Disruption")
        state +=1
    if ninth_line != correct_ninth_line:
        print("Table 3 on Page 3 Encountered a Disruption")
        state +=1
    if state == 0:
        print("\nPage is Up and Running!\n")
        return True
    else:
        print("\nTotal Number of Errors: " + str(state))
        return False

execute_test()
confirm_page()