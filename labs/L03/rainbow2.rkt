#lang slideshow
(define (square n)
  	 ; A semi-colon starts a line comment.
  	 ; The expression below is the function body.
	(filled-rectangle n n))

(define (rainbow2 p)
  (define (color-mapper p color-list)
    (cond
      [(empty? color-list) empty]
      [else (cons (colorize p (first color-list))
                  (color-mapper p (rest color-list)))]))
  (color-mapper p (list "red" "orange" "yellow" "green" "blue" "purple")))



