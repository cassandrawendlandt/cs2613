#lang racket
;Assignment 2

;code from the assignment 
(require xml)
(define (load-xexpr path)
  (xml->xexpr (document-element (read-xml (open-input-file path)))))

(require explorer)
(define data (load-xexpr "rubrics.xml"))

;Quetion 1: Loading the rubrics
(define (load-rubrics name)
  (filter (lambda (x) (not(equal? x '((schemaversion "v2011")))))
          (filter (lambda (x) (not(equal? x 'rubrics)))(load-xexpr name))))

;testcases for question 1 provided in assignment 
(module+ test
  (require rackunit)
  (define rubrics (load-rubrics  "rubrics.xml"))
  (check-equal? (length rubrics) 5)
  (for ([elt rubrics])
    (check-equal? (first elt) 'rubric)))

;Question 2 Improving assoc  
(define (assoc* key lst )
  (cond
    [(empty? lst) #f]
    [(not(list? (first lst)))
     (assoc* key (rest lst))]
    [(equal? (list-ref(list-ref lst 0)0) key) (list-ref(list-ref lst 0)1)]
    [else (assoc* key (rest lst))]))

;Test cases provided by the assignment 
(module+ test
  (define test-list '(1 [keep 2] 3 [keep 4] [keep 5] 6))
  (check-equal? (assoc* 'keep test-list) 2)
  (check-equal? (assoc* 'discard test-list) #f))

(define (rubric-name rubric)
  (assoc* 'name (second rubric)))

(module+ test
  (check-equal?
   (sort (map rubric-name rubrics) string<=?)
   '("JavaScript Assignment" "Journal Entry" "Octave Assignment" "Python Assignment"
                             "Racket assignment")))
;test cases provided by me
(module+ test
  (define test-list2 '(1 [keep 2] 3 [keep 4] [keep 5] 6 [noce 6] [yo whatsup]))
  (check-equal? (assoc* 'noce test-list2) 6)
  (check-equal? (assoc* 'yo test-list2) 'whatsup))

;Question 3: keeping all the pairs 
(define (assoc-all key lst)
  (define newList(filter pair? lst))
  (define (inter key lst lst2)
    (cond
     [(empty? lst)lst2]
     [(not(equal? (list-ref(list-ref lst 0)0) key))
      (inter key (remove (first lst) lst) lst2)]
     [else 
      (inter key (rest lst) (append lst2 (list (first lst))))]))
  (inter key newList '()))

;test cases provided by the assignment 
(module+ test
  (check-equal? (assoc-all 'keep test-list) '([keep 2] [keep 4] [keep 5] ))
  ;test cases provied by me
  (check-equal? (assoc-all 'test '([keep 2] [keep 4] [test 5] [keep 5] )) '([test 5] )))

;Question 4: Extracting criteria groups 
(define (criteria-groups lst)
    (assoc-all 'criteria_group (list-ref lst 3)))

;Test cases provided by the assignment
(module+ test
  ;; Journals have one group, others have 2
  (check-equal? (sort (map length (map criteria-groups rubrics)) <=)
              '(1 2 2 2 2))
  (check-equal?
   (first ;; tag
   (first ;; first criteria group
     (criteria-groups (first rubrics))))
   'criteria_group)
 ;test case provided by me
  (check-equal?
   (first ;; tag
   (first ;; first criteria group
     (criteria-groups (second rubrics))))
  'criteria_group))

;Question5: Extracting criteria groups 
(define (criteria-names lst)
  (list (getcriname (first(assoc-all 'criterion (list-ref lst 3 ))))
          (getcriname (list-ref (rest(assoc-all 'criterion (list-ref lst 3 )))0))))

(define (criteria-levels lst)
  (assoc-all 'level  (list-ref (list-ref lst 2)2)))

;helper method to get the criteria name
(define (getcriname lst)
   (assoc* 'name (list-ref lst 1)))
 
;Test cases provided by the assignments
(module+ test
  (for ([level  (criteria-levels (first (criteria-groups (first rubrics))))])
    (check-equal? (first level) 'level))
  (check-equal? (sort (criteria-names (first (criteria-groups (first rubrics)))) string<=?)
               '("Content" "Technical skills"))
;test cases provided by me 
  (check-equal? (sort (criteria-names (first (criteria-groups (second rubrics)))) string<=?)
               '("Adequacy of tests" "Correctness")))

;Question 6: Reformatting level information
(define (level-name-score lst)
  (append (getName lst '()) (getLevel lst '()))  )

;helper methods to get the level and name 
(define (getLevel lst sendBack)
  (append sendBack (list (inexact->exact(string->number(assoc* 'level_value  (second lst)))))))

(define (getName lst sendBack)
  (append sendBack (list (assoc* 'name  (list-ref lst 1)))))

;Test cases provided by the assignments 
(module+ test
  (check-equal? (map level-name-score (criteria-levels (first (criteria-groups (first rubrics)))))
                '(("Needs improvement" 0)
                  ("Minimally satifactory" 1)
                  ("Good" 2)
                  ("Excellent" 3)))

;test cases provided by me 
(check-equal? (map level-name-score (criteria-levels (first (criteria-groups (second rubrics)))))
                '(("Needs improvement" 0)
                  ("Minimally satisfactory" 1)
                  ("Good" 2)
                  ("Excellent" 3)))
  
(check-equal? (map level-name-score (criteria-levels (first (criteria-groups (third rubrics)))))
                '(("Needs Improvement" 0)
                  ("Minimally Satisfactory" 1)
                  ("Good" 2)
                  ("Excellent" 3)))
  
(check-equal? (map level-name-score (criteria-levels (first (criteria-groups (fourth rubrics)))))
                '(("Needs Improvement" 0)
                  ("Minimally Satisfactory" 1)
                  ("Good" 2)
                  ("Excellent" 3))))



