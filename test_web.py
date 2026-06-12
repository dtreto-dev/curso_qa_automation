import pytest
from playwright.sync_api import sync_playwright, expect

def test_proyecto_integrador_compra_completa():
    with sync_playwright() as p:
        # Configuramos un segundo de delay por acción para poder auditar el flujo visualmente
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        # Red de seguridad contra el lag
        page.set_default_navigation_timeout(90000)
        page.set_default_timeout(90000)
        
        # ---- PASO 1: LOGIN ----
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        
        # ---- PASO 2: FILTRAR POR PRECIO ----
        # Abrimos el dropdown y elegimos precio de menor a mayor (Low to High)
        page.locator(".product_sort_container").select_option(value="lohi")
        
        # ---- PASO 3: AGREGAR AL CARRITO ----
        # Hacemos clic en el botón del primer producto filtrado (la ropita de bebé)
        page.locator("#add-to-cart-sauce-labs-onesie").click()
        
        # ---- PASO 4: IR AL CARRITO ----
        # Cliqueamos el contenedor del carrito arriba a la derecha
        page.locator(".shopping_cart_link").click()
        
        # ---- PASO 5: CHECKOUT ----
        # En la pantalla del carrito, presionamos el botón de ir a la caja (Checkout)
        page.locator("#checkout").click()
        
        # ---- PASO 6: FORMULARIO DE ENVÍO ----
        # Completamos los datos requeridos por el sistema
        page.locator("#first-name").fill("David")
        page.locator("#last-name").fill("Treto")
        page.locator("#postal-code").fill("1425") # CP de Palermo
        page.locator("#continue").click()
        
        # ---- PASO 7: FINALIZAR ----
        # Revisamos el total y presionamos el botón de cierre "Finish"
        page.locator("#finish").click()
        
        # ---- PASO 8: VALIDACIÓN CRÍTICA DE QA ----
        # Buscamos el encabezado de éxito que confirma que la orden fue procesada
        mensaje_exito = page.locator(".complete-header").text_content()
        
        assert mensaje_exito == "Thank you for your order!"
        
        print(f"\n🏆 ¡PROYECTO INTEGRADOR EXITOSO! Compra completada. Mensaje: {mensaje_exito}")
        
        # Cerramos las compuertas
        browser.close()