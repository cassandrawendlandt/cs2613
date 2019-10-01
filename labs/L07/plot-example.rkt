#lang racket
(require plot)
(require "../L06/calculus.rkt")

(lambda (x) (- (deriv sin x) (cos x)))

    (define (fsub f g)
      (lambda (x) (                ))

    (module+ test
      (require rackunit)
      (define (sin2 x) (integrate cos x))
      (define (cos2 x) (deriv sin x))
      (define epsilon 0.001)
      (define test-points (build-list 20 (lambda (x) (* 2 pi (random)))))
      (for ([x test-points])
        (check-= ((fsub cos cos2) x) 0 epsilon)
        (check-= ((fsub sin sin2) x) 0 epsilon)))











      