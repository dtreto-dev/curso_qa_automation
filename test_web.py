import pytest
from playwright.sync_api import Page

def test_login_saucedemo(page: Page):
    # 1. Volamos a una página de login ultra rápida y estable
    page.goto("https://www.saucedemo.com")
    
    # 2. Completamos el usuario (en esta web el ID es "user-name")
    page.locator("#user-name").fill("standard_user")
    
    # 3. Completamos la contraseña (el ID es "password")
    page.locator("#password").fill("secret_sauce")
    
    # 4. Hacemos clic en el botón de ingresar (el ID es "login-button")
    page.locator("#login-button").click()
    
    # 5. Freno de mano de 3 segundos para disfrutar el éxito en pantalla
    page.wait_for_timeout(3000)
    
    # 6. Validamos que entramos chequeando que la URL contenga "inventory"
    assert "inventory" in page.url
    print("\n¡Login en SauceDemo completado con éxito total!")