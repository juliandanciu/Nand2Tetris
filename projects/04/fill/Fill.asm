// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
    @8192 //number of registers in the screen memory map
    D=A
    @R0 //store the number in R0
    M=D

    @itr //initialize the iterator
    M=0

(CHECK)
    @KBD
    D=M
    @DARK
    D;JNE
    @LIGHT
    0;JMP

(DARK)
    @itr
    D=M
    @R0
    D=M-D
    @CHECK
    D;JEQ
    @itr
    D=M
    @SCREEN
    A=D+A
    M=-1
    @itr
    M=M+1
    
    @CHECK
    0;JMP

(LIGHT)
    @itr
    D=M
    @CHECK
    D;JEQ
    @itr
    D=M-1
    @SCREEN
    A=D+A
    M=0
    @itr
    M=M-1
    
    @CHECK
    0;JMP
    

