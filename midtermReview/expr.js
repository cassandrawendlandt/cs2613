
class Expr {

  constructor (operation, num1, num2){
    this.op = operation;
    this.num1 = num1;
    this.num2 = num2;
  }

  eval(){
    if(typeof this.num1  === "object"){
      if (this.num1.op === '+'){
        this.num1 = this.num1.num1 + this.num1.num2;
      }
      else if (this.num1.op === '*'){
        this.num1 = this.num1.num1 * this.num1.num2;
      }
    }

    if(typeof this.num2  === "object"){
      if (this.num2.op === '+'){
        this.num2 = this.num2.num1 + this.num2.num2;
      }
      else if (this.num2.op === '*'){
        this.num2 = this.num2.num1 * this.num2.num2;
      }
    }
    if (this.op === '+'){
      return (this.num1+this.num2);
    }
    else if (this.op === '*'){
      return (this.num1*this.num2);
    }
  }
}

exports.Expr = Expr;
