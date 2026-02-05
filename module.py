import ctypes

lib=ctypes.CDLL("./lib.so")

lib.add.argtypes=[ctypes.c_int,ctypes.c_int]
lib.add.restype=ctypes.c_int

class _Point(ctypes.Structure):
    """
    Initialize with only two arguments
    x and y
    """
    _fields_=[
        ("x",ctypes.c_int),
        ("y",ctypes.c_int)
    ]

class Point:
    pass

lib.Point_move.argtypes=[ctypes.POINTER(_Point),
                        ctypes.c_int,ctypes.c_int]
lib.Point_move.restype=None

def get_pointer(a):
    return ctypes.byref(a)

def Point_move(ptr,dx,dy):
    lib.Point_move(get_pointer(ptr),dx,dy)

def add(a,b):
    return lib.add(a,b)
