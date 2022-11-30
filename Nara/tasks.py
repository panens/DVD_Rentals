from typing import TypeVar
from abc import ABCMeta, abstractmethod

Task = TypeVar('Task')


class AbstractTask(metaclass=ABCMeta):

    @abstractmethod 
    def run(self): #defining a method that needs to be implemented
        raise NotImplementedError("Must be implemented by every task")

class ConcreteTask(AbstractTask): #concrete class
    def __init__(self, function: Task):
        self.function = function
    
    def run(self, *args, **kwargs): #provides implementation details. 
        return self.function(*args,**kwargs) 