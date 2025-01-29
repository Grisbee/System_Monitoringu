from behave import given, when, then
from model.Kamera import Kamera

kamery = []  # Lista przechowująca dodane kamery

@given("istnieje kamera o ID {id:d} w pomieszczeniu \"{pomieszczenie}\"")
def step_impl(context, id, pomieszczenie):
    context.kamera = Kamera(id, pomieszczenie)

@when("pobieram nazwę pomieszczenia z kamery")
def step_impl(context):
    context.result = context.kamera.get_pomieszczenie()

@then("nazwa pomieszczenia powinna wynosić \"{pomieszczenie}\"")
def step_impl(context, pomieszczenie):
    assert context.result == pomieszczenie, f"Oczekiwano {pomieszczenie}, otrzymano {context.result}"

@given("Mam nową instancję kamery")
def step_impl(context):
    context.kamera = None  # Inicjalizacja zmiennej

@when("Dodaję do listy kamerę o ID {id:d} i nazwie \"{pomieszczenie}\"")
def step_impl(context, id, pomieszczenie):
    nowa_kamera = Kamera(id, pomieszczenie)
    kamery.append(nowa_kamera)

@then("Najnowsza kamera na liście powinna mieć ID {id:d} i nazwę \"{pomieszczenie}\"")
def step_impl(context, id, pomieszczenie):
    last_kamera_id = kamery[-1].get_kod()
    assert  last_kamera_id == id, f"Oczekiwano ID {id}, otrzymano {kamery[-1].id}"
    assert kamery[-1].get_pomieszczenie() == pomieszczenie, f"Oczekiwano {pomieszczenie}, otrzymano {kamery[-1].get_pomieszczenie()}"