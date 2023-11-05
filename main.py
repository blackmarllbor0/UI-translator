#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from UI.terminal.terminal import TerminalUI
from trans.env import init_env


def main():
    init_env()

    app = TerminalUI()
    app.run()


if __name__ == "__main__":
    main()
