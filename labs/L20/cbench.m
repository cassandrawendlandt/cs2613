function cbench
  ctimeit(@fib, 42, 100000)
  ctimeit(@fibmat, 42, 100000)
endfunction