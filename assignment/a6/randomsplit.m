## usage: [TRAIN,TEST] = randomsplit(MATRIX,RATIO)
##
## randomly splits a matrix into two parts based on the ratio
## MATRIX is the matrix of the sample data. RATIO is the ratio 
## the matrix is being split by. This number is between 0 and 1. TRAIN
## and TEST are matrixs of random rows from MATRIX. If the ratio does
##not split the matrix evenly, TRAIN will get the bigger section
function [train,test] = randomsplit(matrix, ratio)
  randomGen = randperm(rows(matrix)); 
  train = matrix(randomGen(1:round(ratio *rows(matrix))),:);
  test =  matrix(randomGen(round(ratio*rows(matrix))+1:end),:);
endfunction

%!test "Base case, split in two even halfs"
%!  assert(randomsplit(zeros(10,1), 0.5) == [zeros(5,1),zeros(5,1)])

%!test "checking to see if will split in different sizes"
%! [foo, bar] = randomsplit(zeros(10,1), 0.7);
%! assert(foo == zeros(7,1))
%! assert(bar == zeros(3,1))


%!test "checking to see if the function works with odd numbers"
%! [foo, bar] = randomsplit(zeros(15,1), 0.7);
%! assert(foo == zeros(11,1))
%! assert(bar == zeros(4,1))


%!test "checking to see if the function works matrices bigger than 1D"
%! [foo, bar] = randomsplit(zeros(30,4), 0.8);
%! assert(foo == zeros(24,4))
%! assert(bar == zeros(6,4))
