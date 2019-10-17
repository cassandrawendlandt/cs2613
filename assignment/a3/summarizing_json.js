let fs = require("fs");
let flat = require("./flatten.js");

/**
    Function provided in the assignment
  */
function read_json_file(filename) {
    let contents = fs.readFileSync(filename);
    return JSON.parse(contents);
}
exports.read_json_file=read_json_file;

/**
summarize_mail is the function for part two of the assignment.
reads one of a JSON file and returns a list of objects with
the specified properties.
*/
function summarize_mail(jsonFile) {
    var args = [];
    //getting the list of properties the user inputted
    args = Array.prototype.slice.call(arguments, 1);
    var data = read_json_file(jsonFile);
    //the json file flattened
    var flattened_data = flat.flatten(data);
    var summarized_data = [];
    //looping through the flattened data by item
    flattened_data.forEach(function(item) {
        var obj = {};
        //if the user did not submit any properties it returns an empty
        //list
        if (args.length === 0 ){
            summarized_data.push(obj);
        }//if
        //otherwise looks for it
        else {
            //loops through each key in the header section
            const subKeys = Object.keys(item["headers"]);
            for (const i in subKeys) {
                //loops through the length of the list of properties entered
                //by the user
                for (var x = 0; x <args.length;x++) {
                    //if the key is the same as what the user entered then
                    //it is added to the list to be returned.
                    if(subKeys[i] === args[x]) {
                        obj[args[x]] = item["headers"][subKeys[i]];
                    }//subkey if
                }//fo
            }//i for
            //adds the properties to the list to be returned
            summarized_data.push(obj);
            obj = {};
        }//closes the else
    }); //end of the for each
    return summarized_data;
}//function summarize_mail

/**
  Question 3; creating a class for message
*/
class Message {
    constructor (message){
        this.subject  = message.headers.Subject;
        this.date  = message.headers.Date;
        this.from  = message.headers.From;
        this.to  = message.headers.To;
    }//end of constructor

    /**
        Function created for the second part of question 3
      */
    equals (testMessage){
        //gets the list of keys in the messages
        const keys = Object.keys(testMessage);
        //loops through the messages keys
        for (const key of keys){
            //if the values at the keys are not the same then it will return false
            if (testMessage[key] !== this[key]){
                return false;
            }//end of if
        }//end of for
        return true;
    }//end of function
}//end of class

exports.Message = Message;
exports.summarize_mail = summarize_mail;
