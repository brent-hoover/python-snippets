#include "Python.h"
     extern int gcd(int, int);
     PyObject *wrap_gcd(PyObject *self, PyObject *args) {
         int x, y, g;
         if(!PyArg_ParseTuple(args, "ii", &x, &y))
            return NULL;
         g = gcd(x, y);
         return Py_BuildValue("i", g);
     }
     /* List of all functions in the module */
     static PyMethodDef spammethods[] = {
        {"gcd", wrap_gcd, METH_VARARGS },
        { NULL, NULL }
     };
     /* Module initialization function */
     void initspam(void) {
         Py_InitModule("spam", spammethods);
     }
