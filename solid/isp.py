#ISP - Interface Segregation Principle

# The Interface Segregation Principle (ISP) states that no client should be forced to depend on methods it does not use. This means that interfaces should be small and specific to the clients that use them, rather than large and general-purpose.
from abc import ABC, abstractmethod


class Machine:
    def print(self, document: str) -> None:
        raise NotImplementedError("This method should be overridden by subclasses")

    def scan(self, document: str) -> None:
        raise NotImplementedError("This method should be overridden by subclasses")

    def fax(self, document: str) -> None:
        raise NotImplementedError("This method should be overridden by subclasses")

class MultiFunctionPrinter(Machine):
    def print(self, document: str) -> None:
        pass

    def scan(self, document: str) -> None:
        pass

    def fax(self, document: str) -> None:
        pass

class OldFashionedPrinter(Machine):
    def print(self, document: str) -> None:
        pass

    def scan(self, document: str) -> None:
        raise NotImplementedError("OldFashionedPrinter does not support scanning")

    def fax(self, document: str) -> None:
        """Not supported!"""
        raise NotImplementedError("OldFashionedPrinter does not support faxing")

class Printer:
    @abstractmethod
    def print(self, document: str) -> None:
        pass

class Scanner:
    @abstractmethod
    def scan(self, document: str) -> None:
        pass

class Fax:
    @abstractmethod
    def fax(self, document: str) -> None:
        pass

class MyPrinter(Printer):
    def print(self, document: str) -> None:
        pass

class Photocopier(Scanner, Fax):
    def scan(self, document: str) -> None:
        pass

    def fax(self, document: str) -> None:
        pass

class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def print(self, document: str) -> None:
        pass

    @abstractmethod
    def scan(self, document: str) -> None:
        pass

    @abstractmethod
    def fax(self, document: str) -> None:
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner, fax: Fax):
        self._printer = printer
        self._scanner = scanner
        self._fax = fax

    @abstractmethod
    def print(self, document: str) -> None:
        self._printer.print(document)

    @abstractmethod
    def scan(self, document: str) -> None:
        self._scanner.scan(document)

    @abstractmethod
    def fax(self, document: str) -> None:
        self._fax.fax(document)