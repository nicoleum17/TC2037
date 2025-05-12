#lang racket
;; powkitty number number => number
(define powkitty
  (lambda (n p)
         (cond
           [(= p 0) 1]
           [else (* n (powkitty n (sub1 p)))])))

;; dividing-by-subtraction number number => number
(define dividing-by-subtraction
  (lambda (a b)
    (cond
      [(< a b) 0]
      [else (+ 1 (dividing-by-subtraction (- a b) b))])))