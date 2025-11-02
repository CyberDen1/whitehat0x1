@echo off
:loop
taskkill /F /IM TCPServer.exe
timeout /t 2 >nul
start "" "TCPServer.exe"
timeout /t 120 >nul
goto loop