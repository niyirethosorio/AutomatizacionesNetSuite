from behave import *


@given('ingresar al ambiente de {environment} de netsuite')
def step_impl(context, environment):
    if environment is "pruebas":
        context.browser.get("https://reservas.viajescomfama.com/NetAdmin/Login.aspx")
    elif environment is "google":
        context.browser.get("https://www.google.com/")


@then('Loquearse con usuario {user}, contraseña {password} y empresa {enterprise}')
def step_impl(context, user, password, enterprise):
    pass
