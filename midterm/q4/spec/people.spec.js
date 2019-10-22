let People  = require("../people.js").People;

describe("people",
    function() {
        let people=new People("./ancestry.json");
        it("read all records",
            function () {

                let test = people.length();
                console.log(test);
                
                expect(people.length).toEquals(10);
            });

        // it("hash table",
        //     function() {
        //         expect(people["Clara Aernoudts"]).toEqual(new Person("Clara Aernoudts",95));
        //     });
    });