#lang racket
(require explorer)
(require json)

(define (read-json-file file-name)
  (with-input-from-file file-name read-json))

(define (collect-one-status hash-table)
  (hash-ref hash-table 'status))

(define (visualize-json-file file-name)
  (explore (read-json-file file-name)))


(define (collect-status filename)
  (define json-data (read-json-file filename))
  (map collect-one-status (hash-ref json-data 'errors)))

(module+ test
  (require rackunit)
  (check-equal? (collect-status "errors.json") '("403" "422" "500")))

