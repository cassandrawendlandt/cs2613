#lang racket

    (define (odds-evens2 lst)
      (define (helper lst odds evens)
        (cond
          [(empty? lst) (list odds evens)]
          [(odd? (first lst)) (helper (rest lst) (+ odds 1) evens     )]
          [(even? (first lst)) (helper (rest lst)  odds  (+ 1 evens ))]))
      (helper lst 0 0))

    (module+ test
      (require rackunit)
      (define random-list (build-list 100 (lambda (x) (random 1 100))))
      (check-equal? (odds-evens2 (list 3 2 1 1 2 3 4 5 5 6)) (list 6 4))
      (check-equal? (odds-evens2 random-list) (odds-evens2 random-list))
      )

