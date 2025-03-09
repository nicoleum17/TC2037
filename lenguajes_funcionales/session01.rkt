#lang racket

;; sum: number number => number
(define sum
  (lambda (a b)
    (+ a b )))

(define area-of-triangle
  (lambda (base height)
    (/ (* base height) 2)))

(define area-of-circle
  (lambda (radious)
    (* radious radious 3.1415)))

(define area-of-ring
  (lambda (inner outer)
    (- (area-of-circle outer)
       (area-of-circle inner))))

(define area-of-cylinder
  (lambda (radious height)
    (* height (area-of-circle radious))))