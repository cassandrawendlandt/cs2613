
class Person{ 
    constructor (name,age){ 
        this.name = name;  
        this.age = age;
    }
    birthday(self){ 
       return new Person (this.name, this.age+1)        
    }
}


exports.Person = Person;


let fs = require("fs");


function read_json_file(filename) {
    let contents = fs.readFileSync(filename);
    return JSON.parse(contents);
}
exports.read_json_file=read_json_file;

class People { 
    constructor(jsonFile){
        this.data = read_json_file(jsonFile);
        
        this.length = this.data.length;
    }


}

exports.People = People;