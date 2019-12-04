function [out,out2] = randomsplit(array, weights)
  y = array;
 y(10*weights+1:size(y,1))=[] ;
 array([1:1:10*weights],:)=[];
  
  out =y;
  out2 =array;
endfunction

%!assert(randomsplit(zeros(10,1), 0.5) == [zeros(5,1),zeros(5,1)])

%!test
%! [foo, bar] = randomsplit(zeros(10,1), 0.7);
%! assert(foo == zeros(7,1))
%! assert(bar == zeros(3,1))
