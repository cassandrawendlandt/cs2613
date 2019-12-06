## usage: [RESULTS] = ranges(MATRIX)
##
## finds the min and max of each column in a matrix
## MATRIX is the matrix with the data
## RESULTS is a 2D array. The first row contains the minmum
## values for each row and the second row contains the 
##maximum values.
function [results] = ranges(matrix)
  results =[min(matrix);max(matrix)];
endfunction

%!test "base cases" 
%! A=[0,0,0;
%!    0,1,0;
%!    0,0,1;
%!    1,1,1];
%! assert (ranges(A), [0,0,0;
%!                     1,1,1]);

%!test "checks to makes sure it works with negative numbers" 
%! A=[0,0,0;
%!    0,10,0;
%!    0,0,1;
%!    1,1,-11];
%! assert (ranges(A), [0,0,-11;
%!                     1,10,1]);


%!test "tests the function to work when the min and max are the same" 
%! A=[1,0,0;
%!      1,10,0;
%!      1,0,0;
%!      1,1,0];
%! assert (ranges(A), [1,0,0;
%!                     1,10,0]);