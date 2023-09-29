start:   

greatest_divisor:
    mv t1, a0
start_greatest_divisor_for_loop:
    addi t1, t1, -1
    
    rem t2, a0, t1
    beq t2, x0, found_greatest_divisor
        
    j start_greatest_divisor_for_loop
    
found_greatest_divisor:
    mv t0, a0
    mv a0, t1


kvadrattall:
    li t1, 1
start_kvadrattall_for_loop:
    mul t2, t1, t1
    addi t1, t1, 1
    
    beq t2, t0, kvadrattall_true
    blt t2, t0, start_kvadrattall_for_loop
    
kvadrattall_false:
    li a1, 0
    j end
    
kvadrattall_true:
    li a1, 1
    j end
    
end:
    nop