import pytest

import random

import string

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from pages.test import Negative

import time

authorizedBrowser = Negative("chrome", "https://staging.sphera.work/")
@pytest.mark.skip
def test_01():
    authorizedBrowser.Auth_failed("8888888888")
@pytest.mark.skip
def test_02():
    authorizedBrowser.incorrect_phone() # 10 цифр номера телефона

def test_03():
    authorizedBrowser.create_an_existing_channel("9888888888", "8888", "общий")
