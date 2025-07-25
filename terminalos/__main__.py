from .cli import main

from .core.app import TerminalOSApp


def main():
    """Entry point for terminalos command"""
    app = TerminalOSApp()
    app.run()


if __name__ == "__main__":
    main()
