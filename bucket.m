function out = bucket(vec,ranges,p)
  ratios = (vec-ranges(1,:))./ (ranges(2:) -ranges(1,:));
  ratios = ratios(2:end); 
  out = floor(ratios*p)
  out = min(out,p-1)
endfunction
