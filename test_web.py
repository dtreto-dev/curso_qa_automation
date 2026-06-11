import pytest
from playwright.sync_api import sync_playwright

def test_manejo_de_alertas_estable():
    with sync_playwright() as p:
        # Dejamos slow_mo bajo para que no sume tiempo extra innecesario en la carga
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        # TRUCO DE CONTROL DE TRÁFICO: Le damos un timeout de 90 segundos (90000ms) 
        # para que aguante cualquier bache de internet.
        page.set_default_navigation_timeout(90000)
        page.set_default_timeout(90000)
        
        # 1. Volamos a la página (ahora con paciencia extrema)
        page.goto("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
        
        # 2. CONFIGURACIÓN DEL ROBOT (Escuchador de Alertas)
        page.on("dialog", lambda dialog: dialog.accept())
        
        # 3. Apuntamos al cuadro interno
        cuadro_interno = page.frame_locator("#iframeResult")
        
        # 4. ACCIÓN: Hacemos clic en el botón
        cuadro_interno.locator("text=Try it").click()
        
        print("\n¡Test Exitoso! Rompimos la barrera del lag y aceptamos la alerta.")
        
        browser.close()