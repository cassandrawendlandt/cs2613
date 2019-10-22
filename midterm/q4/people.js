let fs = require("fs");


function read_json_file(filename) {
    let contents = fs.readFileSync(filename);
    return JSON.parse(contents);
}
exports.read_json_file=read_json_file;

class People {
    constructor(jsonFile){
        this.data = read_json_file(jsonFile);
        //console.log(this.data); 
    }

    //this is suppose to return the length of the json file
    //it will return the right number when it is being called and printed properly. 
    length () {
        const keys = Object.values(this.data);
        var length = keys.length;
        return length;
    }

    //the has table function will look through to find the name then call the person class 
    //then it will calculate the difference to find age 
    //then it will create the person object 

    
    
  
}
let people=new People("ancestry.json");
console.log (people.length());
//console.log(people.length);
exports.People = People;