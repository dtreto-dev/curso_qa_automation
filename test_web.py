import pytest
from playwright.sync_api import sync_playwright, expect

def test_remover_producto_del_carrito():
    # Iniciamos Playwright de forma manual para controlar la velocidad
    with sync_playwright() as p:
        # Lanzamos el navegador en modo visible (--headed) y con cámara lenta de 1.5 segundos
        browser = p.chromium.launch(headless=False, slow_mo=1500)
        page = browser.new_page()
        
        # 1. Login
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        
        # 2. Agregamos el producto al carrito
        page.locator("#add-to-cart-sauce-labs-backpack").click()
        
        # 3. Hacemos clic en el botón de Remover
        page.locator("#remove-sauce-labs-backpack").click()
        
        # 4. VALIDACIÓN DE QA AVANZADA: 
        # Aseguramos que el contador NO esté visible.
        contador_carrito = page.locator(".shopping_cart_badge")
        expect(contador_carrito).to_be_hidden()
        
        print("\n¡Test Exitoso! El producto se eliminó en cámara lenta.")
        
        # Cerramos el navegador ordenadamente
        browser.close()