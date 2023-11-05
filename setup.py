from setuptools import setup, find_packages
import os


def get_file(*paths):
    path = os.path.join(*paths)
    try:
        with open(path, "rb") as f:
            return f.read().decode("utf8")
    except IOError:
        pass


get_readme = lambda: get_file(os.path.dirname(__file__), "README.md")

get_requirements = lambda: get_file(
    os.path.dirname(__file__), "requirements.txt"
).splitlines()


def install():
    setup(
        name="trans",
        version="1.0.0",
        author="blackmarllbor0",
        author_email="3100194@gmail.com",
        url="https://github.com/blackmarllbor0/UI-translator",
        long_description=get_readme(),
        install_requires=get_requirements(),
        keywords=["translator"],
        packages=find_packages(),
        entry_points={
            "console_scripts": [
                "trans = main:main",
            ],
        },
        scripts=["main.py"]
    )


if __name__ == "__main__":
    install()
