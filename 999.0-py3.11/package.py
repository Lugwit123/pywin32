# -*- coding: utf-8 -*-
name = "pywin32"
version = "999.0-py3.11"
description = "Python for Windows Extensions (pywin32) for Python 3.11"
authors = ["Mark Hammond"]

requires = ["python-3.11+<3.12"]

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
