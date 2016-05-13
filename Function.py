
class Function(object):

    def __init__(self, function, arg_otuple):
        """ arg_otuple must be a prototype of the function using sympy symbols. """
        self.function = function
        self.F = self.function
        self.arg_tuple = arg_tuple

    def eval(self, arg_tuple=None):
        if arg_tuple is None:
            return self.F(self.arg_tuple)
        else:
            return self.F(arg_tuple)

    def set_args(self, new_args):
        self.arg_tuple = new_args

    def compose(self, other_func):
        result = self.F(self.arg_tuple)
        if len(result) == len(other_func.arg_tuple) and result.o == other_func.arg_tuple.o:
            return other_func.F(result)
        else:
            raise(TypeError)
        
