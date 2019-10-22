#lang racket
(define-syntax-rule (And a b)
  (if b a #f))



(module+ test
  (require rackunit)
  (define (die)
    (error 'die "don't run this"))
  (check-equal? (And (die) #f) #f)
  (check-exn exn:fail? (lambda () (and (die) #f))))

(module+ test
      (define-syntax-rule (check-fail expr)
        (check-exn exn:fail? (lambda () expr)))
      (check-fail (and (die) #f))
      (check-fail (And #f (die))))



(define-syntax-rule (Or a b)
  (if b b (if a  a #f)))

;Testing the Or functions
(module+ test

      (check-equal? (Or #t #t) #t)
      (check-equal? (Or #f #t) #t)
      (check-equal? (Or #t #f) #t)
      (check-equal? (Or (die) #t) #t)
      (check-fail (or (die) #t)))
  
 