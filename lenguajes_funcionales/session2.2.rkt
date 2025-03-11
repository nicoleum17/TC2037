#lang racket
(define interest
  (lambda (saldo)
    (cond [(<= saldo 1000) (* 0.04 saldo)]
          [(<= saldo 5000)(* 0.045 saldo)]
          [else (* 0.05 saldo)])))

(interest 1000)
(interest 5000)
(interest 5001)

(define how-many
  (lambda (a b c)
    (cond
      [(> (* b b) (* 4 a c)) 2]
      [(= (* b b) (* 4 a c)) 1]
      [else 0])))

(how-many 1 12 1)
(how-many 2 4 2)
(how-many 1 1 1)