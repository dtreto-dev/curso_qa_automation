# Esta es la función del sistema que vamos a testear
def validar_usuario(usuario):
    if usuario == "david_qa":
        return "Acceso Concedido"
    else:
        return "Usuario Incorrecto"


# --- AQUÍ EMPIEZAN LOS TESTS DE QA ---
# Recordá que en Pytest las funciones siempre empiezan con "test_"

def test_login_exitoso():
    resultado = validar_usuario("david_qa")
    # Aseguramos que con el usuario correcto de acceso
    assert resultado == "Acceso Concedido"

def test_login_fallido():
    resultado = validar_usuario("intruso123")
    # Aseguramos que con un impostor rebote
    assert resultado == "Usuario Incorrecto"