let read_json_file=require("./read_json_file.js").read_json_file;

let data=read_json_file("ancestry.json");

let names = [];

for (let i=0; i<data.length; i++){
    names.push(data[i].name);
}

exports.names=names;

function shuffle (array) {
    let dest=array.length;

    for (let dest=array.length-1; dest>0; dest--) {

        let source = Math.floor(Math.random() * dest);
        let tmp = array[dest];
        array[dest] = array[source];
        array[source]=tmp;
    }
}

exports.shuffle=shuffle;