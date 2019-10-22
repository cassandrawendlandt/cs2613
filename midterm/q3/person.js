
class Person {
    constructor(name ,age){
        this.name = name; 
        this.age = age; 
    }
    
    birthday(){
        this.name = this.name; 
        this.age = this.age;
        
        return new Person("new"+this.name, this.age+1);
    }
}

exports.Person = Person;