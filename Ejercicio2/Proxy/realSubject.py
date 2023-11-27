from PyQt5.QtWidgets import QApplication
import sys
from Proxy.subject import Subject
from Interface.interfaz_documentos import Interface_Documents


class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def __init__(self, user, password, acces) -> None:
        self.user = user
        self.password = password
        self.acces = acces

    def request(self) -> None:
        app = QApplication(sys.argv)
        interfaz = Interface_Documents()
        app.exec_()

    def getUser(self):
        return self.user