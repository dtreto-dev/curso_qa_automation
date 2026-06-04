def check_status_code(status):
    if status == 200:
        return "¡Prueba Exitosa! La API respondió OK."
    else:
        return f"¡Error en la prueba! Código detectado: {status}"

# Simulamos que probamos una API y nos devuelve un 200
resultado_de_la_prueba = check_status_code(200)
print(resultado_de_la_prueba)