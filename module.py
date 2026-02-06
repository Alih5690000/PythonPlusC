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

def sumof_raw(a,length):
    return lib.sumof(a,length)

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

class _ArrayInt(ctypes.Structure):
    _fields_=[
        ("size",ctypes.c_int),
        ("data",ctypes.POINTER(ctypes.c_int))
    ]

class Pointer:
    def __init__(self,ptr):
        self._ptr=ptr
    @property
    def value(self):
        return self._ptr.contents.value
    @value.setter
    def value(self,a):
        self._ptr.contents.value=a;

lib.ArrayInt_init.argtypes=[ctypes.POINTER(_ArrayInt),ctypes.c_int]
lib.ArrayInt_init.restype=None

lib.ArrayInt_data.argtypes=[ctypes.POINTER(_ArrayInt)]
lib.ArrayInt_data.restype=ctypes.POINTER(ctypes.c_int)

class ArrayInt:
    def __init__(self,size):
        self._obj=_ArrayInt(size)
        lib.ArrayInt_init(ctypes.byref(self._obj),size)
    def __getitem__(self,index)->Pointer:
        if index<0 or index>=self._obj.size:
            raise ValueError("Invalid index")
        return lib.ArrayInt_data(ctypes.byref(self._obj))[index]
    def __setitem__(self,index,val):
        lib.ArrayInt_data(ctypes.byref(self._obj))[index]=val
    
