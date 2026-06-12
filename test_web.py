import pytest
from playwright.sync_api import sync_playwright

def test_manejo_de_multiples_pestanas():
    with sync_playwright() as p:
        # El slow_mo en 1500 nos permite ver el nacimiento de la nueva pestaña
        browser = p.chromium.launch(headless=False, slow_mo=1500)
        context = browser.new_context()
        page = context.new_page()
        
        # Margen de seguridad para nuestra conexión
        page.set_default_navigation_timeout(90000)
        page.set_default_timeout(90000)
        
        # 1. Volamos a la página base
        page.goto("https://www.w3schools.com/tags/att_a_target.asp")
        
        # 2. CONFIGURACIÓN DEL RADAR: Esperamos que el próximo evento sea una nueva página (pestaña)
        # Usamos el contexto del navegador para capturar el nacimiento de la solapa
        with context.expect_page() as nueva_pestana_info:
            # ACCIÓN: Hacemos clic en el botón "Try it Yourself", que tiene target="_blank" (abre otra pestaña)
            page.locator("text=Try it Yourself »").first.click()
        
        # 3. TOMAMOS EL CONTROL DE LA NUEVA PESTAÑA
        # Guardamos la nueva solapa en una variable independiente
        nueva_pagina = nueva_pestana_info.value
        
        # Le decimos a la nueva página que use el mismo tiempo de espera por las dudas
        nueva_pagina.set_default_timeout(90000)
        
        # 4. VALIDACIÓN DE QA: Operamos dentro de la nueva pestaña
        # Leemos el título de la pestaña que se acaba de abrir
        titulo_nueva_pagina = nueva_pagina.title()
        
        print(f"\n¡Título de la nueva pestaña capturado!: '{titulo_nueva_pagina}'")
        
        # Validamos que realmente estamos en la página del editor de W3Schools
        assert "W3Schools Tryit Editor" in titulo_nueva_pagina
        print("\n¡Test Exitoso! El robot migró de pestaña y tomó el control absoluto.")
        
        browser.close()