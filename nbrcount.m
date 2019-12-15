function res = nbrcount(image)
  mask = [1,1,1;
          1,0,1;
          1,1,1]
  res = conv2(image,mask,"same")
endfunction


