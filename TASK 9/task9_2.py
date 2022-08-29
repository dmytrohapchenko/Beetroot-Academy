"""
You can add the custom module directory in PYTHONPATH environment variable, which will augment the default module search paths used by the Python interpreter.

Add the following line to ~/.bashrc, which will have the effect of changing sys.path in Python permanently.

-- export PYTHONPATH=$PYTHONPATH:/custom/path/to/modules --

The specified path will be added to sys.path after the current working directory, but before the default interpreter-supplied paths.
"""