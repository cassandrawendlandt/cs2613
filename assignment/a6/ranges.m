function [out] = ranges(array)
  out =[min(array);max(array)];
endfunction



%!test
%! A=[0,0,0;
%!    0,1,0;
%!    0,0,1;
%!    1,1,1];
%! assert (ranges(A), [0,0,0;
%!                     1,1,1]);

%!test
%! A=[0,0,0;
%!    0,10,0;
%!    0,0,1;
%!    1,1,-11];
%! assert (ranges(A), [0,0,-11;
%!                     1,10,1]);