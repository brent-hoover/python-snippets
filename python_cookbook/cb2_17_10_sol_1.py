void
_Py_CountReferences(FILE *fp)
{
    int nr, no;
    PyObject *op;
    for (nr = no = 0, op = refchain._ob_next;
         op != &refchain;
         op = op->_ob_next, nr += op->ob_refcnt, no += 1)
    { }
    fprintf(fp, "%d refs (%d), %d objs\n", nr, _Py_RefTotal, no);
}
