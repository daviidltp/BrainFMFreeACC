from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time  # Import necesario

# Rutas necesarias (ajusta según tu sistema operativo)
BRAVE_PATH = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
CHROMEDRIVER_PATH = "C:/Users/David/Desktop/chromedriver-win64/chromedriver.exe"

# Configuración para Brave en modo incógnito
options = webdriver.ChromeOptions()
options.binary_location = BRAVE_PATH
options.add_argument("--incognito")

# Inicializa el servicio y el navegador
service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Paso 1: Obtener correo temporal
    driver.get("https://10minutemail.net")
    temp_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fe_text"))
    ).get_attribute("value")
    print(f"Correo temporal obtenido: {temp_email}")

    # Paso 2: Registrar un nuevo usuario en Brain.fm
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.brain.fm")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sign up with email']"))
    ).click()

    # Completar formulario de registro
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name"))).send_keys("Pancho Panchez")
    driver.find_element(By.ID, "email").send_keys(temp_email)
    driver.find_element(By.ID, "password").send_keys("panchitolandia2024")
    
    # Crear cuenta
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='handle-sign-up']"))
    ).click()
    print("Registro completado.")

    # Haz clic en el botón con la imagen de fondo
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-28b0d5f4-6 HggYh' or text()='Focus']"))
    ).click()

    driver.get("https://my.brain.fm/")


    # Haz clic en el botón "Preferences"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='preferencesButton']"))
    ).click()

    # Seleccionar géneros deseados
    genres = [
        "genre_beach", "genre_forest", "genre_nightsounds",
        "genre_rain", "genre_river", "genre_rainforest",
        "genre_thunder", "genre_underwater", "genre_wind"
    ]
    for genre in genres:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[@data-testid='{genre}']"))
        ).click()

    # Seleccionar "Low Effect"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='nel_low']"))
    ).click()

    # Aplicar cambios
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='preferences-apply-changes']"))
    ).click()
    print("Preferencias aplicadas.")

except Exception as e:
    print(f"Error durante la ejecución: {e}")
    traceback.print_exc()

finally:
    input("Ctrl+c para cancelar script...")
    time.sleep(999)
