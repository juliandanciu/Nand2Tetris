//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_0
D;JEQ
@SP
A=M-1
M=0
(END_0)
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_1
D;JEQ
@SP
A=M-1
M=0
(END_1)
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_2
D;JEQ
@SP
A=M-1
M=0
(END_2)
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_3
D;JLT
@SP
A=M-1
M=0
(END_3)
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_4
D;JLT
@SP
A=M-1
M=0
(END_4)
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_5
D;JLT
@SP
A=M-1
M=0
(END_5)
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_6
D;JGT
@SP
A=M-1
M=0
(END_6)
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_7
D;JGT
@SP
A=M-1
M=0
(END_7)
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@END_8
D;JGT
@SP
A=M-1
M=0
(END_8)
//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 53
@53
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
//push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
//neg
@SP
A=M-1
M=-M
//and
@SP
A=M-1
D=M
A=A-1
M=M&D
@SP
M=M-1
//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or
@SP
A=M-1
D=M
A=A-1
M=M|D
@SP
M=M-1
//not
@SP
A=M-1
M=!M