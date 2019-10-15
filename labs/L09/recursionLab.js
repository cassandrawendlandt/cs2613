
function plus(a,b) {
    if (a === 0) {
        return b;
    } else {
        return plus(a-1, b+1);
    }
}

function mult(a,b) {
    if (a===0) {
        return 0;
    } else {
        
        return plus (b, mult (a-1, b));

    }
}


(console.log (mult ( 4, 6)));
(console.log (plus ( 4, 6)));