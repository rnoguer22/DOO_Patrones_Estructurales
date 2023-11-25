from abc import ABC, abstractmethod


class DocumentosSistema(ABC):

    @abstractmethod
    def getNombre(self):
        pass

    @abstractmethod
    def getTipo(self):
        pass

    @abstractmethod
    def getTamaño(self):
        pass

    @abstractmethod
    def acceder(self, usuario):
        pass
