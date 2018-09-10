// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

    @sum //set the sum to 0
    M=0

    @i //set the iterator to 0
    M=0

    @R2 //set the place we will eventually place the sum to zero
    M=0

    @R0 //check if the first input is zero
    D=M
    @ZERO
    D;JEQ

    @R1 //check if the second input is zero
    D=M
    @ZERO
    D;JEQ

(LOOP)   //multiply the two numbers by using addition loop
    @sum
    D=M
    @R0
    D=D+M
    @sum
    M=D
    @i
    MD=M+1
    @R1
    D=M-D
    
    @LOOP
    D; JNE //continue loop or jump out 
    
    @sum  
    D=M
    @R2
    M=D

    @END
    0;JMP

(ZERO)
    @R2
    M=0
    @END
    0;JMP

(END)
    @END
    0;JMP

