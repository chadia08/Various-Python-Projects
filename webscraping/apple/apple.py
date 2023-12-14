from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Initialisation du DataFrame
columns = {'Chiffre affaires': []}

def get_data_after_click():
    url = 'https://www.google.com/finance/quote/AAPL:NASDAQ?hl=fr'
    chromedriver_path = "C:/chromedriver-win64/chromedriver.exe"  # Remplacez ceci par votre chemin
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Exécution en mode headless (en arrière-plan)
    
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    driver.get(url)
    
    # Trouver l'élément à cliquer
    try:
        element_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Annuelles']"))  # XPath pour l'élément 'Annuelles'
        )
        element_to_click.click()  # Cliquer sur l'élément 'Annuelles'
    except:
        print("Impossible de cliquer sur l'élément 'Annuelles'")
        driver.quit()
        return None
    
    try:
        new_data_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[contains(@class, 'QXDnM')]"))  
        )
        new_data = new_data_element.text  # Récupérer les nouvelles données
    except:
        print("Nouvelles données introuvables")
        driver.quit()
        return None
    
    driver.quit()
    return new_data

# Appel de la fonction pour récupérer les données après avoir cliqué sur 'Annuelles'
data_after_click = get_data_after_click()

# Si les données sont récupérées avec succès, les ajouter au DataFrame et enregistrer dans un fichier CSV
if data_after_click:
    columns['Chiffre affaires'].append(data_after_click)
    pd.DataFrame(columns).to_csv('apple.csv', index=False)
