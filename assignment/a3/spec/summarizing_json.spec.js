let ms=require("../summarizing_json.js");
/**
      The test cases provided by the assignment
*/
describe("summarize_mail",
    function() {
        //this tests to make sure if the user does not enter any properties then it returns an empty list. 
        it("no headers",
            function () {
                expect(ms.summarize_mail("example1.json")).toEqual([{}, {}, {}]);
                expect(ms.summarize_mail("example2.json")).toEqual(Array(10).fill({}));
            });
        //this tests to see if the summarize_mail function will return the correct information for the given 
        //property entered by the users. 
        it("Subject",
            function () {
                expect(ms.summarize_mail("example1.json","Subject")).toEqual([{Subject: "[notmuch] archive"},
                    {Subject: "Re: [notmuch] archive"},
                    {Subject: "Re: [notmuch] archive"}]);
            });
        //this checks to see if the function will return the correct information when the user enters more
        //than one property 
        it("Subject, Date",
            function () {
                expect(ms.summarize_mail("example1.json","Subject","Date")).toEqual(
                    [{Subject: "[notmuch] archive", Date: "Tue, 17 Nov 2009 18:21:38 -0500"},
                        {Subject: "Re: [notmuch] archive", Date: "Tue, 17 Nov 2009 18:04:31 -0800"},
                        {Subject: "Re: [notmuch] archive", Date: "Wed, 18 Nov 2009 02:22:12 -0800"}]);
            });
    });

let Message=require("../summarizing_json.js").Message;
let testMsg = new Message({"headers": {"Subject" : "lunch", "Date" : "now"}});
let otherMsg = new ms.Message({"headers": {"Subject" : "dinner", "Date" : "now"}});

describe("Message class",
    function() {
        //this checks to see if the Message class actually works and create a message with a string passed in by the users 
        it("new message is not null",
            function () {
                expect(testMsg).not.toEqual(null);
            });
        //this checks to see if the variable subject has the attribute lunch in it or not 
        it("subject accessor",
            function () {
                expect(testMsg.subject).toEqual("lunch");
            });
        //this tests to see if the equals method in the Message class returns a true result when the messages are equal to each other     
        it("message is equal to itself",
            function () {
                expect(testMsg.equals(testMsg)).toEqual(true);
            });
        //this test to see of the  equals method in the Message class returns a false when the messages are not equal 
        it("message is not equal if field changes",
            function () {
                expect(testMsg.equals(otherMsg)).toEqual(false);
            });
    });


/**
    EXTRA TEST CASES
*/

describe("extra summarize_mail",
    function() {
        //this tests to see if the correct information will be returned when the user only enters 
        //one property and calls a different json file. 
        it("From",
            function () {
                expect(ms.summarize_mail("example3.json","From")).toEqual([
                    {From: "Tamas Papp <tkpapp@gmail.com>"},
                    {From: "Frank Baumeister <baumeisterf@web.de>"},
                    {From: "Tamas Papp <tkpapp@gmail.com>"},
                    {From: "alfon <alfon.gz@gmail.com>"},
                    {From: "Tamas Papp <tkpapp@gmail.com>"},
                    {From: "alfon <alfon.gz@gmail.com>"}]);
            });
        //this checks to see if the correct information will be returned when the user enters two different properties in a different order 
        //than they apppear in the json file. 
        it("From, To",
            function () {
                expect(ms.summarize_mail("example3.json","To","From")).toEqual([
                    { To: "\"linux-thinkpad@linux-thinkpad.org\" <linux-thinkpad@linux-thinkpad.org>",From: "Tamas Papp <tkpapp@gmail.com>"},
                    {To: "linux-thinkpad@linux-thinkpad.org", From: "Frank Baumeister <baumeisterf@web.de>"},
                    {To: "linux-thinkpad@linux-thinkpad.org", From: "Tamas Papp <tkpapp@gmail.com>"},
                    {To: "linux-thinkpad@linux-thinkpad.org", From: "alfon <alfon.gz@gmail.com>" },
                    {To: "linux-thinkpad@linux-thinkpad.org", From: "Tamas Papp <tkpapp@gmail.com>"},
                    {To: "linux-thinkpad@linux-thinkpad.org", From: "alfon <alfon.gz@gmail.com>" }]);
                
            });
    });


let testMsg2 = new Message({"headers": {"Subject" : "lunch", "Date" : "now","From" : "me", "To" : "you"}});
let otherMsg2 = new ms.Message({"headers": {"Subject" : "lunch", "Date" : "now", "To" : "you" ,"From" : "me"}});

describe("Message class2",
    function() {
        //this is a second test case to see if the Message class will creat a method when all the properties have a value. 
        it("new message 2 is not null",
            function () {
                expect(testMsg2).not.toEqual(null);
            });
        //this tests to see if the accessor for to will give the correct results 
        it("to accessor",
            function () {
                expect(testMsg2.to).toEqual("you");
            });
        //this tests to see if the two messages are the same even if the properties were entered in a differennt order
        it("messages are equal if order is different",
            function () {
                expect(testMsg2.equals(otherMsg2)).toEqual(true);
            });
    });




