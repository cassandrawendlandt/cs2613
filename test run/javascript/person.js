
class Person {
    constructor (name, age){
        this.name = name; 
        this.age = age;
    }
    birthday() {
        return  new Person (this.name,this.age+1);
    }
}

exports.Person=Person;


let read_json_file=require("./read_json_file.js").read_json_file;

class People{ 
    constructor (file){
        let data=read_json_file(file);
        this.length = data.length; 

        for (let i = 0;i<this.length;i++){
            this [data[i].name] = new Person(data[i].name, data[i].died-data[i].born);
        }

    }
}


exports.People = People; 