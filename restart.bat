@echo off
:loop
tasklist /fi "imagename eq TCPServer.exe" | find /i "TCPServer.exe" >nul
if errorlevel 1 (
    start "" "C:\TCPServer\TCPServer.exe"
)
timeout /t 5 /nobreak >nul
goto loop