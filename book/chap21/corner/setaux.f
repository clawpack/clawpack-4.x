c     ============================================
      subroutine setaux(maxmx,maxmy,mbc,mx,my,xlower,ylower,dx,dy,
     &                  maux,aux)
c     ============================================
c
c     # set auxiliary arrays 
c     # variable coefficient acoustics
c     #  aux(1,i,j) = impedance Z in (i,j) cell
c     #  aux(2,i,j) = sound speed c in (i,j) cell
c
c     # Piecewise constant medium with single interface at x=0.5
c     # Density and sound speed to left and right are set in setprob.f

c
c     
      implicit double precision (a-h,o-z)
c     dimension aux(2,1-mbc:maxmx+mbc,1-mbc:maxmy+mbc)
      dimension aux(maux,1-mbc:maxmx+mbc,1-mbc:maxmy+mbc)
      common /comaux/ zl,cl,zr,cr
c
c     # density and bulk moduli:
      rhol = zl/cl
      rhor = zr/cr
      bulkl = cl**2 * rhol
      bulkr = cr**2 * rhor

      do 30 j=1-mbc,my+mbc
       do 20 i=1-mbc,mx+mbc
          xl = xlower + (i-1.0d0)*dx
          yl = ylower + (j-1.0d0)*dy

c         # determine what fraction wl of this cell lies to the 
c         # "left" of the interface:
	  call cellave(xl,yl,dx,dy,wl)
	  wr = 1.d0 - wl

c         # average density:
	  rho = wl*rhol + wr*rhor

c         # harmonic average bulk modulus:
	  bulk = 1.d0 / (wl/bulkl + wr/bulkr)

c         # average sound speed:
	  aux(2,i,j) = dsqrt(bulk/rho)

c         # average impedance:
	  aux(1,i,j) = rho*aux(2,i,j)

   20     continue
   30    continue

       return
       end
