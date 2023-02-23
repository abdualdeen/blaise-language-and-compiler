class Binding:
    pass


class BindingList(Binding):
    def __init__(self):
        self.bindings = []

    def __repr__(self):
        s = ''
        for b in self.bindings:
            if s != '':
                s += ', '
            s += repr(b)
        return s

    def __eq__(self, o):
        if not isinstance(o, BindingList):
            return False
        return self.bindings == o.bindings


class Bool(Binding):
    def __repr__(self):
        return 'bool'

    def __eq__(self, o):
        return isinstance(o, Bool)


class Int(Binding):
    def __repr__(self):
        return 'int'

    def __eq__(self, o):
        return isinstance(o, Int)


class Procedure(Binding):
    def __init__(self, lst):
        if isinstance(lst, BindingList):
            self.lst = lst
        else:
            self.lst = None

    def __repr__(self):
        if self.lst is None:
            return 'proc()'
        return 'proc(' + repr(self.lst) + ')'

    def __eq__(self, o):
        if not isinstance(o, Procedure):
            return False
        if self.lst is None:
            return o.lst is None
        return self.lst == o.lst


class SymbolTable:
    def __init__(self, parent=None, scope=None):
        self.bindings = {}
        self.parent = parent
        self.current_scope = scope

    def lookup(self, name):
        if name in self.bindings:
            return self.bindings.get(name)
        if self.parent:
            return self.parent.lookup(name)
        return None

    def lookup4(self, name):
        if name in self.bindings:
            return self.current_scope, self.bindings.get(name)
        if self.parent:
            return self.parent.lookup4(name)
        return None

    def enter(self,scope_name = None):
        if scope_name:
            return SymbolTable(parent=self, scope = scope_name)
        else:
            return SymbolTable(parent=self)

    def exit(self):
        if self.parent:
            return self.parent
        return None

    def __repr__(self):
        if self.parent:
            return repr(self.parent) + ' -> ' + repr(self.bindings)
        return repr(self.bindings)

    def bind(self, name, binding):
        if name in self.bindings:
            return False
        self.bindings[name] = binding
        return True
