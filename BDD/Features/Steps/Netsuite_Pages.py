from behave import *


@given('Se loguea a NetSuite con usuario {user} y contraseña {password} y empresa {enterprise}')
def step_impl(context, user, password, enterprise):
    context.browser.get("https://reservas.viajescomfama.com/NetAdmin/Login.aspx")
