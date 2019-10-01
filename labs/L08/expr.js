//(string-append "Hello\n" "world!")
("Hello \n" + "world");
console.log("Hello \n" + "world");

//(* (+ 1 2 3) 7)
var z = (1+2+3)*7;
console.log(z);
//(< 41 (* 6 7))
(41 <6*7);
console.log(41 <6*7);

//(equal? (* (+ 1 2 3) 7) 42)
var x = 1 + 2+3;
(x*7 == 42);
console.log(x*7 == 42);

//(equal? "Spongebob" "Squarepants")
("Spongebob" == "Squarepants");
console.log("Spongebob" == "Squarepants");

//(and (equal? (* 6 7) 42) (equal? "Spongebob" "Squarepants"))
(6*7 == 42 && "Spongebob" == "Squarepants");
console.log (6*7 == 42 && "Spongebob" == "Squarepants");

//(equal? 42 (if (< 3 5) (* 6 7) "turnip"))
// eslint-disable-next-line no-constant-condition
var foo = 42 == (3 < 5 ? (6*7) : "turniup");
console.log(foo);


// (or #t (/ 1 0))
(true || 1/0);
console.log (true || 1/0);

// (and #f (/ 1 0))
(false && 1/0);
console.log (false && 1/0);