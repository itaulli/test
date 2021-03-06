# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_dla')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_dla')
    _dla = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_dla', [dirname(__file__)])
        except ImportError:
            import _dla
            return _dla
        try:
            _mod = imp.load_module('_dla', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _dla = swig_import_helper()
    del swig_import_helper
else:
    import _dla
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SiteSampler(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SiteSampler, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SiteSampler, name)
    __repr__ = _swig_repr

    def __init__(self, probabilities: 'double const *'):
        this = _dla.new_SiteSampler(probabilities)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def sample(self, rnd: 'double') -> "unsigned int":
        return _dla.SiteSampler_sample(self, rnd)

    def size(self) -> "unsigned int":
        return _dla.SiteSampler_size(self)
    __swig_destroy__ = _dla.delete_SiteSampler
    __del__ = lambda self: None
SiteSampler_swigregister = _dla.SiteSampler_swigregister
SiteSampler_swigregister(SiteSampler)

class CPP11Random(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CPP11Random, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CPP11Random, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _dla.new_CPP11Random(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __call__(self) -> "double":
        return _dla.CPP11Random___call__(self)
    __swig_destroy__ = _dla.delete_CPP11Random
    __del__ = lambda self: None
CPP11Random_swigregister = _dla.CPP11Random_swigregister
CPP11Random_swigregister(CPP11Random)

class Cluster(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Cluster, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Cluster, name)
    __repr__ = _swig_repr

    def __init__(self, size: 'unsigned int', NumberOfBuffers: 'unsigned int'=1):
        this = _dla.new_Cluster(size, NumberOfBuffers)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dla.delete_Cluster
    __del__ = lambda self: None

    def convert(self, reverseRowNumbers: 'bool'=True) -> "PyObject *":
        return _dla.Cluster_convert(self, reverseRowNumbers)

    def isNear(self, i: 'int', j: 'int') -> "bool":
        return _dla.Cluster_isNear(self, i, j)

    def isFilled(self, i: 'int', j: 'int') -> "bool":
        return _dla.Cluster_isFilled(self, i, j)

    def setCellValue(self, i: 'int', j: 'int') -> "bool":
        return _dla.Cluster_setCellValue(self, i, j)

    def getCounter(self) -> "unsigned long":
        return _dla.Cluster_getCounter(self)

    def getR(self) -> "double":
        return _dla.Cluster_getR(self)

    def dist(self, i: 'int', j: 'int') -> "double":
        return _dla.Cluster_dist(self, i, j)

    def getSize(self) -> "int":
        return _dla.Cluster_getSize(self)
Cluster_swigregister = _dla.Cluster_swigregister
Cluster_swigregister(Cluster)

class Walker(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Walker, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Walker, name)
    __repr__ = _swig_repr

    def __init__(self, probabilities: 'double const *'):
        this = _dla.new_Walker(probabilities)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def step(self, rnd: 'double') -> "void":
        return _dla.Walker_step(self, rnd)

    def setPos(self, i: 'int', j: 'int') -> "void":
        return _dla.Walker_setPos(self, i, j)

    def getI(self) -> "int":
        return _dla.Walker_getI(self)

    def getJ(self) -> "int":
        return _dla.Walker_getJ(self)

    def rmax(self) -> "double":
        return _dla.Walker_rmax(self)
    __swig_destroy__ = _dla.delete_Walker
    __del__ = lambda self: None
Walker_swigregister = _dla.Walker_swigregister
Walker_swigregister(Walker)

class Simulation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Simulation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Simulation, name)
    __repr__ = _swig_repr

    def __init__(self, rad_factor: 'double', gen: 'CPP11Random'):
        this = _dla.new_Simulation(rad_factor, gen)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def walk(self, walker: 'Walker', cluster: 'Cluster') -> "bool":
        return _dla.Simulation_walk(self, walker, cluster)
    __swig_destroy__ = _dla.delete_Simulation
    __del__ = lambda self: None
Simulation_swigregister = _dla.Simulation_swigregister
Simulation_swigregister(Simulation)

# This file is compatible with both classic and new-style classes.


