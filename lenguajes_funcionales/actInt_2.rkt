#lang racket

;; COmplejidad: O(cadenas x longitud x transiciones)
(define (validate automata cadenas)
  ;; Obtenemos cada parte
  (define estados (car automata))
  (define alfabeto (cadr automata))
  (define transiciones (caddr automata))
  (define inicial (cadddr automata))
  (define finales (car (cddddr automata)))

  ;; Encontramos la transición
  (define (findT estado simbolo transiciones)
    (cond
      ((null? transiciones) #f)
      ((and (equal? (caar transiciones) estado)
            (equal? (cadar transiciones) simbolo))
       (caddar transiciones))
      (else (findT estado simbolo (cdr transiciones)))))

  ;; Recorrer la cadena
  (define (acepta? cadena)
    (let loop ((estado-actual inicial)
               (simbolos cadena))
      (cond
        ((null? simbolos) 
         (not (not (member estado-actual finales))))
        (else
         (let ((next (findT estado-actual (car simbolos) transiciones)))
           (if next
               (loop next (cdr simbolos))
               #f))))))

  ;; Aplicamos la función a todas las cadenas
  (map acepta? cadenas))