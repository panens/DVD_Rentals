from abc import ABCMeta, abstractmethod


class AbstractTask(metaclass=ABCMeta): #This is an abstract class requiring every concrete class to have a run method

    @abstractmethod 
    def run(self): #defining a method that needs to be implemented
        raise NotImplementedError("Must be implemented by every task")

class ConcreteTask(AbstractTask): #concrete class
    def __init__(self, function: callable): #gets instanciated by giving it a callable called function
        self.function = function 
    
    def run(self, *args, **kwargs): #provides implementation details for method run 
        return self.function(*args,**kwargs) #returns the result of the function 