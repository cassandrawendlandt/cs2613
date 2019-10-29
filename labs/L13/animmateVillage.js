let village=require("./village.js");

function animate(state,robot,memory,count) {
    console.log("\033c");
    console.log(state.toString());
    console.log("Turn: " + count);

    if(state.parcels.length >0){
        
        let newCount = count + 1;
        let action = robot(state,memory);
        let newState = state.move(action.direction);
        let newMemory = action.memory; 
    
        setTimeout (function (){animate(newState,robot,newMemory, newCount);},300);
    }

}

animate(village.VillageState.random(), village.randomRobot,[],0);