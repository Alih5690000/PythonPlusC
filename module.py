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


lib.Point_move.argtypes=[ctypes.POINTER(_Point),
                        ctypes.c_int,ctypes.c_int]
lib.Point_move.restype=None


class Point:
    def __init__(self,a,b):
        self.obj=_Point(a,b)
    @property
    def x(self):
        return self.obj.x
    @property
    def y(self):
        return self.obj.y
    def move(self,dx,dy):
        lib.Point_move(ctypes.byref(self.obj),dx,dy)
def get_pointer(a):
    return ctypes.pointer(a)

lib.sumof.argtypes=[ctypes.POINTER(ctypes.c_int),ctypes.c_int]
lib.sumof.restype=ctypes.c_int

def sumof(a):
    arr_t=ctypes.c_int*len(a)
    arr=arr_t(*a)
    return lib.sumof(arr,len(a))

def add(a,b):
    return lib.add(a,b)

lib.stoi.argtypes=[ctypes.c_char_p,ctypes.POINTER(ctypes.c_int)]
lib.stoi.restype=ctypes.c_int

def stoi(a:str)->int:
    res=ctypes.c_int()
    err=lib.stoi(a.encode("utf-8"),ctypes.byref(res))
    if err!=0:
        raise ValueError("stoi error")
    return res.value
