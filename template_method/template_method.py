#! /usr/bin/env python
# coding:utf-8

from __future__ import division
import abc


class TemplateClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def pr(self):
        pass

    def template(self):
        for i in range(10):
            self.pr()


class ConcleteClass(TemplateClass):

    def pr(self):
        print "hello, world"


class ConcleteClass2(TemplateClass):

    def pr(self):
        print "hello, world, world"

if __name__ == "__main__":
    template = ConcleteClass2()
    template.template()
