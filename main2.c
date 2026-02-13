#include <Python.h>

typedef struct{
    PyObject_HEAD
    int a;
} Obj;

static PyObject* Obj_new(PyTypeObject* tp,PyObject* args,PyObject* kwargs){
    Obj* self;
    self=(Obj*)tp->tp_alloc(tp,0);
    if (!self) return NULL;
    int a;
    if (!PyArg_ParseTuple(args,"i",&a)) return NULL;
    self->a=a;
    return self;
}

static PyTypeObject Obj_t={
    PyVarObject_HEAD_INIT(NULL,0)
    .tp_name="Obj",
    .tp_basicsize=sizeof(Obj),
    .tp_flags=Py_TPFLAGS_DEFAULT,
    .tp_new=Obj_new
};

static PyObject* add(PyObject* self,PyObject* args){
    PyObject* first;
    PyObject* second;
    if (PyArg_ParseTuple(args,"OO",&first,&second)){
        PyObject* res=PyNumber_Add(first,second);
        return res;
    }
    return NULL;
}

static PyMethodDef ModuleMethods[]={
    {"add",add,METH_VARARGS,"adds"},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef moduledef={
    PyModuleDef_HEAD_INIT,
    "module",
    NULL,
    -1,
    ModuleMethods
};

PyMODINIT_FUNC PyInit_lib2(void){
    PyType_Ready(&Obj_t);
    return PyModule_Create(&moduledef);
}
