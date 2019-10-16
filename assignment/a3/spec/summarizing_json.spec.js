let ms=require("../summarizing_json.js");
/**
      The test cases provided by the assignment
*/
describe("summarize_mail",
    function() {

        it("no headers",
            function () {
                expect(ms.summarize_mail("example1.json")).toEqual([{}, {}, {}]);
                expect(ms.summarize_mail("example2.json")).toEqual(Array(10).fill({}));
            });

        it("Subject",
            function () {
                expect(ms.summarize_mail("example1.json","Subject")).toEqual([{Subject: "[notmuch] archive"},
                    {Subject: "Re: [notmuch] archive"},
                    {Subject: "Re: [notmuch] archive"}]);
            });

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

describe("Message class",
    function() {

        it("new message is not null",
            function () {
                expect(testMsg).not.toEqual(null);
            });

        it("subject accessor",
            function () {
                expect(testMsg.subject).toEqual("lunch");
            });
    });

let otherMsg = new ms.Message({"headers": {"Subject" : "dinner", "Date" : "now"}});
it("message is equal to itself",
    function () {
        expect(testMsg.equals(testMsg)).toEqual(true);
    });
it("message is not equal if field changes",
    function () {
        expect(testMsg.equals(otherMsg)).toEqual(false);
    });


/**
    EXTRA TEST CASES
*/

describe("extra summarize_mail",
    function() {

        it("no headers file 2",
            function () {
                expect(ms.summarize_mail("example2.json")).toEqual([{}, {}, {},{},{},{},{},{},{},{}]);
            });

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

        it("From, To",
            function () {
                expect(ms.summarize_mail("example3.json","From","To")).toEqual([
                    {From: "Tamas Papp <tkpapp@gmail.com>", To: "\"linux-thinkpad@linux-thinkpad.org\" <linux-thinkpad@linux-thinkpad.org>"},
                    {From: "Frank Baumeister <baumeisterf@web.de>", To: "linux-thinkpad@linux-thinkpad.org"},
                    {From: "Tamas Papp <tkpapp@gmail.com>", To: "linux-thinkpad@linux-thinkpad.org"},
                    {From: "alfon <alfon.gz@gmail.com>", To: "linux-thinkpad@linux-thinkpad.org"},
                    {From: "Tamas Papp <tkpapp@gmail.com>", To: "linux-thinkpad@linux-thinkpad.org"},
                    {From: "alfon <alfon.gz@gmail.com>", To: "linux-thinkpad@linux-thinkpad.org"}]);
                
            });
    });


let testMsg2 = new Message({"headers": {"Subject" : "lunch", "Date" : "now","From" : "me", "To" : "you"}});

describe("Message class2",
    function() {

        it("new message 2 is not null",
            function () {
                expect(testMsg2).not.toEqual(null);
            });

        it("subject accessor2",
            function () {
                expect(testMsg2.to).toEqual("you");
            });
    });

let otherMsg2 = new ms.Message({"headers": {"Subject" : "lunch", "Date" : "now","From" : "me", "To" : "you"}});
it("message 2 is equal to itself",
    function () {
        expect(testMsg2.equals(testMsg2)).toEqual(true);
    });
it("message 2 is not equal if field changes",
    function () {
        expect(testMsg2.equals(otherMsg2)).toEqual(true);
    });
