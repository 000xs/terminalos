#!/bin/bash
pyinstaller --noconfirm --onefile --windowed --name "TerminalOS" \
--hidden-import="terminalos.config" \
--hidden-import="terminalos.core" \
--hidden-import="terminalos.utils" \
--hidden-import="terminalos.apps" \
run_terminalos.py
