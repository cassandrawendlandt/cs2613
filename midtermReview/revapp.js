function revapp(){
  args = Array.prototype.slice.call(arguments, 0);

  var reversed = args.reverse();
  var str = ""
  reversed.forEach (l=> str = str + l)
  return str;

}
exports.revapp = revapp
//console.log(revapp("a","b","c","d"))
