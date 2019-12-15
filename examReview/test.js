class Test {
    constructor (number){
        this.number = number;
    }

    inc(){
        this.number += 1;
    }

    mul (b){
        this.number *=b;
    }
}

a =new Test(1);
console.log(a);
console.log(a.number);
a.inc();
console.log(a);

a.mul(100);
console.log(a);