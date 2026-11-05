from pathlib import Path

from setuptools import find_packages, setup

def create_file():
    file_name = Path(__file__).resolve().parent.parent / "pwned.txt"
    with open (file_name, "w") as f:
        f.write("Infiltrated by utils_lib")
        
create_file()

setup(
    name="utils_lib",
    version="0.1.0",
    py_modules=[],
)