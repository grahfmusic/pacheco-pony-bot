#!/usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

__author__ = 'deanypoo'

def main():
    """
    Entry point for the script. Handles initialization and main operations.
    """
    # Clear the console screen
    clear_screen()

    # Print welcome message
    print_welcome_message()

    # Initialize the web driver and wait object
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # Input credentials
    in_user = "<username>"
    in_pass = "<password>"

    # Log into the website
    login_to_website(driver, wait, in_user, in_pass)

    # Perform main operations
    perform_main_operations(driver, wait)

    # Close the web driver
    driver.quit()

    # Print success message
    print(":: Operation completed successfully!")

def print_welcome_message():
    """
    Prints the welcome message for the Pacheco Pony Bot.
    """
    # Define the welcome message
    message = (
        "\033[35m.''\033[0m         \033[33mPacheco Pony Bot\033[0m\n"
        "\033[35m._.-.___.' (`\\\033[0m   \033[32mVersion 1.0\033[0m\n"
        "\033[35m//(\033[0m          \033[35m( `'\033[0m\n"
        "\033[35m'/ )\)__. )\033[0m    \033[36m..that's what she said..\033[0m\n"
        "\033[35m' <' `\ ._/'\ \033[0m  \033[31m ...code.by...  \u2665 \033[0m  "
        "\033[91m...your.slave...\033[0m"
    )

    # Print the welcome message
    print(message)

def login_to_website(driver, wait, username, password):
    """
    Logs into the PonyIsland.net website using the provided credentials.

    Args:
        driver (webdriver.Chrome): The web driver to use.
        wait (WebDriverWait): The wait object to use.
        username (str): The username to use.
        password (str): The password to use.
    """
    # Print message indicating login process start
    print(":: Loading PonyIsland.net Website and entering credentials.")

    # Load the website
    driver.get("https://ponyisland.net")

    # Call the login page function to enter the credentials
    login_page(wait, username, password)

def login_page(wait, username, password):
    """
    Enters the provided credentials on the login page of PonyIsland.net.

    Args:
        wait (WebDriverWait): The wait object to use.
        username (str): The username to use.
        password (str): The password to use.
    """
    # Find the input fields for username and password
    user_field = _get(wait, '//*[@id="login"]/form/fieldset[1]/div/input')
    pass_field = _get(wait, '//*[@id="login"]/form/fieldset[2]/div/input')

    # Enter the provided credentials
    user_field.send_keys(username)
    pass_field.send_keys(password)

    # Find and click the login button
    _get(wait, '//*[@id="login"]/form/div/button').click()

def perform_main_operations(driver, wait):
    """
    Performs the main operations on the PonyIsland.net website.

    Args:
        driver (webdriver.Chrome): The web driver to use.
        wait (WebDriverWait): The wait object to use.
    """
    # Navigate to contests page
    navigate_to_contests(driver)

    # Click the 'Award' button
    click_button(wait, 'Award', '/html/body/div/header/div/div[2]/nav/ul/li[5]/span/a')

    # Navigate to Arena page and click 'Arena' tab
    navigate_and_click(driver, wait, 'Arena', '/html/body/div/div[2]/div/div/div/div/nav/ul/li[2]/span/a')

    # Click the link for the first unscheduled contest
    click_link(wait, 'First Unscheduled', '/html/body/div/div[2]/div/div/div/div/div[2]/section[3]/div/form/table/tbody/tr[1]/td[1]/a')

    # Click the 'Schedule' button
    click_button(wait, 'Schedule', '/html/body/div/div[2]/div/div/div/div/div[2]/section[2]/div/form/fieldset[3]/div/div[2]/button/span')

    # Confirm the popup
    confirm_popup(wait)

    # Click the 'Mass Signup' button
    click_button(wait, 'Mass Signup', '/html/body/div[1]/div[2]/div/div/div/div/div[2]/section[5]/div/form/fieldset[1]/div/div/button/span')

    # Confirm the dialog
    confirm_dialog(wait)


def navigate_to_contests(driver):
    """
    Navigates to the contests page of the PonyIsland.net website.

    Args:
        driver (webdriver.Chrome): The web driver to use.
    """
    # Print message indicating navigation to contests page
    print(":: Navigating to contests page")

    # Load the contests page of the PonyIsland.net website
    driver.get("https://ponyisland.net/#!/?src=contests&sub=contests")

def click_button(wait, name, xpath):
    """
    Clicks a button located by the given XPath.

    Args:
        wait (WebDriverWait): The wait object to use.
        name (str): The name of the button.
        xpath (str): The XPath of the button.
    """
    # Wait until the button is clickable using the given XPath
    try:
        button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        # Click the button
        button.click()
        # Print success message
        print(f"   - Successfully clicked the {name} button.")
    # If the button is not found within the given time, print an error message
    except TimeoutException:
        print(f"   - Failed to find the {name} button within the given time.")

def navigate_and_click(driver, wait, name, xpath):
    """
    Navigates to an element using the given XPath and clicks it.

    Args:
        driver (webdriver.Chrome): The web driver to use.
        wait (WebDriverWait): The wait object to use.
        name (str): The name of the element.
        xpath (str): The XPath of the element.
    """
    # Find and click the element using the given XPath
    try:
        # Wait until the element is clickable using the given XPath
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        # Click the element
        element.click()
        # Print success message
        print(f"   - Successfully navigated to and clicked on the {name} tab.")
    # If the element is not found within the given time, print an error message
    except TimeoutException:
        print(f"   - Failed to navigate to and click on the {name} tab.")

def click_link(wait, name, xpath):
    """
    Clicks a link located by the given XPath.

    Args:
        wait (WebDriverWait): The wait object to use.
        name (str): The name of the link.
        xpath (str): The XPath of the link.
    """
    # Wait until the link is clickable using the given XPath
    try:
        # Find the link using the given XPath
        link = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        # Click the link
        link.click()
        # Print success message
        print(f"   - Successfully clicked the {name}.")
    # If the link is not found within the given time, print an error message
    except TimeoutException:
        print(f"   - Failed to click the {name}.")

def confirm_popup(wait):
    """
    Clicks the 'Confirm' button on a popup window.

    Args:
        wait (WebDriverWait): The wait object to use.
    """
    # XPath of the 'Confirm' button on a popup window
    confirm_button_xpath = '/html/body/div[2]/div[3]/div/button[1]'

    # Clicks the 'Confirm' button
    click_button(wait, 'Confirm', confirm_button_xpath)

def confirm_dialog(wait):
    """
    Clicks the 'Ok' button on a dialog window and waits for user input.

    Args:
        wait (WebDriverWait): The wait object to use.
    """
    # XPath of the 'Ok' button on a dialog window
    ok_button_xpath = '/html/body/div[2]/div[3]/div/button[1]'

    # Clicks the 'Ok' button
    click_button(wait, 'Ok', ok_button_xpath)

    # Waits for user input before continuing
    input("Press Enter to exit...")

def clear_screen():
    """
    Clears the console screen based on the OS.

    This function uses the `os.system` function to execute the appropriate
    command to clear the screen based on the operating system.

    Parameters:
        None

    Returns:
        None
    """
    # The `cls` command is used to clear the screen on Windows systems
    # while the `clear` command is used on Unix-based systems (like Linux)
    # to clear the screen.
    os.system('cls' if os.name == 'nt' else 'clear')

def _get(wait, xpath):
    """
    Retrieves an element using its XPath.

    Args:
        wait (WebDriverWait): The WebDriverWait object to use.
        xpath (str): The XPath of the element to retrieve.

    Returns:
        WebElement: The retrieved element.
    """
    # Uses the WebDriverWait object to wait until the element with the
    # given XPath is present.
    #
    # Parameters:
    # - By.XPATH: Specifies that we are looking for an element using XPath.
    # - xpath: The XPath of the element to retrieve.
    #
    # Returns:
    # The retrieved element.
    return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

if __name__ == "__main__":
    main()

