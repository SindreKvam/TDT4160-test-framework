start:
    li s10, 1 # Holder 1 i s10
    
    add t0, a0, a1    # t0 inneholder f�rste sum
    add t1, a2, a3    # t1 inneholder andre sum
    add t2, a4, a5    # t2 inneholder tredje sum
        
    # s3 og s4 brukes til � sjekke om en av summene er st�rre enn de andre
    # s0, s1 og s2 brukes til � finne hvilken som er st�rst.
    
    slt s3, t1, t0 # Hvis t0 > t1 s� vil s0 inneholde verdien 1
    slt s4, t2, t0 # Hvis t0 > t2 s� vil s1 inneholde verdien 1
    and s0, s3, s4 # Hvis t0 er st�rst vil s0 inneholde verdien 1
    beq s0, s10, t0_largest
    
    # Reset s3 og s4 tilbake til 0
    li s3, 0
    li s4, 0
    
    slt s3, t0, t1 # Hvis t1 > t0 s� vil s0 inneholde verdien 1
    slt s4, t2, t1 # Hvis t1 > t2 s� vil s1 inneholde verdien 1
    and s1, s3, s4 # Hvis t0 er st�rst vil s1 inneholde verdien 1
    beq s1, s10, t1_largest
    
    # Reset s3 og s4 tilbake til 0
    li s3, 0
    li s4, 0
    
    slt s3, t0, t2 # Hvis t0 > t1 s� vil s0 inneholde verdien 1
    slt s4, t1, t2 # Hvis t0 > t2 s� vil s1 inneholde verdien 1
    and s2, s3, s4 # Hvis t0 er st�rst vil s2 inneholde verdien 1
    beq s2, s10, t2_largest

t0_largest:
    mv a0, t0
    j end
    
t1_largest:
    mv a0, t1
    j end
    
t2_largest:
    mv a0, t2
    j end
    
end:
    nop
    
    

    
    
