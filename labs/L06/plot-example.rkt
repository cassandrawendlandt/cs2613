#lang racket
(require "calculus.rkt")
(require plot)

(plot
 (list
  (function sin -2pi 2pi)
  (function (lambda (x) (deriv sin x)))))


(plot
 (list
  (function cos -2pi 2pi)
  (function (lambda (x) (-(cos x) (deriv sin x)))
            -2pi 2pi)
  ))