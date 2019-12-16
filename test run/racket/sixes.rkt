#lang racket
(define (sixes-and-sevens lst))


(module+ test
  (require rackunit)
  (check-equal? (sixes-and-sevens '(1 6 7 12)) '(6 7 12)))