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


