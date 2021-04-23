from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from deep_translator import GoogleTranslator
import pickle
import os
import json
import colorama
from colorama import Fore
from colorama import Style
import string
import chromedriver_autoinstaller
import re


# nombre de lecon fini
countLesson = 0


def passe(temps):
    time.sleep(temps)
    driver.find_element_by_xpath(
        "//*[text()='Continuer']").click()


def newTeacher():
    global countLesson

    driver.get("https://www.duolingo.com/stories")
    time.sleep(2)
    story = driver.find_elements_by_xpath(
        "//a[@href='/stories/en-fr-new-teacher']")
    if len(story) == 1:
        story[0].click()
    else:
        try:
            driver.find_element_by_xpath("//span[text()='Anglais']").click()
            newTeacher()
        except:
            raise Exception(
                Fore.RED + "The chosen language must be english" + Style.RESET_ALL)
    try:
        passe(2)  # new teacher
    except:
        driver.find_element_by_xpath(
            "//button[text()='COMMENCER L'HISTOIRE']").click()
        passe(2)  # new teacher
    passe(4)  # mark is outside
    passe(5)  # ok i'm going

    driver.find_element_by_xpath(
        "//span[text()='Oui']").click()
    passe(1)  # reponse oui

    passe(2.5)  # I'm a bad teacher
    passe(2.5)  # My students hate me
    passe(3)  # teaching is too hard

    time.sleep(2)
    choice = driver.find_elements_by_xpath(
        "//*[contains(@class, '_1Q3F0')]/li/button")
    for i in choice:
        try:
            i.click()
        except:
            break
    passe(1)  # reponse door

    passe(3)  # Mark Come inside
    passe(2)  # How can I help you

    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='I']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='want']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='to talk about']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='something']").click()
    passe(1)  # reponse I want to

    passe(2)  # I'm a new teacher
    passe(2.5)  # And you're great teacher
    passe(2)  # your students love you
    passe(1)  # really

    time.sleep(3)
    driver.find_element_by_xpath(
        "//button[text()='a hard job']").click()
    passe(1)  # reponse a hard job

    passe(3)  # a lot of
    passe(4)  # but you stay
    passe(2)  # they feel important
    passe(2)  # your students need you
    passe(1.5)  # you're right

    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='I']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='need']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='to remember']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='that']").click()
    passe(1)  # reponse I need to remember that

    passe(3)  # I woory that
    passe(2.5)  # I know you're worried Mark
    passe(2)  # How do you know
    passe(5)  # Well your were talking very

    driver.find_element_by_xpath(
        "//span[text()='fort']").click()
    passe(1)  # reponse fort

    time.sleep(1)
    try:
        driver.find_element_by_xpath(
            "//button[text()='vraiment']").click()
        driver.find_element_by_xpath(
            "//button[text()='really']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='mauvais']").click()
        driver.find_element_by_xpath(
            "//button[text()='bad']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='students']").click()
        driver.find_element_by_xpath(
            "//button[text()='élèves']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='dur']").click()
        driver.find_element_by_xpath(
            "//button[text()='hard']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='dire']").click()
        driver.find_element_by_xpath(
            "//button[text()='to tell']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='détestent']").click()
        driver.find_element_by_xpath(
            "//button[text()='hate']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='teacher']").click()
        driver.find_element_by_xpath(
            "//button[text()='professeur']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='bureau']").click()
        driver.find_element_by_xpath(
            "//button[text()='office']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='parliez']").click()
        driver.find_element_by_xpath(
            "//button[text()='were talking']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='loudly']").click()
        driver.find_element_by_xpath(
            "//button[text()='fort']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='travail']").click()
        driver.find_element_by_xpath(
            "//button[text()='job']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='teacher']").click()
        driver.find_element_by_xpath(
            "//button[text()='professeur']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='you're right']").click()
        driver.find_element_by_xpath(
            "//button[text()='vous avez raison']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='vous avez raison']").click()
        driver.find_element_by_xpath(
            "//button[text()='you're right']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='boss']").click()
        driver.find_element_by_xpath(
            "//button[text()='patronne']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='frappe à']").click()
        driver.find_element_by_xpath(
            "//button[text()='knocks on']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='quitter']").click()
        driver.find_element_by_xpath(
            "//button[text()='to leave']").click()
    except:
        None
    passe(1)  # paires
    passe(8)  # fin
    countLesson += 1
    time.sleep(3)


def party():
    global countLesson

    driver.get("https://www.duolingo.com/stories")
    time.sleep(4)
    story = driver.find_elements_by_xpath(
        "//a[@href='/stories/en-fr-the-party-1']")
    if len(story) == 1:
        story[0].click()
    else:
        try:
            driver.find_element_by_xpath("//span[text()='Anglais']").click()
        except:
            raise Exception(
                Fore.RED + "The chosen language must be english" + Style.RESET_ALL)
    try:
        passe(2)  # the party
    except:
        driver.find_element_by_xpath(
            '//button[text()="COMMENCER L\'HISTOIRE"]').click()
        passe(2)  # the party
    passe(4)  # madeline and steven

    time.sleep(2.5)
    driver.find_element_by_xpath(
        "//button[text()=\"What's the address\"]").click()
    passe(1)  # reponse what's the adress

    passe(2)  # fifteen george street
    passe(2.5)  # OK we're here

    time.sleep(3)
    try:
        driver.find_element_by_xpath(
            "//*[contains(@class, '_2l5CB')]//span[text()='But']").click()
        driver.find_element_by_xpath(
            "//*[contains(@class, '_2l5CB')]//span[text()=\"it's\"]").click()
        driver.find_element_by_xpath(
            "//*[contains(@class, '_2l5CB')]//span[text()='an']").click()
        driver.find_element_by_xpath(
            "//*[contains(@class, '_2l5CB')]//span[text()='old']").click()
        driver.find_element_by_xpath(
            "//*[contains(@class, '_2l5CB')]//span[text()='factory']").click()
    except:
        None
    passe(1)  # reponse but it's an old factory

    passe(3)  # well it's the adress Josh gave me
    passe(3)  # Mark Come inside
    passe(1.5)  # they leave the car
    passe(2)  # do you see an entrance
    passe(0.5)  # no

    time.sleep(4)
    time.sleep(2)
    choice = driver.find_elements_by_xpath(
        "//*[contains(@class, '_1Q3F0')]/li/button")
    for i in choice:
        try:
            i.click()
        except:
            break
    passe(1)  # reponse door

    passe(1.5)  # here's the door
    passe(2.8)  # I don't think there is a party here
    passe(2.5)  # I'm going inside
    passe(1.5)  # ok

    time.sleep(2.5)
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='They']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='go inside']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='the']").click()
    driver.find_element_by_xpath(
        "//*[contains(@class, '_2l5CB')]//span[text()='building']").click()
    passe(1)  # reponse they go inside the bulding

    passe(2)  # it's dark in here
    passe(3)  # Ok this is a little scary

    driver.find_element_by_xpath(
        "//span[text()='peur']").click()
    passe(1)  # reponse peur

    passe(2.5)  # suddenly the door closes
    passe(3.1)  # Steven Why did you close the door
    passe(1.5)  # I didn't
    passe(3)  # It's Ok I have a light
    passe(3)  # Wait there's a message from Josh
    passe(3)  # He says he gave me the wrong address
    passe(2)  # We need to leave now
    passe(4.5)  # Madeline this is really bad

    time.sleep(0.25)
    driver.find_element_by_xpath(
        "//span[text()='coincés']").click()
    passe(1)  # reponse fort

    time.sleep(2.5)
    try:
        driver.find_element_by_xpath(
            "//button[text()='OK']").click()
        driver.find_element_by_xpath(
            "//button[text()='d'accord']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='night']").click()
        driver.find_element_by_xpath(
            "//button[text()='soir']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='soudain']").click()
        driver.find_element_by_xpath(
            "//button[text()='suddenly']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='quittent']").click()
        driver.find_element_by_xpath(
            "//button[text()='leave']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='fifteen']").click()
        driver.find_element_by_xpath(
            "//button[text()='quinze']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='address']").click()
        driver.find_element_by_xpath(
            "//button[text()='adresse']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='gave']").click()
        driver.find_element_by_xpath(
            "//button[text()='a donné']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='dangerous']").click()
        driver.find_element_by_xpath(
            "//button[text()='dangereuses']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='building']").click()
        driver.find_element_by_xpath(
            "//button[text()='bâtiment']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='scary']").click()
        driver.find_element_by_xpath(
            "//button[text()='effrayant']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='car']").click()
        driver.find_element_by_xpath(
            "//button[text()='voiture']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='de nouveau']").click()
        driver.find_element_by_xpath(
            "//button[text()='again']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='party']").click()
        driver.find_element_by_xpath(
            "//button[text()='fête']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='door']").click()
        driver.find_element_by_xpath(
            "//button[text()='porte']").click()
    except:
        None
    try:
        driver.find_element_by_xpath(
            "//button[text()='usine']").click()
        driver.find_element_by_xpath(
            "//button[text()='factory']").click()
    except:
        None
    passe(1)  # paires
    passe(8)  # fin
    countLesson += 1
    time.sleep(3)


def enter():
    driver.find_element_by_xpath("//html/body").send_keys(Keys.ENTER)


def lecon():
    global countLesson
    global corrections

    fini = False

    driver.get("https://www.duolingo.com/learn")
    time.sleep(2)

    # si il nous propose de partager a nos amis clique sur non merci
    amis = driver.find_elements_by_xpath("//span[text()='Non merci']")
    if(len(amis) > 0):
        amis[0].click()

    # recuperation de la langue de l'exercice
    title = driver.find_element_by_xpath("//title").get_attribute('innerHTML')
    langueEx = re.match(r"(.*d'apprendre l(a |e |'))(?P<langue>.+$)",
                        title).group('langue')
    langueEx = (GoogleTranslator(
        source='auto', target='en').translate(langueEx)).lower()
    if langueEx not in corrections:
        corrections[langueEx] = {}
        pickle.dump(corrections, open("corrections.pkl", "wb"))

    # choisi aléatoirement une lecon
    lecons = driver.find_elements_by_xpath(
        "//*[@data-test='skill']")
    lecon = random.choice(lecons)
    ActionChains(driver).move_to_element(lecon).perform()
    lecon.click()

    time.sleep(1)
    # clique sur commencer, restaurer ou reviser
    if len(driver.find_elements_by_xpath("//button[text()='COMMENCER']")) == 1:
        driver.find_element_by_xpath("//button[text()='COMMENCER']").click()
    elif len(driver.find_elements_by_xpath("//button[text()='Réviser']")) == 1:
        driver.find_element_by_xpath("//button[text()='Réviser']").click()
    elif len(driver.find_elements_by_xpath("//button[text() = 'Restaurer']")) == 1:
        driver.find_element_by_xpath("//button[text() = 'Restaurer']").click()
    elif len(driver.find_elements_by_xpath("//button[text() = 'BLOQUÉ']")) == 1:
        print('Blocked lesson')
        pass
    else:
        raise Exception(
            Fore.RED + "Fail to start the lesson" + Style.RESET_ALL)
    time.sleep(1)

    while fini == False:
        time.sleep(0.5)

        while True:
            # récupère le titre de l'exercice
            title = driver.find_elements_by_xpath(
                "//*[contains(@data-test, 'challenge-header')]/span")
            progressBar = driver.find_elements_by_xpath(
                "//*[contains(@role, 'progressbar')]")
            # si c'est la fin
            if len(progressBar) == 1:
                if float(progressBar[0].get_attribute('aria-valuenow')) == 1:
                    wait.until(EC.presence_of_element_located((
                        By.XPATH, "//*[contains(@data-test, 'player-end-carousel')]")))
                    enter()
                    countLesson += 1
                    fini = True
                    break
                elif len(title) == 1:
                    title = title[0].get_attribute('innerHTML')
                    break
                # si le titre et pas detecter on tapes sur entrer car il y a un msg d'encouragement
                else:
                    enter()
                    time.sleep(0.5)

        # detecte l'exercice
        # passe si c un exercice de comprehension ou d'expression orale
        if 'Prononce' in title:
            driver.find_element_by_xpath(
                "//*[contains(@data-test, 'player-skip')]").click()
        elif 'entends' in title:
            driver.find_element_by_xpath(
                "//*[contains(@data-test, 'player-skip')]").click()
        # exercice ecris
        elif 'Écris' in title and not '«' in title:
            # active le clavier si besoin
            toggleKeyboard = driver.find_elements_by_xpath(
                "//*[contains(@data-test, 'player-toggle-keyboard')]")
            if len(toggleKeyboard) > 0:
                if toggleKeyboard[0].find_element_by_xpath("div/div[2]").get_attribute('innerHTML') == 'Utiliser le clavier':
                    toggleKeyboard[0].click()

            # repère la phrase à traduire
            elementsPhrase = driver.find_elements_by_xpath(
                "//*[contains(@data-test, 'hint-token')]")
            phrase = ''
            for element in elementsPhrase:
                phrase += element.get_attribute('innerHTML')
            # cherhe l'input
            input = driver.find_element_by_xpath(
                "//*[contains(@data-test, 'challenge-translate-input')]")
            # si la phrase est deja dans le dictionnaire
            if phrase in corrections[langueEx]:
                result = corrections[langueEx][phrase]
            else:
                # cherche la langue
                langue = input.get_attribute("lang")
                # traduction
                result = GoogleTranslator(
                    source='auto', target=langue).translate(phrase)
            if input.is_enabled:
                # renvoie du resultat
                input.send_keys(result)
            else:
                pass
            enter()
        elif 'Écris' in title and '«' in title:
            phrase = title[title.find('«') + 7: title.find('»') - 6]
            # cherhe l'input
            input = driver.find_element_by_xpath(
                "//*[contains(@data-test, 'challenge-text-input')]")  # !!!si erreur challenge translate input
            # si la phrase est deja dans le dictionnaire
            if phrase in corrections[langueEx]:
                result = corrections[langueEx][phrase]
            else:
                # cherche la langue
                chaineLangue = input.get_attribute("placeholder")
                langue = re.match(r'(.*en )(?P<langue>.+$)',
                                  chaineLangue).group('langue')
                langue = (GoogleTranslator(
                    source='auto', target='en').translate(langue)).lower()
                if langue in langs_dict:
                    lang = langs_dict[langue]
                else:
                    lang = 'fr'
                # traduction
                result = GoogleTranslator(
                    source='auto', target=lang).translate(phrase)
            if input.is_enabled:
                # renvoie du resultat
                input.send_keys(result)
            else:
                pass
            enter()
        elif 'Complète' in title:
            driver.find_element_by_xpath(
                "//*[contains(@data-test, 'player-toggle-keyboard')]").click()
            pass
        elif 'Choisis' in title:
            # si le choix est pour completer une phrase
            if len(driver.find_elements_by_xpath("//*[contains(@data-test, 'challenge-form-prompt')]")) > 0:
                phrase = driver.find_element_by_xpath(
                    "//*[contains(@data-test, 'challenge-form-prompt')]").get_attribute("data-prompt")
            # si le choix est donner la traduction
            elif len(driver.find_elements_by_xpath("//*[contains(@class, '_3-JBe')]")) > 0:
                phrase = driver.find_element_by_xpath(
                    "//*[contains(@class, '_3-JBe')]").get_attribute("innerHTML")
            # si la phrase est deja dans le dictionnaire
            if phrase in corrections[langueEx]:
                # on essaie de cliquer sur cette phrase
                try:
                    driver.find_element_by_xpath(
                        f"//*[contains(@data-test, 'challenge-judge-text') and contains(text(),'{corrections[langueEx][phrase]}')").click()
                # sinon on clique sur une réponse aléatoire
                except:
                    random.choice(driver.find_elements_by_xpath(
                        "//*[contains(@data-test, 'challenge-judge-text')]")).click()
            else:
                # on clique sur une réponse aléatoire
                random.choice(driver.find_elements_by_xpath(
                    "//*[contains(@data-test, 'challenge-judge-text')]")).click()
            enter()
        else:
            enter()
            pass

        # verifie si c'est correct
        incorrect = driver.find_elements_by_xpath(
            "//*[contains(@data-test, 'blame blame-incorrect')]")
        correct = driver.find_elements_by_xpath(
            "//*[contains(@data-test, 'blame blame-correct')]")
        # si c'est incorrect
        if len(incorrect) > 0:
            correctionDiv = driver.find_element_by_xpath(
                "//*[contains(@class, '_1UqAr ')]")
            correctionSpan = correctionDiv.find_elements_by_xpath(
                "//span/span")
            # on récupère la phrase
            correction = correctionDiv.get_attribute('innerHTML')
            if 'span' in correction:
                correction = ''
                for element in correctionSpan:
                    correction += element.get_attribute('innerHTML')
            # on enlève tous les espaces et les ponctuations avant
            for i in range(len(correction)):
                if correction[i] in string.ascii_letters:
                    first_letter = i
                    break
            correction = correction[first_letter:len(correction)]
            # on l'ajoute dans le dictionnaire
            corrections[langueEx][phrase] = correction
            pickle.dump(corrections, open("corrections.pkl", "wb"))
            enter()
        elif len(correct) > 0:
            enter()


# récupère les corrections si il y en a
if os.path.isfile("corrections.pkl"):
    corrections = pickle.load(open("corrections.pkl", "rb"))
else:
    corrections = {}

# initialisation du module de couleur
colorama.init()

# demande quel exercice il faut résoudre
choixExo = input(
    Fore.BLUE + 'Press\n• 1 to resolve lessons\n• 2 to resolve the story named "Le nouveau professeur"\n• 3 to resolve the story named "La fête 1/2"\n• 4 to print all the corrections of the mistakes' + Style.RESET_ALL)

# vérifie que la réponse est correct
if choixExo in ['1', '2', '3', '4']:
    choixExo = int(choixExo)
else:
    raise Exception(Fore.RED + 'Please choose 1,2,3 or 4' + Style.RESET_ALL)

if choixExo != 4:
    # demande le nombre de répétition
    repeat = input(
        Fore.BLUE + 'Press enter to resolve lessons endlessly or type the number of lessons you want to do' + Style.RESET_ALL)

    # traitement de la rponse
    if repeat == '':
        repeat = -3
    else:
        try:
            repeat = int(repeat)
        except:
            raise Exception(
                Fore.RED + 'Please type enter or a number' + Style.RESET_ALL)

    # demarre chromedriver
    chromedriver_autoinstaller.install(True)
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=' + os.getcwd() + '\data')
    driver = webdriver.Chrome(options=options)

    langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)

    # va sur duolingo.com
    driver.get("https://www.duolingo.com/")
    wait = WebDriverWait(driver, 600)

    # information
    print(Fore.YELLOW + 'If you want to login with google or facebook go to https://github.com/Bapt5/duolingo-bot#readme' + Style.RESET_ALL)

    # récupère les cookies si besoin
    if os.path.isfile("exported-cookies.json"):
        with open('exported-cookies.json') as json_file:
            cookies = json.loads(json_file.read())
            for cookie in cookies:
                for key in cookie.copy():
                    if key != 'name' and key != 'value':
                        cookie.pop(key)
                driver.add_cookie(cookie)
            driver.get("https://www.duolingo.com/")

    # demande si l'user est connecté
    input(Fore.GREEN + 'Press enter when you are logged in' + Style.RESET_ALL)

# resout des lecons
if choixExo == 1:
    while countLesson != repeat:
        # try:
        lecon()
        # except Exception as e:
        #     if 'Fail to start the lesson' in e.args[0]:
        #         raise e
        #     else:
        #         pass
        # except:
        #     pass
        print(countLesson)
    driver.close()

# resout l'hsitoire le nouveau professeur
elif choixExo == 2:
    while countLesson != repeat:
        try:
            newTeacher()
        except Exception as e:
            if 'The chosen language must be english' in e.args[0]:
                raise e
            else:
                pass
        except:
            pass
        print(countLesson)
    driver.close()

# resout l'histoire la fete 1/2
elif choixExo == 3:
    while countLesson != repeat:
        try:
            party()
        except Exception as e:
            if 'The chosen language must be english' in e.args[0]:
                raise e
            else:
                pass
        except:
            pass
        print(countLesson)
    driver.close()

# affiche les corrections des erreurs
elif choixExo == 4:
    for langue, dico in corrections.items():
        print(langue)
        for question, reponse in dico.items():
            print(question + ' => ' + reponse)
        print()
