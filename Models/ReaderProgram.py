from Models.FileFastaReader import FileFastaReader

from readerProcess import pr


if __name__ == "__main__":

    fileReader = FileFastaReader()
    fileReader.data_ready.connect(pr)
    fileReader.getData("Models/abc.fasta")
