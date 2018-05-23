      program primos
      implicit none
      integer::i,j
      logical::eh_primo=.FALSE.
      !
      print *,"Lista de Primos entre 1-100000"
      print *, 2
      do j=3, 100000
        eh_primo=.TRUE.
        testar_quociente:do i=2, j-1
          if(modulo(j,i) .eq. 0) then
            eh_primo=.FALSE.
            exit testar_quociente
          end if
        end do testar_quociente
        !
        if(eh_primo) then
          print *,j
        end if
      end do
      end program primos    
