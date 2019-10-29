#lang racket 
(define (list->hash lst ht num)
  (define ht (make-hash))

  (helper lst ht num)
)


(define (helper lst ht num)
  (cond
    [(empty? lst) ht]
    [else (hash-set! ht num (first lst))
     (helper (rest lst) ht (add1 num))]))


(module+ test
  (require rackunit)
  (define hash-table (list->hash (list "a" "b" "c") (hash) 1))
  (check-equal? (hash-ref hash-table 1) "a")
  (check-equal? (hash-ref hash-table 2) "b")
  (check-equal? (hash-ref hash-table 3) "c"))