#!/usr/bin/env python3

import os
from time import sleep
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

__author__ = 'deanypoo'

def main():
    """
    Main function that creates a new Firefox instance, logs in, prompts the user
    and starts the breeding process.

    This function does not take any parameters and does not return anything.
    """
    # Call the function to clear the screen
    clear_screen()

    print("""
                    \033[35m.''\033[0m         \033[33mPacheco Penis Pony Bot\033[0m
          \033[35m._.-.___.' (`\\\033[0m        \033[32mVersion 1.0\033[0m
         \033[35m//(\033[0m        \033[35m( `'\033[0m
          \033[35m'/ )\)__. )\033[0m          \033[36m..that's what she said..\033[0m
         \033[35m' <' `\ ._/'\ \033[0m        \033[31m ...code.by...  \u2665 \033[0m
         \033[35m  `    \     \ \033[0m       \033[91m     \u2665  ...your.slave...\033[0m
    """)

    # credentials
    # add your username/password in here
    in_user = "<username>"
    in_password = "<password>"

    # Create a new instance of the Chrome WebDriver
    driver = webdriver.Chrome()
    load_website(driver)
    store_credentials(driver, wait, in_user, in_pass)
    navigate_to_contests_page(driver, wait)
    click_award_button(driver, wait)
    navigate_to_arena_tab(driver, wait)
    click_first_link_in_unscheduled_window(driver, wait)
    click_schedule_button(driver, wait)
    confirm_popup(driver, wait)
    click_mass_signup_button(driver, wait)
    click_ok_buttons(driver, wait)
    driver.quit()
    print(":: Operation completed successfully!")

def load_website(driver):
    print(":: Loading up Chrome Browser and PonyIsland.net Website")
    url = "https://ponyisland.net"
    driver.get(url)

def store_credentials(driver, wait, in_user, in_pass):
    print(":: Enter your Username and Password.")
    user_field = _get(wait, '//*[@id="login"]/form/fieldset[1]/div/input')
    user_pass = _get(wait, '//*[@id="login"]/form/fieldset[2]/div/input')
    user_field.send_keys(in_user)
    user_pass.send_keys(in_pass)
    login_button = _get(wait, '//*[@id="login"]/form/div/button')
    login_button.click()

def navigate_to_contests_page(driver, wait):
    contests_url = "https://ponyisland.net/#!/?src=contests&sub=contests"
    print(":: Navigating to contests page")
    driver.get(contests_url)

def click_award_button(driver, wait):
    print(":: Clicking the award button")
    award_button_xpath = '/html/body/div/header/div/div[2]/nav/ul/li[5]/span/a'
    award_button = wait.until(EC.element_to_be_clickable((By.XPATH, award_button_xpath)))
    award_button.click()

def navigate_to_arena_tab(driver, wait):
    print(":: Navigating to the Arena tab")
    arena_tab_xpath = '/html/body/div/div[2]/div/div/div/div/nav/ul/li[2]/span/a'
    try:
        arena_tab = wait.until(EC.element_to_be_clickable((By.XPATH, arena_tab_xpath)))
        arena_tab.click()
        print("   - Successfully navigated to the Arena tab.")
    except TimeoutException:
        print("   - Failed to find the Arena tab within the given time.")

def click_first_link_in_unscheduled_window(driver, wait):
    print(":: Clicking the first link in the unscheduled window")
    unscheduled_xpath = '/html/body/div/div[2]/div/div/div/div/div[2]/section[3]/div/form/table/tbody/tr[1]/td[1]/a'
    try:
        unscheduled_link = wait.until(EC.element_to_be_clickable((By.XPATH, unscheduled_xpath)))
        unscheduled_link.click()
        print("   - Successfully clicked the first link in the unscheduled window.")
    except TimeoutException:
        print("   - Failed to find the first link in the unscheduled window within the given time.")

def click_schedule_button(driver, wait):
    print(":: Clicking the Schedule button")
    schedule_xpath = '/html/body/div/div[2]/div/div/div/div/div[2]/section[2]/div/form/fieldset[3]/div/div[2]/button/span'
    try:
        schedule_button = wait.until(EC.element_to_be_clickable((By.XPATH, schedule_xpath)))
        schedule_button.click()
        print("   - Successfully clicked the Schedule button.")
    except TimeoutException:
        print("   - Failed to find the Schedule button within the given time.")

def confirm_popup(driver, wait):
    print(":: Confirming the popup")
    confirm_xpath = '/html/body/div[2]/div[3]/div/button[1]'
    try:
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, confirm_xpath)))
        confirm_button.click()
        print("   - Successfully confirmed the popup.")
    except TimeoutException:
        print("   - Failed to find the confirm button within the given time.")

def click_mass_signup_button(driver, wait):
    print(":: Clicking the Mass Signup button")
    mass_signup_xpath = '/html/body/div[1]/div[2]/div/div/div/div/div[2]/section[5]/div/form/fieldset[1]/div/div/button/span'
    try:
        mass_signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, mass_signup_xpath)))
        mass_signup_button.click()
        print("   - Successfully clicked the Mass Signup button.")
    except TimeoutException:
        print("   - Failed to find the Mass Signup button within the given time.")

def click_ok_buttons(driver, wait):
    print(":: Clicking the Ok button on the dialog box")
    ok_xpath = '/html/body/div[2]/div[3]/div/button[1]'
    try:
        ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, ok_xpath)))
        ok_button.click()
        print("   - Successfully clicked the Ok button on the dialog box.")
    except TimeoutException:
        print("   - Failed to find the Ok button on the dialog box within the given time.")
    input("Press Enter to exit...")


def clear_screen():
    """
    Clears the console screen.

    This function checks the operating system and uses the appropriate
    command to clear the screen.

    This function does not take any parameters and does not return anything.
    """
    # Check if the operating system is Windows
    if os.name == 'nt':
        # Use 'cls' command for Windows
        os.system('cls')
    else:
        # Use 'clear' command for Unix/Linux/macOS
        os.system('clear')


def _get(wait, xpath):
    """
    Utility function to retrieve an element by its XPath.
    """
    return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

if __name__ == "__main__":
    main()
