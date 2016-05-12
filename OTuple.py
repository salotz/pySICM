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
        pass

    def __contains__(self, item):
        pass

    def __eq__(self, otup):
        if self.o == otup.o and self.tuple == otup.tuple:
            return True
        else:
            return False
    
    def __add__(self, otup):
        # only add OTuples that are the same orientation
        if otup.o != self.o:
            raise ValueError("OTuples not the same orientation and cannot be added.")
        elif len(otup.tuple) != len(self.tuple):
            raise ValueError("OTuples not of the same length and cannot be added.")
        else:
            tup = tuple([self.tuple[i]+otup.tuple[i] for i in range(len(self.tuple))])
        return otuple(tup, self.o)

    def __sub__(self, otup):
        # only add OTuples that are the same orientation
        if otup.o != self.o:
            raise ValueError("OTuples not the same orientation and cannot be subtracted.")
        elif len(otup.tuple) != len(self.tuple):
            raise ValueError("OTuples not of the same length and cannot be subtracted.")
        else:
            tup = tuple([self.tuple[i]-otup.tuple[i] for i in range(len(self.tuple))])
        return otuple(tup, self.o)

    def elmul(self, other):
        try:
            return [el * other for el in self.tuple]
        except(TypeError):
            return [other * el for el in self.tuple]

    def contract(self, otup):

        sum_exp = []
        for i in range(len(self.tuple)):
            try:
                sum_exp.append( sum(self[i] * otup[i]) )
            except(TypeError):
                pass
            try:
                sum_exp.append( sum(otup[i] * self[i]) )
            except(TypeError):
                sum_exp.append(otup[i] * self[i])

        print("returning contraction", sum_exp)
        return sum(sum_exp)


    # forward multiple; OTuple * something
    def __mul__(self, otup):

        # if they are both OTuples
        if isinstance(otup, otuple) and isinstance(self, otuple):
            print("contracting", self, "by", otup)
            # check to make sure they are the same length
            if len(self) != len(otup):
                raise(TypeError, "OTuples must be of the same length to be multiplied")
            # check to see if they are the same orientation
            elif self.o == otup.o:
                raise(NotImplementedError)
            # if they are not the same orientation contract them
            elif self.o != otup.o:
                return self.contract(otup)
            
        # if one is an OTuple and the other a scalar, elementwise multiply
        elif isinstance(otup, otuple):
            print("elementwise on ", otup)
            return(otup.elmul(self))
        elif isinstance(self, otuple):
            print("elementwise on ", self)
            return(self.elmul(otup))
        
    # reverse operations
    __rmul__ = __mul__
