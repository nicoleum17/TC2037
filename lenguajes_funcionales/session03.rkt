#lang racket
(define sum
  (lambda (n)
    (cond
      [(= n 0) 0]
      [else (+ n (sum(sub1 n)))]
      )))

(define count-digits
  (lambda (n)
    (cond
      [(< n 10) 1]
      [else (+ 1 (count-digits(quotient n 10)))])))

(define factorial
  (lambda (n)
    (cond
      [(= n 1) 1]
      [else (* n (factorial (sub1 n)))])))

(define fibo
  (lambda (n)
    (cond
      [(= n 1) 1]
      [(= n 2) 1]
      [else (+ (fibo (sub1 n ))
               (fibo (- n 2)))])))