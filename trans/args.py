import argparse


class ArgParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="Application startup and configuration management"
        )

        self.args = [
            {
                "flags": ["-sc", "--set-config"],
                "help": "enter this arg, if you want to change config",
                "required": False,
                "type": None,
                "choices": None,
                "action": "store_true",
            },
            {
                "flags": ["-src"],
                "help": "select the source language",
                "required": False,
                "type": str,
                "choices": None,
                "action": "store",
            },
            {
                "flags": ["-dest"],
                "help": "select the destional language",
                "required": False,
                "type": str,
                "choices": None,
                "action": "store",
            },
            {
                "flags": ["-api"],
                "help": "choice API from [ google, yandex, deepl ]",
                "required": False,
                "type": str,
                "choices": ["google", "yandex", "deepl"],
                "action": "store",
            },
            {
                "flags": ["-o", "--open"],
                "help": "choice open method from [ terminal, browser ]",
                "required": False,
                "type": bool,
                "choices": [True, False],
                "action": "store",
            },
            {
                "flags": ["-paste"],
                "help": "select true or false to change the value",
                "required": False,
                "type": bool,
                "choices": [True, False],
                "action": "store",
            },
            {
                "flags": ["-copy"],
                "help": "select true or false to change the value",
                "required": False,
                "type": bool,
                "choices": [True, False],
                "action": "store",
            },
            {
                "flags": ["-p", "--print"],
                "help": "select true or false to change the value",
                "required": False,
                "type": bool,
                "choices": [True, False],
                "action": "store",
            },
        ]

    def add_args(self):
        for arg in self.args:
            if arg["type"] is None:
                self.parser.add_argument(
                    *arg["flags"],
                    required=arg["required"],
                    help=arg["help"],
                    action=arg["action"]
                )
            else:
                self.parser.add_argument(
                    *arg["flags"],
                    required=arg["required"],
                    help=arg["help"],
                    type=arg["type"],
                    choices=arg["choices"],
                    action=arg["action"]
                )

        return self.parser.parse_args()
