/**
 * running annimation without using the for loop. 
 */
function animate(iterations) {
    let i=0;
    let str="";
    let timer = null;
    function frame() {
        // add code here
        i++; 
        str+="*";
        console.log('\033c');
        console.log(str);
        if (i>=iterations){
            clearInterval(timer);
            console.log("All done!");
        }
    }
    timer=setInterval(frame,300);
}
animate(20);