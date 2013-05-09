#! /usr/bin/env python
# coding:utf-8

from __future__ import division
import abc


class Aggregate(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def iterator(self):
        pass


class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Persons(Aggregate):

    def __init__(self):
        self._persons = []

    def iterator(self):
        return iter(self._persons)

    def add_person(self, person):
        self._persons.append(person)


if __name__ == "__main__":
    person1 = Person("hoge", 21)
    person2 = Person("fuga", 22)
    person3 = Person("piyo", 23)
    p = Persons()
    p.add_person(person1)
    p.add_person(person2)
    p.add_person(person3)

    for person in p.iterator():
        print person.name, person.age
