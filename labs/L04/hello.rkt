(module goodbye racket
  (provide hi)
  (define (hi)
    (displayln "Hello world!"))
  
(module+ test
  (require rackunit)
  (check-equal? (with-output-to-string hi) "Hello world!\n")
   (check-equal? (with-output-to-string hi) (begin (sleep 3) "Hello world!\n")))
  )




  