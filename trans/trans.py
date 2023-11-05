from trans.args import ArgParser
from trans.env import init_env
from trans.storage import StorageService

from UI.terminal.terminal import TerminalUI


def run():
    app = None
    
    arg_parser = ArgParser()
    args = arg_parser.add_args()

    if args["set_config"] == False:
        storage = StorageService()
        open_in = storage.storage["open_in"]
        
        if open_in == "terminal":
            init_env()

            app = TerminalUI()
            app.run()
        elif args.open == "browser":
            pass
        else:
            pass
    else:
        pass