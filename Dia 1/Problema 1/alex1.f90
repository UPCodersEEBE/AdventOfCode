program alex1
    implicit none
    integer :: n1,n2,er,i
    open( unit = 15, file="pr1.dat", status = "old", action = "read")
    open( unit = 16, file="pr1.dat", status = "old", action = "read")
    i=0
    do
        rewind(16)
        read(unit=15,fmt=*,iostat=er) n1
        if (er.ne.0) then
            exit
        endif
        do
            read(unit=16,fmt=*,iostat=er) n2
            i=i+1
            if (n1+n2.eq.2020) then
                print*,n2*n1
                stop 
            endif
            if (er.ne.0) then
                exit
            endif
        enddo
    enddo
    close(unit=15)
    close(unit=16)
end program alex1