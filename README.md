# Pacheco Pony Bot: Technical Documentation

## Overview

The Pacheco Pony Bot is a Python-based automation tool crafted to enhance the gaming experience on PonyIsland.net by automating routine tasks such as logging in, navigating contests, and claiming awards. This document details the required dependencies and provides an overview of the bot's operation.

## Dependencies

### Software and Libraries

- **Python 3.8 or newer**: The primary programming language utilised for the bot.
- **Selenium WebDriver**: An open-source tool for automated testing of web applications, enabling programmatic interaction with web pages to simulate user actions.
  - **Installation**: Execute `pip install selenium` to install.
- **Web Drivers**: Selenium necessitates a web driver to interface with the chosen browser. The bot is configured for Chrome WebDriver.
  - **Chrome WebDriver**: Ensure compatibility with your browser version. Available for download from the [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/) page.
- **Additional Python Packages**:
  - **`webdriver_manager`**: Facilitates the management of binary drivers for various browsers.
    - **Installation**: Execute `pip install webdriver_manager` to install.

### Environment Setup

1. **Python Installation**: Ensure Python 3.8 or newer is installed on your system. Download it from [python.org](https://www.python.org/downloads/).
2. **Selenium and WebDriver Manager**: Install these Python libraries using pip:
   ```bash
   pip install selenium webdriver_manager
   ```

### Installing the WebDriver

#### Windows

1. **Download Chrome WebDriver**: Visit the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/) and download the version that matches your Chrome browser.
2. **Extract the ZIP File**: Once downloaded, extract the ZIP file to retrieve `chromedriver.exe`.
3. **Add WebDriver to Path**:
   - Right-click on 'This PC' or 'My Computer' and select 'Properties'.
   - Navigate to 'Advanced system settings' and click on 'Environment Variables'.
   - Under 'System Variables', find 'Path', and select 'Edit'.
   - Click 'New' and add the path to the folder where `chromedriver.exe` is located.
   - Click 'OK' on all windows to apply the changes.

#### Linux

1. **Download Chrome WebDriver**: Visit the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/) and download the version that matches your Chrome browser.
2. **Extract and Move WebDriver**:
   - Extract the downloaded ZIP file using `unzip`:
     ```bash
     unzip chromedriver_linux64.zip
     ```
   - Move `chromedriver` to `/usr/local/bin` (or any location on your PATH):
     ```bash
     sudo mv chromedriver /usr/local/bin/
     ```
3. **Make WebDriver Executable**:
   - Ensure `chromedriver` is executable:
     ```bash
     sudo chmod +x /usr/local/bin/chromedriver
     ```

## How It Works

1. **Initialisation**: The bot initiates by setting up the Selenium WebDriver, configuring necessary browser options, and launching the browser.
2. **Website Interaction**:
   - **Login**: Navigates to the PonyIsland login page, inputs user credentials, and logs into the account.
   - **Navigation**: Once logged in, it moves to various sections of the site, such as the contests page, following predefined tasks.
   - **Action Execution**: Performs specific actions like clicking buttons for contest entries, claiming awards, or participating in arena battles.
3. **Automation Flow**: The bot adheres to a sequential flow, defined in its script, for task automation. Error handling mechanisms, like retries for failed actions, ensure smooth operations.
4. **Session Termination**: After all tasks are completed, the bot securely closes the browser and ends the session.

## Conclusion

The Pacheco Pony Bot utilises Selenium WebDriver and Python scripting to automate and enhance the PonyIsland gaming experience, minimising manual effort and maximising efficiency. Its modular design allows for straightforward customisation and extension to include additional functionalities as required.
