import pytest
from playwright.sync_api import sync_playwright

def test_manejo_de_dropdown():
    with sync_playwright() as p:
        # Mantenemos el slow_mo en 1500 (segundo y medio) para llegar a ver el cambio
        browser = p.chromium.launch(headless=False, slow_mo=1500)
        page = browser.new_page()
        
        # 1. Login clásico
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        
        # 2. ACCIÓN NUEVA: Seleccionar opción del menú desplegable
        # La "caja" del menú tiene la clase ".product_sort_container"
        # Usamos .select_option() indicando el "value" de la opción que queremos (lo_to_hi = Low to High)
        page.locator(".product_sort_container").select_option(value="lohi")
        
        # 3. VALIDACIÓN DE QA: Verificamos que el primer producto ahora sea el más barato
        # El primer producto de la lista debería ser la "Sauce Labs Onesie" (que vale $7.99)
        primer_producto = page.locator(".inventory_item_name").first.text_content()
        
        assert primer_producto == "Sauce Labs Onesie"
        print(f"\n¡Test Exitoso! El menú cambió el orden y el primer producto es: {primer_producto}")
        
        browser.close()