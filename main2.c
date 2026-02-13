#include <Python.h>

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
    return PyModule_Create(&moduledef);
}
