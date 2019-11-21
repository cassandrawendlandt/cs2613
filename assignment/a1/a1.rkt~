#lang racket

;the functions are restricted to exact positive numbers only


(define (drop-divisible m list)
       (filter (lambda (x) (not (equal? x 0)))
            (map (lambda (x) (cond
                    [(equal? x m) x]
                    [(equal? m 1) x]
                    [(equal? m 0) x]
                    [(equal? (remainder x m) 0) 0 ]
                    [else x ]))list)))



(define (sieve-with div list)
  (cond
    [(empty? div) list]
    [else (drop-divisible (first div)
                          (sieve-with (rest div) list))]))



(define (sieve n)
  (define list (range 2  n))
  (define div (range 2 (add1 (integer-sqrt n))))
  (sieve-with div list))


(module+ test
  (require rackunit)
  (check-equal? (drop-divisible 3 (list 2 3 4 5 6 7 8 9 10)) (list 2 3 4 5 7 8 10))
  (check-equal? (sieve-with '(2 3) (list 2 3 4 5 6 7 8 9 10)) (list 2 3 5 7))
  (check-equal? (sieve 10) (list 2 3 5 7))
  (check-equal? (sieve 30) (filter prime? (range 1 30)))
  (check-equal? (sieve 100000) (filter prime? (range 1 100000)))
  (require math/number-theory))

