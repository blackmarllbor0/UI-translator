import sys


class Exit:
    @staticmethod
    def good():
        exit(0)

    @staticmethod
    def error(err):
        sys.exit(err)
