ng racket/base

(define (my-+ a b)
  
  (if (zero? a)
      b
      (my-+ (sub1 a) (add1 b)))
)


(define (my-* a b)
  (if (zero? a)
      0
      (my-+ b (my-* (sub1 a) b)))
)

(provide my-+
         my-*)


(module+ test
         (require rackunit)
         (check-equal? (my-+ 1 1) 2 "Simple addition")
         (check-equal? (my-* 1 2) 2 "Simple multiplication")
)

