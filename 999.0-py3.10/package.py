# -*- coding: utf-8 -*-
name = "pywin32"
version = "999.0-py3.10"
description = "Python for Windows Extensions (pywin32) for Python 3.10"
authors = ["Mark Hammond"]

requires = ["python-3.10+<3.11"]

build_command = False
cachable = True
relocatable = True


def commands():
    import platform

    if platform.system() == "Windows":
        env.PYTHONPATH.prepend("{root}")
        env.PYTHONPATH.prepend("{root}\\win32")
        env.PYTHONPATH.prepend("{root}\\win32\\lib")
        env.PATH.prepend("{root}\\pywin32_system32")
        env.PATH.prepend("{root}\\win32")
        env.PYWIN32_ROOT = "{root}"
