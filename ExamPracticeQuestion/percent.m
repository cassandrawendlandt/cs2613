function out=percent(raw, maxes, weights)
  grades = normalize(raw,maxes)
  out = grades.*weights; 
  out = sum (out');
  out = out';
end

%!test
%! #    journal,assgn,  midterm,final
%! mxs=[260,    60,     20,     60];
%! wgt=[20,     30,     20,     30];
%! raw=[234,    54,     18,     54;
%!      195,    45,     15,     45;
%!      260,    0,      20,     0;
%!      0,      60,     0,      60;
%!      200,    40,     17,     33];
%! assert(percent(raw, mxs, wgt), [90;75;40;60;68.88], .01);