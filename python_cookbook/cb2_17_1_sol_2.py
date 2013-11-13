#include "Python.h"
/* type-definition and utility-macros */
typedef struct {
    PyObject_HEAD
    PyObject *car, *cdr;
} cons_cell;
staticforward PyTypeObject cons_type;
/* a type-testing macro (we don't actually use it here) */
#define is_cons(v) ((v)->ob_type == &cons_type)
/* utility macros to access car and cdr, as either lvalues or rvalues */
#define carof(v) (((cons_cell*)(v))->car)
#define cdrof(v) (((cons_cell*)(v))->cdr)
/* ctor ("internal" factory-function) and dtor */
static cons_cell*
cons_new(PyObject *car, PyObject *cdr)
{
    cons_cell *cons = PyObject_New(cons_cell, &cons_type);
    if(cons) {
        cons->car = car; Py_INCREF(car); /* INCREF when holding a PyObject */
        cons->cdr = cdr; Py_INCREF(cdr); /* ditto */
    }
    return cons;
}
static void
cons_dealloc(cons_cell* cons)
{
    /* DECREF when releasing previously-held PyObject*'s */
    Py_DECREF(cons->car); Py_DECREF(cons->cdr);
    PyObject_Del(cons);
}
/* A minimal Python type-object */
statichere PyTypeObject cons_type = {
    PyObject_HEAD_INIT(0)     /* initialize to 0 to ensure Win32 portability */
    0,                        /* ob_size */
    "cons",                   /* tp_name */
    sizeof(cons_cell),        /* tp_basicsize */
    0,                        /* tp_itemsize */
    /* methods */
    (destructor)cons_dealloc, /* tp_dealloc */
    /* implied by ISO C: all zeros thereafter, i.e., no other method */
};
/* module-functions */
static PyObject*
cons(PyObject *self, PyObject *args)    /* the exposed factory-function */
{
    PyObject *car, *cdr;
    if(!PyArg_ParseTuple(args, "OO", &car, &cdr))
        return 0;
    return (PyObject*)cons_new(car, cdr);
}
static PyObject*
car(PyObject *self, PyObject *args)     /* car-accessor */
{
    PyObject *cons;
    if(!PyArg_ParseTuple(args, "O!", &cons_type, &cons)) /* type-checked */
        return 0;
    return Py_BuildValue("O", carof(cons));
}
static PyObject*
cdr(PyObject *self, PyObject *args)     /* cdr-accessor */
{
    PyObject *cons;
    if(!PyArg_ParseTuple(args, "O!", &cons_type, &cons)) /* type-checked */
        return 0;
    return Py_BuildValue("O", cdrof(cons));
}
static PyObject*
setcar(PyObject *self, PyObject *args)  /* car-setter */
{
    PyObject *cons;
    PyObject *value;
    if(!PyArg_ParseTuple(args, "O!O", &cons_type, &cons, &value))
        return 0;
    Py_INCREF(value);
    Py_DECREF(carof(cons));
    carof(cons) = value;
    return Py_BuildValue("");
}
static PyObject*
setcdr(PyObject *self, PyObject *args)  /* cdr-setter */
{
    PyObject *cons;
    PyObject *value;
    if(!PyArg_ParseTuple(args, "O!O", &cons_type, &cons, &value))
        return 0;
    Py_INCREF(value);
    Py_DECREF(cdrof(cons));
    cdrof(cons) = value;
    return Py_BuildValue("");
}
static PyMethodDef elemlist_module_functions[] = {
    {"cons",   cons,   METH_VARARGS},
    {"car",    car,    METH_VARARGS},
    {"cdr",    cdr,    METH_VARARGS},
    {"setcar", setcar, METH_VARARGS},
    {"setcdr", setcdr, METH_VARARGS},
    {0, 0}
};
/* module entry-point (module-initialization) function */
void
initelemlist(void)
{
    /* Create the module, with its functions */
    PyObject *m = Py_InitModule("elemlist", elemlist_module_functions);
    /* Finish initializing the type-objects */
    cons_type.ob_type = &PyType_Type;
}
