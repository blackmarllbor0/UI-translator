#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from UI.terminal.terminal import TerminalUI
from storage import StorageService


def main():
    app = TerminalUI()
    app.run()


if __name__ == "__main__":
    main()
