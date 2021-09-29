from mock_data import mock_data
from flask import Flask, render_template, request, abort
import json


class Dog:
    def __init__(self, name):
        self.name = name

    def bark():
        print("I'm barking! Woof Woof")


me = {
    "name": "Cameron",
    "last": "Campbell",
    "email": "test@email.com",
    "age": 30,
    "hobbies": [],
    "address": {
        "street": "main",
        "number": "42"
    }
}


def print_data():
    print(me["name"])
    print(me["name"] + " " + me["last"])
    print(me["age"])

    # create an object of Dog class
    fido = Dog("Fido")
    print(fido.name)
    Dog.bark()

    lola = Dog("Lola")
    print(lola.name)

    # print(type(me))
    # print(type(fido))


print_data()


def get_cheapest():
    cheapest = mock_data[0]
    for cheapest in mock_data:
        if prod["price"] < cheapest["price"]:
            cheapest = prod
    return prod


get_cheapest()


def get_sum():
    total = 0
    for prod in mock_data:
        total += prod["price"]
    print(total)


get_sum()
