from module import Person, Wizard, HealthPotion
from app import main

def test_person_initial_amount():
    person = Person('user1')
    assert person.life_points == 100

def test_wizard_initial_amount():
    wizard = Wizard(Person)
    assert wizard.life_points == 80

def test_person_hit_amount():
    person = Person('user1')
    wizard = Wizard(Person)
    person.hit(wizard)
    assert wizard.life_points == 70

def test_wizard_hit_amount():
    person = Person('user1')
    wizard = Wizard(Person)
    wizard.hit(person)
    assert person.life_points == 85

def test_gained_amount():
    person = Person('user1')
    wizard = Wizard(Person)
    person.gained_life_points(10)
    assert person.life_points == 110

def test_isdead_amount():
    person = Person('user1')
    wizard = Wizard(Person)
    while person.life_points >= 0:
        wizard.hit(person)
    assert person.is_dead() == True


def test_app():
    assert app.main() in ['Hero wins','Wizard wins']

