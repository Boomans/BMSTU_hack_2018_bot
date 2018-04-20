#include <stdio.h>
#include <Python.h>

#define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a < _b ? _a : _b; })

static PyObject* distance(PyObject* src, PyObject* dst) {
    const size_t m = (size_t)PyUnicode_GetLength(src);
    const size_t n = (size_t)PyUnicode_GetLength(src);
    if (m == 0) {
        return PyLong_FromSize_t(n);
    }
    if (n == 0) {
        return PyLong_FromSize_t(m);
    }

    unsigned int** matrix = calloc(sizeof(int*), m + 1);

    for (unsigned int i = 0; i <= m; ++i) {
        matrix[i] = calloc(sizeof(int), m + 1);
        matrix[i][0] = i;
    }
    for (unsigned int i = 0; i <= n; ++i) {
        matrix[0][i] = i;
    }

    unsigned int above_cell, left_cell, diagonal_cell, cost;

    for (unsigned int i = 1; i <= m; ++i) {
        for(unsigned int j = 1; j <= n; ++j) {
            if (PyUnicode_ReadChar(src, i - 1) == PyUnicode_ReadChar(dst, j - 1)) {
                cost = 0;
            } else {
                cost = 1;
            }
            above_cell = matrix[i - 1][j];
            left_cell = matrix[i][j - 1];
            diagonal_cell = matrix[i - 1][j - 1];
            matrix[i][j] = min(min(above_cell + 1, left_cell + 1), diagonal_cell + cost);
        }
    }

    return PyLong_FromSize_t(matrix[m][n]);
}

PyMethodDef SpamMethods[] =
        {
                {"distance", (PyCFunction)distance, METH_VARARGS, 0},
                {0,0,0,0}
        };

static struct PyModuleDef levmodule = {
        PyModuleDef_HEAD_INIT,
        "levenshtein",   /* name of module */
        "Ehh, hello modyle", /* module documentation, may be NULL */
        -1,       /* size of per-interpreter state of the module,
			  or -1 if the module keeps state in global variables. */
        SpamMethods
};

PyMODINIT_FUNC
PyInit_levenshtein(void)
{
    return PyModule_Create(&levmodule);
}