
class Person{ 
    constructor (name,age){ 
        this.name = name;  
        this.age = age;
    }
    birthday(){ 
        return new Person (this.name, this.age+1);        
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
        let data = read_json_file(jsonFile);
        
        for (var i =0 ; i < data.length; i++) {
            this [data[i].name] = new Person(data[i].name,data[i].died-data[i].born);
            

        } 
        
        this.length = data.length;
        
    }


}

exports.People = People;