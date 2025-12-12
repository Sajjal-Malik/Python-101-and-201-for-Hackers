# setup.py
from distutils.core import setup
import py2exe

# This configuration specifies a console application whose entry point is 'demo_script.py'.
# The 'options' dictionary is an optional part used for advanced configurations
# such as including/excluding specific modules or bundling files.
setup(
    console=["demo_script.py"],
    options={
        "py2exe": {
            # Optimization level (0, 1, or 2) to reduce file size.
            "optimize": 2,
            # 3 = don't bundle (default, generally more stable).
            "bundle_files": 3,
            "includes": [],  # Manually include modules py2exe might miss.
            # Exclude unnecessary modules (e.g., Tkinter if using wxPython).
            "excludes": [],
            "dll_excludes": [],  # Exclude specific DLLs from being copied.
        }
    }
)
