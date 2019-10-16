function flatten (array) {
    var returnArray = [];
    //loops through the array that is passed in
    for (var i = 0; i < array.length; i++) {
    //if the element in the array is a array then it
    //recursively calls itself again.
        if (Array.isArray(array[i])) {
            returnArray = returnArray.concat(flatten(array[i]));
        }//end of if
        //otherwise push the element to the return array
        else {
            returnArray.push(array[i]);
        }//end of else
    }//end of for
    return returnArray;
}//end of flatten function

exports.flatten = flatten;
