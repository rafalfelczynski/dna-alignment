

class ISequenceProvider:

    def write(self, seq):
        pass

    def read(self, ident):
        pass

    def readAll(self):
        pass

    def delete(self, ident):
        pass

    def checkIfExists(self, ident):
        pass


