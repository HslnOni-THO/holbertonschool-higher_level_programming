#!/usr/bin/env python3
"""Abstract base class Animal and its subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class implementing sound()"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class implementing sound()"""

    def sound(self):
        return "Meow"
