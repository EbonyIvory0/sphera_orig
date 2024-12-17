from selenium.webdriver.common.by import By

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import selenium.webdriver.support.expected_conditions as EC

import time

import random

from selenium.webdriver.common.keys import Keys

LINK = "https://staging.sphera.work/"

wait = WebDriverWait



class Authorization:

    def __init__(self, browser, url):
        if browser.lower() == 'chrome':
            self.browser = webdriver.Chrome()
        else:
            raise ValueError("Unsupported browser. Supported browsers are 'chrome'.")

        self.url = url
        self.browser.get(self.url)
        

    def enter_phone_number(self, phone_number):
        phone_field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "phone"))
        )
        phone_field.send_keys(phone_number)

    def click_receive_code_button(self):
        receive_code_button = wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.phone-input__receive-button"))
        )
        receive_code_button.click()
        
    def enter_one_time_code(self, one_time_code):
        one_time_code_field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "one-time-code"))
        )
        one_time_code_field.send_keys(one_time_code)

    def click_enter_space_button(self):
        enter_space_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']//div[2]/div[2]//button"))
            ).click() 
    
    def authorization(self, phone_number, one_time_code):
        self.enter_phone_number(phone_number) 
        self.click_receive_code_button()
        self.enter_one_time_code(one_time_code)
        self.click_enter_space_button()  

    ###############################################################################
    def test_01_create_channel_add_member_delete_channel(self, name_channel, info_channel):
        create_channel_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Создать канал"]'))
        )
        create_channel_button.click()
        channel_name_field = self.browser.find_element(By.ID, 'name')
        channel_name_field.send_keys(name_channel)
        channel_info_field = self.browser.find_element(By.ID, 'description')
        channel_info_field.send_keys(info_channel)
        create_channel_submit_button = self.browser.find_element(By.XPATH, "//button[text()='Продолжить']")
        create_channel_submit_button.click()
        modal_window = wait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='dialog']"))
        )
        # button_skip = self.browser.find_element(By.CSS_SELECTOR, "div[role='dialog']")
        # button_skip = wait(self.browser, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//button[text() = 'Пока пропустить']"))).click()
        time.sleep(1)
        header_button = wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'header__button-icon'))
        ).click()
        modal_window = wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']"))
        )
        button_header = self.browser.find_elements(By.CSS_SELECTOR, 'button[role="tab"]')[1].click()
        wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MuiBox-root"))
        )

        add_member = self.browser.find_elements(By.TAG_NAME, "button")[-1].click()

        add_member_by_name = self.browser.find_element(By.ID, "select-input")
        add_member_by_name.send_keys("Вильгельмина-Виктория Новгородняя-Завгородняя-Перегородняя") #NAME MEMBER
        time.sleep(10)
        notifications = wait(self.browser, 10).until(
            EC.presence_of_element_located((By. CLASS_NAME, "dialog__title-text"))
        )
        close = wait(self.browser, 15).until(
            EC.presence_of_element_located((By. CLASS_NAME, "MuiButton-outlinedPrimary"))
        ).click()
        time.sleep(1)
        add_member_by_name_button = self.browser.find_element(By.CLASS_NAME, "user-container__default").click()
        member_add_submit_button = self.browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        try:
            member_check = wait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast'))
            )
        except:
            pass
        else:
            assert member_check.text == "Пользователи успешно добавлены"
        button_header = self.browser.find_elements(By.CSS_SELECTOR, 'button[role="tab"]')[-1].click()
        
        wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MuiBox-root"))
        )    
        delete_button = self.browser.find_element(By.CLASS_NAME, 'settings__button-warning').click()
        wait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()        

    def test_02_create_and_archive_channel(self, name_channel, info_channel):
        create_channel_button = wait(self.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Создать канал"]'))
        )
        create_channel_button.click()
        channel_name_field = self.browser.find_element(By.ID, 'name')
        channel_name_field.send_keys(name_channel)
        channel_info_field = self.browser.find_element(By.ID, 'description')
        channel_info_field.send_keys(info_channel)
        create_channel_submit_button = self.browser.find_element(By.XPATH, "//button[text()='Продолжить']")
        create_channel_submit_button.click()
        modal_window = wait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='dialog']"))
        )
        time.sleep(1)
        header_button = wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'header__button-icon'))
        ).click()
        modal_window = wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']"))
        )
        button_header_settings = self.browser.find_elements(By.CSS_SELECTOR, 'button[role="tab"]')[-1].click()
        wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MuiBox-root"))
        )
        archive_button = self.browser.find_element(By.CSS_SELECTOR, ".MuiButton-textSizeMedium.settings__button").click()
        
        wait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        self.browser.find_element(By. CSS_SELECTOR, "[alt='logo sphere']").click()
        time.sleep(2)
        try:
            toast = wait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast'))
            )        
        except:
            pass
        else:
            assert toast.text == "Изменения сохранены"

    # def test_03_pinned_message(self, name_channel):
    #     choose_channel = wait(self.browser, 10).until(
    #         EC.presence_of_all_elements_located((By.CLASS_NAME, 'channel-data-container'))
    #     )
    #     choose_channel = random.choice(choose_channel)
    #     choose_channel.click()
    #     print_text = wait(self.browser, 5).until(
    #     EC.presence_of_element_located((By. CSS_SELECTOR, "div.ql-editor.ql-blank[contenteditable='true']"))
    #     )       
    #     print_text.send_keys(name_channel)
    #     wait(self.browser, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//button[text()='Отправить']"))
    #     ).click()
    #     wait(self.browser, 10).until(
    #         EC.presence_of_all_elements_located((By.CLASS_NAME, "message-card"))
    #     )[-1].click()
    #     message_menu = wait(self.browser, 10).until(
    #         EC.presence_of_all_elements_located((By.CLASS_NAME, "message-action-buttons-container"))
    #     )[-1]
    #     wait(self.browser, 60).until(EC.visibility_of_element_located(
    #         (By.CSS_SELECTOR, 'button[aria-label="Другие действия"]'))).click()
    #     time.sleep(60)

    def test_04_mention_member(self):
        choose_channel = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'channel-data-container'))
        )
        choose_channel = random.choice(choose_channel)
        choose_channel.click()
        print_text = wait(self.browser, 5).until(
            EC.presence_of_element_located((By. CSS_SELECTOR, "div.ql-editor.ql-blank[contenteditable='true']"))
        )       
        print_text.send_keys("Darova")
        mention_button = self.browser.find_element(By.CSS_SELECTOR, '[aria-label="Упоминание пользователей"]').click()
        mention = wait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By. CLASS_NAME, "ql-mention-list"))
        )
        mention_list = self.browser.find_elements(By. CLASS_NAME, "ql-mention-list-item")
        choose_mention = random.choice(mention_list)
        choose_mention.click()
        time.sleep(1)
        submit = self.browser.find_element(By. XPATH, '//button[text()="Отправить"]').click()    
        time.sleep(2)    

    def test_05_pinned_mesagges(self):
        choose_channel = wait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'channel-data-container'))
        )[10]
        choose_channel.click()
        pinned = wait(self.browser, 5).until(
            EC.presence_of_element_located((By. CSS_SELECTOR, ".header__pinned[type=button]"))
        ).click()

        pinned_message = self.browser.find_elements(By. CLASS_NAME, "header__pinned-list")

        discussions = wait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".header__pinned-block > .header__pinned-list > .pinned-message"))
        )
        choose_message = random.choice(discussions)
        choose_message.click()    
        time.sleep(1)   
        try:
            element_image_close = wait(self.browser, 10).until(
                EC.presence_of_element_located((By. CLASS_NAME, "image-modal__close-icon"))
            )
            element_image_close.click()
        except:
            pass
        time.sleep(1)
        self.browser.execute_script("document.elementFromPoint(10, 10).click();")
    # def test_06_open_discussions(self, name_channel):
    #         choose_channel = wait(self.browser, 10).until(
    #             EC.presence_of_all_elements_located((By.CLASS_NAME, 'channel-data-container'))
    #         )
    #         choose_channel = random.choice(choose_channel)
    #         choose_channel.click()
    #         print_text = wait(self.browser, 5).until(
    #         EC.presence_of_element_located((By. CSS_SELECTOR, "div.ql-editor.ql-blank[contenteditable='true']"))
    #         )       
    #         print_text.send_keys(name_channel)
    #         wait(self.browser, 10).until(
    #             EC.presence_of_element_located((By.XPATH, "//button[text()='Отправить']"))
    #         ).click()
    #         self.browser.find_elements(By.TAG_NAME, 'div')[0]
    #         comment = self.browser.find_elements(
    #         By.CLASS_NAME, 'message-card')
    #         comment1 = comment[-1]
    #         wait(self.browser, 30).until(EC.visibility_of_element_located(
    #             (By.CSS_SELECTOR, 'button[aria-label="Начать обсуждение"]'))).click()


    def test_07_open_discussions_go_to_message(self):
        choose_channel = wait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'channel-data-container'))
        )
        choose_channel = random.choice(choose_channel)
        choose_channel.click()
        button = wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'channel-data-container'))
        ).click()
        try:
            header_name = wait(self.browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'header__name'))
            )
        except:
            pass
        else:
            assert header_name.text == "Обсуждения"
        go_to_message = wait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'link-to-message'))
        )
        go_to_message = random.choice(go_to_message)
        go_to_message.click()
        random_message = wait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'message-card'))
        )
        random_message = random.choice(random_message)
        random_message.click()














        # wait(self.browser, 10).until(
        #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[aria-label="Добавить реакцию"]'))
        # )[-1].click()
        # emoji = wait(self.browser, 10).until(
        #     EC.presence_of_element_located((By.TAG_NAME, 'emoji-picker'))
        # )
        # emoji_list = wait(self.browser, 10).until(
        #     EC.presence_of_all_elements_located((By. PARTIAL_LINK_TEXT, "Grinning Face with Sweat"))
        # )[1].click()
        # time.sleep(10)
