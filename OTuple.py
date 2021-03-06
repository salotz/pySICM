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

    def __eq__(self, other):
        if self.o == other.o and self.tuple == other.tuple:
            return True
        else:
            return False
    
    def __add__(self, other):
        # only add OTuples that are the same orientation and length
        if other.o != self.o:
            raise ValueError("OTuples not the same orientation and cannot be added.")
        elif len(other.tuple) != len(self.tuple):
            raise ValueError("OTuples not of the same length and cannot be added.")
        else:
            tup = tuple([self.tuple[i]+other.tuple[i] for i in range(len(self.tuple))])
        return OTuple(tup, self.o)

    def __sub__(self, other):
        # only subtract OTuples that are the same orientation and length
        if other.o != self.o:
            raise ValueError("OTuples not the same orientation and cannot be subtracted.")
        elif len(other.tuple) != len(self.tuple):
            raise ValueError("OTuples not of the same length and cannot be subtracted.")
        else:
            tup = tuple([self.tuple[i]-other.tuple[i] for i in range(len(self.tuple))])
        return OTuple(tup, self.o)

    def elmul(self, other):
        return OTuple( tuple([el * other for el in self.tuple]), self.o)

    def contract(self, other):
        if self.contracts_with(other):
            sum_exp = []
            for i in range(len(self)):
                new_el = self[i] * other[i]
                if isinstance( new_el, OTuple):
                    new_el = sum(new_el)
                sum_exp.append(new_el)

            return sum(sum_exp)
        else:
            raise(TypeError)

    def pairmul(self, other):
        if isinstance(other, OTuple) and len(self) == len(other) and self.o == other.o:
            new_otuple = []
            for i in range(len(self)):
                new_otuple.append(self[i] * other[i])
            return OTuple(new_otuple, self.o)
        else:
            raise(TypeError)            

        
    # forward multiple; OTuple * something
    def __mul__(self, other):

        # if the other operand is an OTuple either contract or
        # pairwise multiply
        if isinstance(other, OTuple):
            
            # check to make sure they are the same length
            if len(self) != len(other):
                raise(TypeError)
            
            # if they are the same orientation pairwise multiply
            elif self.o == other.o:
                return(self.pairmul(other))
            
            # if they are not the same orientation contract them
            elif self.o != other.o:
                return self.contract(other)
            
        # if the other one is a scalar do elementwise multiplication                        
        elif isinstance(other, int) or isinstance(other, float):
            return(self.elmul(other))
        else:
            raise(TypeError)
        
    # reverse operations
    __rmul__ = __mul__

    
    def contracts_with(self, other):
        if isinstance(other, OTuple) and len(self) == len(other) and self.o != other.o:
            return True
        else:
            return False
