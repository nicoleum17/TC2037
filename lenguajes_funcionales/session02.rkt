#lang racket
;; if (condicion) regresa sino
(define max2
  (lambda (a b)
    (if(> a b) a b)))

(define max3
  (lambda (a b c)
    (max2 a (max2 b c))))

(define max4
  (lambda (a b c)
    (if (> a b)
        (if (> a b) a c)
        (if (> b c) b c))))