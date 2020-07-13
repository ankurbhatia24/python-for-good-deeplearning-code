# Abstract Base Class: Abstract classes are classes that contain one or more abstract methods. \
# An abstract method is a method that is declared, but contains no implementation. \
# Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
# So we will use this as the base class and inherit this in its subclass to define functions.


"""
Always remember the rules of abstract classes
1. the menthods of the abstract class should have the decorator @abstractmethod written before their initialization.
   If not then the class will be instantiable (we can create an instance from it) and no requirement of defining 
   the method in its subclass (since its not an abstract method (decorated by @abstractmethod)).
2. The subclass of the abstract class should have defined the abstract method, else the instance of subclass will not be created.
   i.e. A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.
3. An abstract method can have an implementation in the abstract class also!
   Even if they are implemented, designers of subclasses will be forced to override the implementation.
   In such case, like in other cases of "normal" inheritance, the abstract method can be invoked with super() call mechanism.

For eg:

from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
    
    @abstractmethod
    def do_something(self):
        print("Some implementation!")
        
class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")
        
x = AnotherSubclass()
x.do_something()

"""
from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(self, database, network_cls):
        self.database = database
        self.network_cls = network_cls
        self.train_dataset = None
        self.val_dataset = None
        self.test_dataset = None

    @abstractmethod
    def train(self, epochs):
        pass

    @abstractmethod
    def evaluate(self, iterations):
        pass

    @abstractmethod
    def get_train_dataset(self):
        pass

    @abstractmethod
    def get_val_dataset(self):
        pass

    @abstractmethod
    def get_test_dataset(self):
        pass

    @abstractmethod
    def get_config_info(self):
        pass