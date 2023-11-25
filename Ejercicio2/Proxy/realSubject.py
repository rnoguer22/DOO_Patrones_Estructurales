from Proxy.subject import Subject

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
        print("RealSubject: Handling request.", self.user, self.password, self.acces)