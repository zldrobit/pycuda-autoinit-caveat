#include <Python.h>

int main()
{
    PyObject *pModule;

    Py_Initialize();
    if (!Py_IsInitialized())
    {
        printf("py init failed\n");
        goto fail;
    }
    PyRun_SimpleString("import sys");   
    PyRun_SimpleString("sys.path.append('./')");
    PyRun_SimpleString("print(sys.path)");
    pModule = PyImport_ImportModule("good");
    if (pModule == NULL)
    {
        printf("import module failed\n");
        goto fail;
    }
fail:
    return 0;
}

