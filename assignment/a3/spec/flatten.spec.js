let ms=require("../flatten.js");
/**
    These are the test cases that are provided by the assignment
*/
describe("flatten",
    function () {
        //this tests to see if the base case to make sure when an empty array is entered 
        //an empty array is returned. 
        it("base case",
            function () {
                expect(ms.flatten([])).toEqual([]);
            });
        //this test to make sure when an array of one element is entered then an array 
        //of one element is returned. 
        it("single element",
            function () {
                expect(ms.flatten([1])).toEqual([1]);
                expect(ms.flatten(["foo"])).toEqual(["foo"]);
                expect(ms.flatten([{foo: 1}])).toEqual([{foo: 1}]);
            });
        //this test to see if an array with nested arrays is entered then the function 
        //will just return a single array 
        it("longer list, no mutation",
            function () {
                var data = [[[1],2,[3]],4,[5,6]];
                var orig_data = data;
                
                expect(ms.flatten(data)).toEqual([1,2,3,4,5,6]);
                expect(data).toEqual(orig_data);
            });
        /**
            Extra test cases
        */
        //this tests the function to see if it would work with other elements besides just numbers 
        it("mixed element",
            function () {
                expect(ms.flatten([1, ["a"], "c"])).toEqual([1, "a", "c"]);
            });
        //this tests the function to remove more nested arrays to return a single array. 
        it("longer list",
            function () {
                var data = [[[1],2,[3]],4,[5,6],[7],8,[9,[10,11]]];

                expect(ms.flatten(data)).toEqual([1,2,3,4,5,6,7,8,9,10,11]);
            });
    });



