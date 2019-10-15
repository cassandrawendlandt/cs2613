let village = require("../village.js");
let VillageState = village.VillageState;
//let randomBot = village.randomRobot; 
describe ("roadGraph", 
    function() {
        let roadGraph = village.roadGraph; 
        it ("Allice's neigbours", 
            function(){
                expect(roadGraph["Alice's House"].sort()).toEqual(["Bob's House", "Cabin","Post Office"]);
                
            });

        it ("Bob's neigbours", 
            function(){
                expect(roadGraph["Bob's House"]).toEqual(jasmine.objectContaining (["Alice's House"]));
                
            });
    });


describe ("Village State ", 
    function() {
        let first = new VillageState(
            "Post Office",
            [{place: "Post Office", address: "Alice's House"},{place: "Mars", address: "Junpiter"}]
        );
        let next = first.move("Alice's House");
        it ("move changes place",
            function (){
                expect(next.place).toEqual("Alice's House");
            });

        it ("parcles deliver", 
            function(){
                expect(next.parcels).toEqual([{place: "Mars", address: "Junpiter"}]);
            }
        );

        it ("move does not modify", 
            function(){
                expect(first.place).toEqual("Post Office");
            });

        it ("invaild destinations", 
            function (){ 
                expect(first.move ("Mars")).toBe(first);
            });
        
       
    });

describe("runRobot",
    function() {
        it("no parcels",
            function() {
                console.log = jasmine.createSpy("log");

                noParcels = new VillageState("Post Office",[]);
                village.runRobot(noParcels);

                expect(console.log).toHaveBeenCalledWith("Done in 0 turns");
            });

        it ("randomBot", 
            function (){
                console.log = jasmine.createSpy("log");
                village.runRobot(VillageState.random(),village.randomRobot);
                
                expect(console.log).toHaveBeenCalledWith(jasmine.stringMatching(/^Done/));
            });
    });
