//bootstrap code
@256
D=A
@SP
M=D
//call Sys.init 0
@FUNC_RETURN_0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@LCL
M=D
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
@ARG
M=D
@Sys.init
0;JMP
(FUNC_RETURN_0)
//function Sys.init 0
(Sys.init)
//push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@0
D=A
@3
D=D+A
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@1
D=A
@3
D=D+A
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//call Sys.main 0
@FUNC_RETURN_1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@LCL
M=D
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
@ARG
M=D
@Sys.main
0;JMP
(FUNC_RETURN_1)
//pop temp 1
@1
D=A
@5
D=D+A
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//label LOOP
(Sys.init$LOOP)
//goto LOOP
@Sys.init$LOOP
0;JMP
//function Sys.main 5
(Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@0
D=A
@3
D=D+A
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@1
D=A
@3
D=D+A
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 1
@1
D=A
@LCL
D=D+M
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 2
@2
D=A
@LCL
D=D+M
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 3
@3
D=A
@LCL
D=D+M
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
//call Sys.add12 1
@FUNC_RETURN_2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@LCL
M=D
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
@ARG
M=D
@Sys.add12
0;JMP
(FUNC_RETURN_2)
//pop temp 0
@0
D=A
@5
D=D+A
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 1
@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 4
@4
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
//add
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
//add
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
//add
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
//return
@LCL
D=M
@R13
M=D
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
//function Sys.add12 0
(Sys.add12)
//push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@0
D=A
@3
D=D+A
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@1
D=A
@3
D=D+A
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
//push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 12
@12
D=A
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
//return
@LCL
D=M
@R13
M=D
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
