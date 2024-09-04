# Setting Up Selenium Environment for Python with Chrome and Firefox

This guide covers setting up Selenium with both Chrome and Firefox on Windows, Linux, and macOS.

## Common Steps for All Operating Systems

### 1. Install Python

1. Go to https://www.python.org/downloads/
2. Download the latest version of Python for your operating system
3. Run the installer and follow the installation wizard
   - On Windows, make sure to check "Add Python to PATH"

### 2. Verify pip installation

Pip usually comes pre-installed with Python. To check:

1. Open a command prompt or terminal
2. Run: `pip --version`

If pip is not installed, follow the instructions at: https://pip.pypa.io/en/stable/installation/

### 3. Install Selenium

1. Open a command prompt or terminal
2. Run: `pip install selenium`

## Chrome Setup

### 4. Install ChromeDriver

#### Windows:

1. Check your Chrome version: Help > About Google Chrome
2. Download matching ChromeDriver from: https://sites.google.com/a/chromium.org/chromedriver/downloads
3. Unzip and move chromedriver.exe to C:\WebDriver
4. Add C:\WebDriver to your PATH:
   - Search for "Environment Variables" in Start menu
   - Click "Edit the system environment variables"
   - Click "Environment Variables"
   - Under "System variables", select "Path" and click "Edit"
   - Click "New" and add "C:\WebDriver"
   - Click "OK" on all dialogs

#### Linux:

1. Check Chrome version: Menu > Help > About Google Chrome
2. Download matching ChromeDriver
3. In terminal:
   ```
   unzip chromedriver_linux64.zip
   sudo mv chromedriver /usr/local/bin/chromedriver
   sudo chown root:root /usr/local/bin/chromedriver
   sudo chmod +x /usr/local/bin/chromedriver
   ```

#### macOS:

1. Check Chrome version: Chrome > About Google Chrome
2. Download matching ChromeDriver
3. In terminal:
   ```
   unzip chromedriver_mac64.zip
   sudo mv chromedriver /usr/local/bin/chromedriver
   sudo chown root:root /usr/local/bin/chromedriver
   sudo chmod +x /usr/local/bin/chromedriver
   ```

## Firefox Setup

### 5. Install GeckoDriver

#### Windows:

1. Download latest GeckoDriver from: https://github.com/mozilla/geckodriver/releases
2. Unzip and move geckodriver.exe to C:\WebDriver (create if it doesn't exist)
3. Add C:\WebDriver to your PATH if you haven't already (see Chrome instructions)

#### Linux:

1. Download latest GeckoDriver
2. In terminal:
   ```
   tar -xvzf geckodriver-v*-linux64.tar.gz
   sudo mv geckodriver /usr/local/bin/geckodriver
   sudo chown root:root /usr/local/bin/geckodriver
   sudo chmod +x /usr/local/bin/geckodriver
   ```

#### macOS:

1. Download latest GeckoDriver
2. In terminal:
   ```
   tar -xvzf geckodriver-v*-macos.tar.gz
   sudo mv geckodriver /usr/local/bin/geckodriver
   sudo chown root:root /usr/local/bin/geckodriver
   sudo chmod +x /usr/local/bin/geckodriver
   ```

## Verify Installation

Test your setup with both Chrome and Firefox:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Chrome test
chrome_service = ChromeService(executable_path="/path/to/chromedriver")
chrome_driver = webdriver.Chrome(service=chrome_service)
chrome_driver.get("https://www.google.com")
print("Chrome title:", chrome_driver.title)
chrome_driver.quit()

# Firefox test
firefox_service = FirefoxService(executable_path="/path/to/geckodriver")
firefox_driver = webdriver.Firefox(service=firefox_service)
firefox_driver.get("https://www.google.com")
print("Firefox title:", firefox_driver.title)
firefox_driver.quit()
```

Replace "/path/to/chromedriver" and "/path/to/geckodriver" with the actual paths if they're not in your system PATH.

## Troubleshooting

- "XXXdriver executable needs to be in PATH" error: Ensure the WebDriver is in your system PATH or use the full path in the Service() constructor.
- On Linux/macOS: Use `sudo` if you encounter "permission denied" errors.
- Browser version mismatch: Ensure your WebDriver version matches your browser version.

## Next Steps

You're now ready to start automating both Chrome and Firefox with Selenium! Experiment with different browsers and explore Selenium's capabilities.
