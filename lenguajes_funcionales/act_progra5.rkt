#lang racket
;; how-many-positives( list => number )
(define how-many-positives
  (lambda (lst)
    (cond
      [(null? lst)0]
      [(positive? (car lst))
            (+ 1 (how-many-positives(cdr lst)))]
      [else (how-many-positives(cdr lst))])))

;; count ( number list => number)
(define count
  (lambda (n lst)
    (cond
      [(null? lst) 0]
      [(equal? (car lst) n) (+ 1 (count n (cdr lst)))]
      [else (count n (cdr lst))])))