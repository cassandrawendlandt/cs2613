#lang racket
(require xml)
(define (load-xexpr path)
  (xml->xexpr (document-element (read-xml (open-input-file path)))))


(require explorer)
(define data (load-xexpr "rubrics.xml"))



;quetion 1
(define (load-rubrics name)

  (filter (lambda (x) (not(equal? x '((schemaversion "v2011")))))
          (filter (lambda (x) (not(equal? x 'rubrics)))(load-xexpr name)))
  
)




(explore (load-rubrics "rubrics.xml"))



(module+ test
  (require rackunit)
  (define rubrics (load-rubrics  "rubrics.xml"))
  (check-equal? (length rubrics) 5)
  (for ([elt rubrics])
    (check-equal? (first elt) 'rubric)))


(define (asso* key help )
  (define list(load-rubrics "rubrics.xml"))
  (map (lambda (x) (list-ref (list-ref x 1) 2)) list)
  )


(explore (asso* 0 0))

(define (rubric-name rubric)
  (asso* 'name (second rubric)))



