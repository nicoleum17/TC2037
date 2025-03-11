#lang racket
;; fahrenheit-to-celsius number => number
(define fahrenheit-to-celsius
  (lambda (fahrenheit)
    (/(* 5(- fahrenheit 32)) 9)))

;; roots number number number => number
(define roots
  (lambda (a b c)
    (/ (- (+ (sqrt (- (* b b) (* 4 a c)))) b) (* 2 a))))