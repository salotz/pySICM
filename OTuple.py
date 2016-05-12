class OTuple(object):
    __name__ = "OTuple"
    def __init__(self, tup, orientation):
        self.tuple = tup
        self.orientation = orientation
        self.o = self.orientation

    def __str__(self):
        return str(self.o) + "-" + str(self.tuple)
    def __repr__(self):
        return str(self.o) + "-" + str(self.tuple)

    def __getslice__(self, start, end):
        return self.tuple[start:end]

    def __getitem__(self, index):
        return self.tuple[index]

    def __len__(self):
        return len(self.tuple)

    def __iter__(self):
        for el in self.tuple:
            yield el

    def __contains__(self, item):
        if item in self.tuple:
            return True
        else:
            return False

    def __eq__(self, otup):
        if self.o == otup.o and self.tuple == otup.tuple:
            return True
        else:
            return False
    
    def __add__(self, otup):
        # only add OTuples that are the same orientation and length
        if otup.o != self.o:
            raise ValueError("OTuples not the same orientation and cannot be added.")
        elif len(otup.tuple) != len(self.tuple):
            raise ValueError("OTuples not of the same length and cannot be added.")
        else:
            tup = tuple([self.tuple[i]+otup.tuple[i] for i in range(len(self.tuple))])
        return otuple(tup, self.o)

    def __sub__(self, otup):
        # only subtract OTuples that are the same orientation and length
        if otup.o != self.o:
            raise ValueError("OTuples not the same orientation and cannot be subtracted.")
        elif len(otup.tuple) != len(self.tuple):
            raise ValueError("OTuples not of the same length and cannot be subtracted.")
        else:
            tup = tuple([self.tuple[i]-otup.tuple[i] for i in range(len(self.tuple))])
        return otuple(tup, self.o)

    def elmul(self, other):
        return [el * other for el in self.tuple]

    def contract(self, otup):
        if self.contracts_with(otup):
            sum_exp = []
            for i in range(len(self)):
                new_el = self[i] * otup[i]
                sum_exp.append(new_el)

            return sum(sum_exp)
        else:
            raise(TypeError)

    # forward multiple; OTuple * something
    def __mul__(self, otup):

        # if the other operand is an OTuple either contract or
        # pairwise multiply
        if isinstance(otup, OTuple):
            
            # check to make sure they are the same length
            if len(self) != len(otup):
                raise(TypeError)
            
            # if they are the same orientation pairwise multiply
            elif self.o == otup.o:
                raise(NotImplementedError)
            
            # if they are not the same orientation contract them
            elif self.o != otup.o:
                return self.contract(otup)
            
        # if the other one is a scalar do elementwise multiplication                        
        elif isinstance(otup, int) or isinstance(otup, float):
            return(self.elmul(otup))            

        else:
            raise(TypeError)
        
    # reverse operations
    __rmul__ = __mul__

    
    def contracts_with(self, otup):
        if isinstance(otup, OTuple) and len(self) == len(otup) and self.o != otup.o:
            return True
        else:
            return False
