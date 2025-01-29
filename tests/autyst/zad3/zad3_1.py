from behave import given, when, then
from model.Kamera import Kamera
from model.Dao import Dao

@given('Mam nową instancję kamery')
def step_impl(context):
    context.dao = Dao()
    context.nowa_kamera = Kamera(6, "salon")

@when('Dodaję do listy kamerę o ID {id:d} i nazwie "{name}"')
def step_impl(context, id, name):
    context.dao.update_kamera(context.nowa_kamera)

@then('Najnowsza kamera na liście powinna mieć ID {id:d} i nazwe "{name}"')
def step_impl(context, id, name):
    dao = Dao()
    last_camera = dao.get_kamery()[-1]
    print(last_camera)
    ostatni_kod = last_camera.get_kod()
    assert ostatni_kod == id, f"Powinno byc {id} ale jest {ostatni_kod}"
    ostatnia_nazwa = last_camera.get_pomieszczenie()
    assert ostatnia_nazwa == name, f"Powinno byc '{name}' ale jest '{ostatnia_nazwa}'"


@given('Mam listę kamer i instancje kamery do usuniecia')
def step_impl(context):
    context.dao = Dao()
    context.kamery = context.dao.get_kamery()
    context.kamera_do_usuniecia = context.kamery[-1]

@when('Usuwam kamerę o ID {id:d}')
def step_impl(context, id):
    context.kamery.remove(context.kamera_do_usuniecia)

@then('Kamera o ID {id:d} nie powinna znajdować się na liście')
def step_impl(context, id):
    for kamera in context.kamery:
        assert kamera.get_kod() != id, f"Kamera o ID {id} nadal znajduje się na liście"