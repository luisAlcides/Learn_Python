# Sample class

class Sample:
    nObjects = 0  # this is a class variable of the Sample class

    def __init__(self, name):
        self.name = name
        Sample.nObjects = Sample.nObjects + 1

    def howManyObjects(self):
        print('There are', Sample.nObjects, ' Sample objects')

    def __del__(self):
        Sample.nObjects = Sample.nObjects - 1


# Instantiate 4 objects
sample1 = Sample('A')
sample2 = Sample('B')
sample3 = Sample('C')
sample4 = Sample('D')

# Delete 1 object
del sample3

# See how many we have
sample1.howManyObjects()
