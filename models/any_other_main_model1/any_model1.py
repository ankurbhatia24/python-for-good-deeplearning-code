""" See from: https://github.com/siavash-khodadadeh/MetaLearning-TF2.0/blob/master/models/maml/maml.py
and its base: https://github.com/siavash-khodadadeh/MetaLearning-TF2.0/blob/master/models/base_model.py
"""
"""
Always remember the rules of abstract class
"""
from models.base_model import  BaseModel

class any_model1(BaseModel):    #inherit from BaseModel Class
    def __init__(
        self,
        n,
        k,
        num_steps_validation,
        param1,
        param2
    ):
        self.n = n
        self.k = k
        self.param1 = param1
        self.param2 = param2
        self.num_steps_validation = num_steps_validation
        super(any_model1, self).__init__(param1, param2)

    #then define the required variables


    #the define the required functions