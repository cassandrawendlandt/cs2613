## usage: [RESULT] = hash(ARRAY)
##
## Finds the most votes for each row. 
## ARRAY is the array of votes. there is one column per class
## RESULT is the array of column indexs for each row. If there is
## no votes for then the value will be the number of columns +1
function result= tally(array)
  [value,indices] = max(array');
  indices(value ==0) =columns(array)+1;
  result = indices'; 
endfunction

%!test "basic test" 
%! A = [1,2,3;
%!     2,1,3;
%!     2,3,1;
%!     3,1,2;
%!     3,2,1;
%!     0,0,0];
%! assert (tally(A) == [3;3;2;1;1;4]);


%!test "checks if it will take value if the rest in the row are zero" 
%! A = [1,2,3;
%!     2,1,3;
%!     2,3,1;
%!     3,1,2;
%!     3,2,1;
%!     0,4,0];
%! assert (tally(A) == [3;3;2;1;1;2]);


%!test "checks if it can handle negative numbers" 
%! A = [1,2,-3;
%!     2,1,3;
%!     2,-3,1;
%!     3,1,2;
%!     3,2,1;
%!     0,4,0];
%! assert (tally(A) == [2;3;1;1;1;2]);


%!test "checks to see if returns correct answer with multiple size arrays" 
%! A = [1,2,3,10;
%!     2,1,3,0;
%!     2,3,1,9;
%!     0,0,0,0;
%!     0,3,2,1;
%!     0,4,0,0];
%! assert (tally(A) == [4;3;4;5;2;2]);