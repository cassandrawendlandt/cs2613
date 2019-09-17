#lang scribble/manual
@(define (hello) "hello")
@(define (todo hdr . lst) (list (bold hdr) (apply itemlist (map item lst))))
Title: Scribble Demo
Date: 2019-09-17T12:52:22


Replace this with your post text. Add one or more comma-separated
Tags above. The special tag `DRAFT` will prevent the post from being
published.


@hello{}
@todo["Shopping" "cheese" "fish" "shuriken"]
<!-- more -->

