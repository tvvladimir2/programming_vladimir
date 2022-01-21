# Lesson from:
# https://www.youtube.com/watch?v=XKoTwepEzPI

# Description:
# Record keystrokes

# Executing scripts:
# Documentation:
# https://docs.python.org/2/using/windows.html
Python scripts (files with the extension .py) will be executed by python.exe by default.
This executable opens a terminal, which stays open even if the program uses a GUI.
If you do not want this to happen, use the extension .pyw which will cause the script
to be executed by pythonw.exe by default (both executables are located in the top-level
of your Python installation directory). This suppresses the terminal window on startup.

You can also make all .py scripts execute with pythonw.exe,
setting this through the usual facilities, for example (might require administrative rights):

    Launch a command prompt.

    Associate the correct file group with .py scripts:

    assoc .py=Python.File

    Redirect all Python files to the new executable:

    ftype Python.File=C:\Path\to\pythonw.exe "%1" %*
