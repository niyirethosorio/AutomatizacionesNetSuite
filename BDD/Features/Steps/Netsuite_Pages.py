from behave import *


@given('Se loguea a NetSuite con usuario "{User}" y contraseña "{Pass}" y empresa "{Enterprise}"')
def step_impl(context, User, Pass, Enterprise):
    print("hola mundo cruel")


@when('')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
