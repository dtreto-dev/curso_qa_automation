import pytest
from playwright.sync_api import Page, expect

def test_busqueda_en_google(page: Page):
    # 1. Vamos a Google
    page.goto("https://www.google.com")
    
    # 2. Localizamos el cuadro de búsqueda usando su atributo 'name' (en Google se llama 'q')
    # y le decimos que escriba solo
    cuadro_busqueda = page.locator("textarea[name='q']")
    cuadro_busqueda.fill("Playwright con Python")
    # 3. Simulamos que el robot presiona la tecla 'Enter' en el teclado
    cuadro_busqueda.press("Enter")
    
    # 4. Le damos un segundo de paciencia para que carguen los resultados
    page.wait_for_timeout(5000)
    
    # 5. Validamos que la nueva página contenga la palabra de nuestra búsqueda en el título
    assert "Playwright" in page.title()
    print("\n¡Búsqueda completada y validada con éxito!")