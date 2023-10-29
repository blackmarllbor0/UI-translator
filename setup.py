from cx_Freeze import setup, Executable

base = None
executables = [Executable("main.py", base=base)]
packages = ["idna", "main", "UI", "API"]
options = {
    "build_exe": {
        "packages": packages,
    },
}

setup(
    name="trans",
    version="1.0.0",
    author="blackmarllbor0",
    author_email="3100194@gmail.com",
    url="https://github.com/blackmarllbor0/UI-translator",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt").read().splitlines(),
    keywords=["translator"],
    options=options,
    executables=executables,
)
