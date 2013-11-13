#include <Python.h>
static PyObject *totalIter(PyObject *self, PyObject *args)
{
    PyObject* seq;
    PyObject* item;
    double result;
    /* get one argument as an iterator */
    if(!PyArg_ParseTuple(args, "O", &seq))
        return 0;
    seq = PyObject_GetIter(seq);
    if(!seq)
        return 0;
    /* process data sequentially */
    result = 0.0;
    while((item=PyIter_Next(seq))) {
        PyObject *fitem;
        fitem = PyNumber_Float(item);
        if(!fitem) {
            Py_DECREF(seq);
            Py_DECREF(item);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        result += PyFloat_AS_DOUBLE(fitem);
        Py_DECREF(fitem);
        Py_DECREF(item);
    }
    /* clean up and return result */
    Py_DECREF(seq);
    return Py_BuildValue("d", result);
}
static PyMethodDef totitMethods[] = {
    {"totit", totalIter, METH_VARARGS, "Sum a sequence of numbers."},
    {0} /* sentinel */
};
void
inittotit(void)
{
    (void) Py_InitModule("totit", totitMethods);
}
