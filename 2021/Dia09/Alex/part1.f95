program part1
    implicit none
    character (len=200) :: filename, row
    integer :: iostat, cols, rows, col, i, j, height
    integer, dimension (:,:), allocatable :: grid
    integer :: total

    filename = "input.dat"
    
    open(unit=1, file=filename, status="old", action="read")
    
    ! get grid dimensions
    rows = 0
    cols = 0
    do
        read(unit = 1, fmt = *, iostat = iostat) row
        if (iostat .ne. 0) exit
        if ( cols .eq. 0 ) cols = len_trim(row)
        rows = rows + 1 
    enddo    
    
    
    ! save to grid
    allocate(grid(rows,cols))
    grid = 0
    
    rewind(1)
    do i = 1, rows
        read(unit = 1, fmt = *, iostat = iostat) row
        if (iostat .ne. 0) exit
        do j = 1, cols
            read (row(j:j), "(i10)") height
            grid(i,j) = height
        end do
    enddo

    total = 0
    do i = 1, rows
        do j = 1, cols
            height = grid(i,j)
            ! up
            if ( i .gt. 1) then
                if ( height .ge. grid(i-1,j) ) cycle            
            endif
            ! down
            if ( i .lt. rows) then
                if ( height .ge. grid(i+1,j) ) cycle            
            endif
            ! left
            if ( j .gt. 1) then
                if ( height .ge. grid(i,j-1) ) cycle            
            endif
            ! right
            if ( j .lt. cols) then
                if ( height .ge. grid(i,j+1) ) cycle            
            endif
            total = total + grid( i,j ) + 1
        end do
    end do

    print*, "Result", total
    
    deallocate(grid)

end program part1