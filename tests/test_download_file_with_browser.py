import os
import time
from selene import browser
from selenium import webdriver
from tests.conftest import path_to_TMP


def test_download_file_zip(tmp_dir_manager):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": path_to_TMP,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)
    assert os.path.exists(os.path.join(path_to_TMP, 'pytest-main.zip'))
