from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_extension('Adblock-Plus_v1.4.1.crx')
driver = webdriver.Chrome(options=options)





driver.get("https://www.delugerpg.com/login/validate")



time.sleep(6)
username_box = driver.find_element(By.XPATH, '//*[@id="loginformform"]/input[1]')
time.sleep(6)
username_box.send_keys('ENTER_USERNAME')



password_box = driver.find_element(By.XPATH, '//*[@id="loginformform"]/input[2]')
time.sleep(6)
password_box.send_keys('ENTER_PASSWORD')



login_button = driver.find_element(By.XPATH, '//*[@id="btn-login"]')


time.sleep(6)

login_button.click()







delugeDict = {
        "Normal" : "NL",
        "Shiny" : "SY",
        "Metallic" : "MC",
        "Ghostly" : "GY",
        "Dark" : "DK",
        "Shadow" : "SW",
        "Mirage" : "ME",
        "Chrome" : "CE",
        "Negative" : "NE",
        "Retro" : "RO",
        "All" : "AL"
    }

print("|-----------         |----------------      |                  |          |      -----------           |-----------")
print("|            |       |                      |                  |          |      |                     |")
print("|            |       |                      |                  |          |      |                     |")
print("|            |       |----------------      |                  |          |      |   ---------|        |-----------")
print("|            |       |                      |                  |          |      |            |        |")
print("|            |       |                      |                  |          |      |            |        |")
print("|-----------         |-----------------     |____________      |__________|      |____________|        |------------")

pokemon_type = input("Enter FIRST and LAST character in of type (i.e. \"NL\" for type Normal or \"AL\" for ALL types): ")
amount_of_times = int(input("How many times foo: "))
is_valid_input = False


for i, value in delugeDict.items():
        #  print(delugeDict[i].lower())
        if delugeDict[i].lower() == pokemon_type.lower():
            print("hi")
            is_valid_input = True
            break

if is_valid_input is False:
    print("Invalid input")

#going to map (replace parameter with whatever map link you desire cause its 3:30 am and im too lazy to do that)#
time.sleep(4)
#change the map to whatever you want
driver.get("https://www.delugerpg.com/map/overworld20")
#WINDOW GUNNA GET BIG, DW.#
driver.maximize_window()
time.sleep(4)

def check_exists_by_xpath():
    try:
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'btn-catch-action')
    except NoSuchElementException:
            print("false")
            return False
    print("true")
    return True
if "nl" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="nl":
                time.sleep(3)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Shiny" not in pokemon_type_text and "Metallic" not in pokemon_type_text and "Ghostly" not in pokemon_type_text and "Dark" not in pokemon_type_text and "Shadow" not in pokemon_type_text and "Mirage" not in pokemon_type_text and "Chrome" not in pokemon_type_text and "Negative" not in pokemon_type_text and "Retro" not in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Shiny" not in pokemon_type_text and "Metallic" not in pokemon_type_text and "Ghostly" not in pokemon_type_text and "Dark" not in pokemon_type_text and "Shadow" not in pokemon_type_text and "Mirage" not in pokemon_type_text and "Chrome" not in pokemon_type_text and "Negative" not in pokemon_type_text and "Retro" not in pokemon_type_text:
                        time.sleep(3)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(3)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)

if "sy" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="sy":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Shiny" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Shiny" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)

                        if "sy" in pokemon_type.lower():
                            for i in range(amount_of_times):
                                if is_valid_input is True:
                                    if pokemon_type.lower() == "sy":
                                        time.sleep(2)
                                        up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                                        up_arrow.click()
                                        if check_exists_by_xpath() == True:
                                            time.sleep(1)
                                            pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                                            print("pokemon type text is " + pokemon_type_text)
                                            if "Shiny" in pokemon_type_text:
                                                time.sleep(2)
                                                try_to_catch_button = driver.find_element(By.CLASS_NAME,
                                                                                          'btn-catch-action')
                                                time.sleep(2)
                                                try_to_catch_button.click()
                                                time.sleep(2)
                                                start_battle_button = driver.find_element(By.CLASS_NAME,
                                                                                          'btn-battle-action')

                                                driver.execute_script("arguments[0].click();", start_battle_button)
                                                # start_battle_button.click()

                                                time.sleep(2)
                                                masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                                                driver.execute_script("arguments[0].click();", masterball)
                                                time.sleep(2)
                                                throw_ball = driver.find_element(By.XPATH,
                                                                                 '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                                                time.sleep(2)
                                                driver.execute_script("arguments[0].click();", throw_ball)

                                                time.sleep(2)
                                                return_to_map = driver.find_element(By.XPATH,
                                                                                    '//*[@id="battle"]/div[1]/a[3]')
                                                time.sleep(2)
                                                driver.execute_script("arguments[0].click();", return_to_map)
                                        time.sleep(2)
                                        down_array = driver.find_element(By.XPATH, '//*[@id="dr-s"]')
                                        down_array.click()
                                        if check_exists_by_xpath() == True:
                                            time.sleep(1)
                                            pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                                            print("pokemon type text is " + pokemon_type_text)
                                            if "Shiny" in pokemon_type_text:
                                                time.sleep(2)
                                                try_to_catch_button = driver.find_element(By.CLASS_NAME,
                                                                                          'btn-catch-action')
                                                time.sleep(2)
                                                try_to_catch_button.click()
                                                time.sleep(2)
                                                start_battle_button = driver.find_element(By.CLASS_NAME,
                                                                                          'btn-battle-action')

                                                driver.execute_script("arguments[0].click();", start_battle_button)
                                                # start_battle_button.click()

                                                time.sleep(2)
                                                masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                                                driver.execute_script("arguments[0].click();", masterball)
                                                time.sleep(2)
                                                throw_ball = driver.find_element(By.XPATH,
                                                                                 '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                                                time.sleep(2)
                                                driver.execute_script("arguments[0].click();", throw_ball)

                                                time.sleep(2)
                                                return_to_map = driver.find_element(By.XPATH,
                                                                                    '//*[@id="battle"]/div[1]/a[3]')
                                                time.sleep(2)
                                                driver.execute_script("arguments[0].click();", return_to_map)

if "mc" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="mc":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Metallic" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Metallic" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)

if "gy" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="gy":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Ghostly" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Ghostly" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)

if "dk" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="dk":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Dark" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Dark" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)

if "sw" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="sw":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Shadow" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Shadow" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(3)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)


if "me" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="me":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Mirage" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Mirage" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)


if "ce" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="ce":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Chrome" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Chrome" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)


if "ro" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="ro":
                time.sleep(1.5)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Retro" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(1.5)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Retro" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)


if "ne" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="ne":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)
                    if "Negative" in pokemon_type_text:

                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        #start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)
                    if "Negative" in pokemon_type_text:
                        time.sleep(2)
                        try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                        time.sleep(2)
                        try_to_catch_button.click()
                        time.sleep(2)
                        start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                        driver.execute_script("arguments[0].click();", start_battle_button)
                        # start_battle_button.click()

                        time.sleep(2)
                        masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                        driver.execute_script("arguments[0].click();", masterball)
                        time.sleep(2)
                        throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", throw_ball)

                        time.sleep(2)
                        return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                        time.sleep(2)
                        driver.execute_script("arguments[0].click();", return_to_map)



if "al" in pokemon_type.lower():
    for i in range(amount_of_times):
        if is_valid_input is True:
            if pokemon_type.lower()=="al":
                time.sleep(2)
                up_arrow = driver.find_element(By.XPATH, '//*[@id="dr-n"]')

                up_arrow.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text

                    print("pokemon type text is "+pokemon_type_text)


                    time.sleep(2)
                    try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                    time.sleep(2)
                    try_to_catch_button.click()
                    time.sleep(2)
                    start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                    driver.execute_script("arguments[0].click();", start_battle_button)
                    #start_battle_button.click()

                    time.sleep(2)
                    masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                    driver.execute_script("arguments[0].click();", masterball)
                    time.sleep(2)
                    throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", throw_ball)

                    time.sleep(2)
                    return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", return_to_map)
                time.sleep(2)
                down_array = driver.find_element(By.XPATH,'//*[@id="dr-s"]')
                down_array.click()
                if check_exists_by_xpath() == True:
                    time.sleep(1)
                    pokemon_type_text = driver.find_element(By.ID, 'dexy').text
                    print("pokemon type text is " + pokemon_type_text)

                    time.sleep(2)
                    try_to_catch_button = driver.find_element(By.CLASS_NAME, 'btn-catch-action')
                    time.sleep(2)
                    try_to_catch_button.click()
                    time.sleep(2)
                    start_battle_button = driver.find_element(By.CLASS_NAME, 'btn-battle-action')

                    driver.execute_script("arguments[0].click();", start_battle_button)
                    # start_battle_button.click()

                    time.sleep(2)
                    masterball = driver.find_element(By.XPATH, '//*[@id="item-masterball"]')
                    driver.execute_script("arguments[0].click();", masterball)
                    time.sleep(2)
                    throw_ball = driver.find_element(By.XPATH, '//*[@id="itemwrap"]/div[1]/form/div[2]/input[2]')
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", throw_ball)

                    time.sleep(2)
                    return_to_map = driver.find_element(By.XPATH, '//*[@id="battle"]/div[1]/a[3]')
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", return_to_map)



















