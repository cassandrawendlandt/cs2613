function join(lst) {
return lst.reduce((acc, curr) => acc.concat(curr), "");
}
exports.join = join;
