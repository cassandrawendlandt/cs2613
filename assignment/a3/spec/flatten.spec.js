let ms=require("../flatten.js");
/**
    These are the test cases that are provided by the assignment
*/
describe("flatten",
    function () {
        it("base case",
            function () {
                expect(ms.flatten([])).toEqual([]);
            });

        it("single element",
            function () {
                expect(ms.flatten([1])).toEqual([1]);
                expect(ms.flatten(["foo"])).toEqual(["foo"]);
                expect(ms.flatten([{foo: 1}])).toEqual([{foo: 1}]);
            });
            
        it("longer list, no mutation",
            function () {
                var data = [[[1],2,[3]],4,[5,6]];
                var orig_data = data;
                expect(ms.flatten(data)).toEqual([1,2,3,4,5,6]);
                expect(data).toEqual(orig_data);
            });
    });


/**
  Extra test cases
*/

describe("Extra flatten",
    function () {

        it("mixed element",
            function () {
                expect(ms.flatten([1, ["a"], "c"])).toEqual([1, "a", "c"]);
            });

        it("longer list",
            function () {
                var data = [[[1],2,[3]],4,[5,6],[7],8,[9,[10,11]]];

                expect(ms.flatten(data)).toEqual([1,2,3,4,5,6,7,8,9,10,11]);

            });
    });
