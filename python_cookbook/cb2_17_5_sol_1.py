%typedef BOOL BOOLAPI
%typemap(python,except) BOOLAPI {
      Py_BEGIN_ALLOW_THREADS
      $function
        Py_END_ALLOW_THREADS
        if (!$source)  {
              $cleanup
               return PyWin_SetAPIError("$name");
        }
}
