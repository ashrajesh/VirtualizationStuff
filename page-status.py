# TASK:
# Simple python script to check whether or not the page is up and running and that the data is loading in properly.
# If it is up and data is loaded properly, return true, and return false otherwise.
# https://datastudio.google.com/u/0/reporting/fc733b10-9744-4a72-a502-92290f608571/page/70YCB


# This program assumes the internet connection is relatively fast and stable
# This program assumes the loading of the filter at that bottom of the table correlates to the successful loading of data
# This program assumes that the data studio report content, pages, filters remain unchanged (otherwise changes to the tests and lists will be required)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from webdriver_manager.chrome import ChromeDriverManager

test_url = "https://datastudio.google.com/u/0/reporting/fc733b10-9744-4a72-a502-92290f608571/page/70YCB" #This is the Data-studio link we will be testing

test_lines = [] # Contains all of the test results gathered from selenium
correct_lines = [] # Contains all of the desired (correct) results

correct_lines.append('This dashboard shows the results of Google Cloud Inter-Region latency and throughput benchmarks. ') #The first test will involve checking whether the title of the report appears
for x in range(8):
    correct_lines.append('sending_region') #The rest of the tests will check whether the sending_region filter has been loaded on all 8 tables

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3") #hides uneccesary messages
options.add_argument("headless") #prevents a giant pop-up browser from appearing on screen
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def execute_test():
    global test_lines #Declaring Test Results as Global Variables
    global temp
    try:
        driver.get(test_url) #Running URL on Chrome Driver
        time.sleep(3) #Allow for Loading Time
        #Execute First Test
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(20) > canvas-component > div > div > div > div > textbox > div > div:nth-child(1) > div:nth-child(1) > font > font').text 
    except NoSuchElementException:
        print("Loading of Report Failed")
        return False
    test_lines.append(temp)
    driver.get(test_url) #Reload Webpage
    time.sleep(5)
    #Execute Second Test
    try:
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(10) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 2 Failed to Execute (Table 1, Page 1)")
        return False
    test_lines.append(temp)
    #Execute Third Test
    try:
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(17) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 3 Failed to Execute (Table 2, Page 1)")
        return False
    test_lines.append(temp)
    #Enter Next Page
    driver.find_element_by_css_selector('#reporting-app-header > md-toolbar > div > div.ng-scope.flex > page-navigation > div > div > div.ng-scope > div > span.navBtn.nextBtn').click()
    time.sleep(5)
    #Execute Fourth Test
    try:
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(11) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text  
    except NoSuchElementException:
        print("Test 4 Failed to Execute (Table 1, Page 2)")
        return False
    test_lines.append(temp)
    #Execute Fifth Test
    try:
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(21) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 5 Failed to Execute (Table 2, Page 2)")
        return False
    test_lines.append(temp)
    #Execute Sixth Test
    try:
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(28) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 6 Failed to Execute (Table 3, Page 2)")
        return False
    test_lines.append(temp)
    #Enter Next Page
    driver.find_element_by_css_selector('#reporting-app-header > md-toolbar > div > div.ng-scope.flex > page-navigation > div > div > div.ng-scope > div > span.navBtn.nextBtn').click()
    time.sleep(5)
    #Execute Seventh Test
    try:
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(11) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 7 Failed to Execute (Table 1, Page 3)")
        return False
    test_lines.append(temp)
    #Execute Eighth Test
    try:
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(22) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 8 Failed to Execute (Table 2, Page 3)")
        return False
    test_lines.append(temp)
    #Execute Ninth Test
    try:
        temp = driver.find_element_by_css_selector('#body > div > div > div.lego-reporting-view.activity-view.no-licensed > div.page > div > div.mainBlock.ng-scope > div > div.scaleSizeHolder > div > lego-report > lego-canvas-container > div > file-drop-zone > span > content-section > div:nth-child(30) > canvas-component > div > div > div > div > dimension-filter-control > simple-dimension-filter > control-layout-wrapper > button > div > span.lego-control-section.label > span.main-text > main-section').text 
    except NoSuchElementException:
        print("Test 9 Failed to Execute (Table 3, Page 4)")
        return False
    test_lines.append(temp)
    driver.quit()

def confirm_page():
    state = 0
    try:
        if test_lines[0] != correct_lines[0]:
            print("Report Failed to Meet Loading Requirements")
            state += 1
    except:
        print("Report Failed to Meet Loading Requirements")
        return False
    try:
        for y in range(8):
            z = y + 1
            if test_lines[z] != correct_lines[z]:
                print("Table "+str(z)+" Encountered a Disruption")
                state += 1
    except IndexError:
        print("\nPlease Tend to Faulty Table Listed Above.")
        return False
    if state == 0:
        print("\nPage is Up and Running!\n")
        return True
    else:
        print("\nTotal Number of Errors: " + str(state))
        return False

execute_test() # Executes all 9 tests
confirm_page() # Compares results gathered to desired results