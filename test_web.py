import pytest
from playwright.sync_api import Page

def test_agregar_producto_al_carrito(page: Page):
    # 1. Login clásico (lo que ya dominás)
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # 2. ACCIÓN NUEVA: Buscamos el botón del primer producto y hacemos CLIC
    # Usamos el ID del botón específico de la mochila "Sauce Labs Backpack"
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    
    # 3. Freno de mano de 2 segundos para ver el cambio con tus propios ojos
    page.wait_for_timeout(2000)
    
    # 4. VALIDACIÓN DE QA: Buscamos el texto que está adentro del círculo del carrito
    # La clase web del contador se llama ".shopping_cart_badge"
    texto_carrito = page.locator(".shopping_cart_badge").text_content()
    
    # Aseguramos que el robot lea un "1" adentro del carrito
    assert texto_carrito == "1"
    print(f"\n¡Test Exitoso! El carrito tiene {texto_carrito} producto adentro.")