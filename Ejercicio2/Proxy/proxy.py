from Proxy.subject import Subject
from Proxy.realSubject import RealSubject

class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access(self._real_subject.acces):
            #Poner aqui el composite para crear las carpetas y documentos
            self._real_subject.request()
            self.log_access()

    def check_access(self, acceso) -> bool:
        print(acceso)
        return acceso

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")