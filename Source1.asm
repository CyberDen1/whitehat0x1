.model flat, stdcall
;----------
include C:\masm32\include\kernel32.inc
include C:\masm32\include\msvcrt.inc

includelib C:\masm32\lib\kernel32.lib
includelib C:\masm32\lib\msvcrt.lib
;----------
.data
s_end DB 13,10,"-- END --",13,10,0
s_msg DB "Vvedite 2 chisla: ", 0
s_format DB "%d %d",0
s_format_out DB "%d + %d = %d",13,10,0
result DD 0
.code
start:
    call main
    invoke crt_printf, offset s_end
    invoke crt__getch
    invoke ExitProcess,0
;----------
main proc
    local x:dword, y:dword
    mov x, 0
    mov y, 0
    invoke crt_printf, offset s_msg
    invoke crt_scanf, offset s_format, addr x, addr y
    mov eax, x
    add eax, y
    mov result, eax
    invoke crt_printf, offset s_format_out, x, y, result
    ret 0
main endp
end start