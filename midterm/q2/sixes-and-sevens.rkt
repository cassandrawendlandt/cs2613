#lang racket

(define (sixes-and-sevens lst)
    (define (helper lst acc)
      (cond
        [(empty? lst) acc]
        [(equal? (remainder (first lst) 6) 0) (helper (rest lst) acc)]
        [(equal? (remainder (first lst) 7) 0)(helper (rest lst) acc)]
        [else (helper (rest lst) (remove (first lst) acc))]))
  (helper lst lst))
        

(module+ test
  (require rackunit)
  (check-equal? (sixes-and-sevens '(1 6 7 12)) '(6 7 12))
  (check-equal? (sixes-and-sevens '(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18)) '(6 7 12 14 18))
  (check-equal? (sixes-and-sevens '(6 12 18 19 24 30 32 36 42)) '(6 12 18 24 30 36 42))
  (check-equal? (sixes-and-sevens '(6 7 12 14 21 28 60 90 100 200)) '(6 7 12 14 21 28 60 90)))