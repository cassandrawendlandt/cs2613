function out = isolated(img)
  results = nbrcount(img);

  out =!results&img;
 

endfunction

%!test
%! A= [1,0,0; 0,0,0; 0,0,1; 1,0,0];
%! assert(isolated(A) == A)

%!test
%! A=[1,0,0;
%!    0,0,0;
%!    0,1,1;
%!    1,0,1];
%! assert(isolated(A) == [1,0,0; 0,0,0; 0,0,0;0,0,0])