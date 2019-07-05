class ReversedStr(str):
    def __new__(*args,**kwargs):
        # takes no self as operates on a class - class method 
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self
 
class Double(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        return self 