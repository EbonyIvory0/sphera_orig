

import pytest

import random

import string

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from pages.test import AuthorizationSmoke


import time

def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

authorizedBrowser = AuthorizationSmoke("chrome", "https://staging.sphera.work/")


def test_auth():
    authorizedBrowser.authorization("9888888888", "8888")
   
# def test_01():
#     name_channel = generate_random_string(10)
#     info_channel = generate_random_string(20)
#     authorizedBrowser.test_01_create_channel_add_member_delete_channel(name_channel, info_channel)
#     authorizedBrowser.test_02_create_and_archive_channel(name_channel, info_channel)    
    

# def test_03():
#     authorizedBrowser.test_04_mention_member()

# def test_04():
#     authorizedBrowser.test_05_pinned_mesagges()


# def test_06():
#     authorizedBrowser.test_07_open_discussions_go_to_message()

def test_07():
    authorizedBrowser.my_profile_settings()


# @pytest.mark.skip
# def test_02():
#     name_channel = generate_random_string(10)
#     authorizedBrowser.test_03_pinned_message(name_channel)

    # @pytest.mark.skip
# def test_05():
#     name_channel = generate_random_string(10)
#     authorizedBrowser.test_06_open_discussions(name_channel)
#####################################################################################################################################

