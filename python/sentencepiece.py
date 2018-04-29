# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_sentencepiece')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_sentencepiece')
    _sentencepiece = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sentencepiece', [dirname(__file__)])
        except ImportError:
            import _sentencepiece
            return _sentencepiece
        if fp is not None:
            try:
                _mod = imp.load_module('_sentencepiece', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _sentencepiece = swig_import_helper()
    del swig_import_helper
else:
    import _sentencepiece
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

class SentencePieceProcessor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SentencePieceProcessor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SentencePieceProcessor, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _sentencepiece.new_SentencePieceProcessor()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _sentencepiece.delete_SentencePieceProcessor
    __del__ = lambda self: None

    def Load(self, filename):
        return _sentencepiece.SentencePieceProcessor_Load(self, filename)

    def SetEncodeExtraOptions(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_SetEncodeExtraOptions(self, extra_option)

    def SetDecodeExtraOptions(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_SetDecodeExtraOptions(self, extra_option)

    def GetPieceSize(self):
        return _sentencepiece.SentencePieceProcessor_GetPieceSize(self)

    def PieceToId(self, piece):
        return _sentencepiece.SentencePieceProcessor_PieceToId(self, piece)

    def IdToPiece(self, id):
        return _sentencepiece.SentencePieceProcessor_IdToPiece(self, id)

    def GetScore(self, id):
        return _sentencepiece.SentencePieceProcessor_GetScore(self, id)

    def IsUnknown(self, id):
        return _sentencepiece.SentencePieceProcessor_IsUnknown(self, id)

    def IsControl(self, id):
        return _sentencepiece.SentencePieceProcessor_IsControl(self, id)

    def Encode(self, input):
        return _sentencepiece.SentencePieceProcessor_Encode(self, input)

    def EncodeAsPieces(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsPieces(self, input)

    def EncodeAsIds(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsIds(self, input)

    def NBestEncode(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncode(self, input, nbest_size)

    def NBestEncodeAsPieces(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsPieces(self, input, nbest_size)

    def NBestEncodeAsIds(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsIds(self, input, nbest_size)

    def SampleEncode(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncode(self, input, nbest_size, alpha)

    def SampleEncodeAsPieces(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsPieces(self, input, nbest_size, alpha)

    def SampleEncodeAsIds(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsIds(self, input, nbest_size, alpha)

    def Decode(self, input):
        return _sentencepiece.SentencePieceProcessor_Decode(self, input)

    def DecodePieces(self, input):
        return _sentencepiece.SentencePieceProcessor_DecodePieces(self, input)

    def DecodeIds(self, input):
        return _sentencepiece.SentencePieceProcessor_DecodeIds(self, input)

    def __len__(self):
        return _sentencepiece.SentencePieceProcessor___len__(self)

    def __getitem__(self, key):
        return _sentencepiece.SentencePieceProcessor___getitem__(self, key)
SentencePieceProcessor_swigregister = _sentencepiece.SentencePieceProcessor_swigregister
SentencePieceProcessor_swigregister(SentencePieceProcessor)

class SentencePieceTrainer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SentencePieceTrainer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SentencePieceTrainer, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        Train = staticmethod(_sentencepiece.SentencePieceTrainer_Train)
    else:
        Train = _sentencepiece.SentencePieceTrainer_Train
SentencePieceTrainer_swigregister = _sentencepiece.SentencePieceTrainer_swigregister
SentencePieceTrainer_swigregister(SentencePieceTrainer)

def SentencePieceTrainer_Train(arg):
    return _sentencepiece.SentencePieceTrainer_Train(arg)
SentencePieceTrainer_Train = _sentencepiece.SentencePieceTrainer_Train

# This file is compatible with both classic and new-style classes.


