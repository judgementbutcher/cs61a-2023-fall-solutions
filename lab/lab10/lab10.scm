(define (over-or-under num1 num2) 'YOUR-CODE-HERE
  (cond 
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    ((> num1 num2) 1)
  )
)

(define (make-adder num) 'YOUR-CODE-HERE
  (lambda (inc) (+ num inc))
)

(define (composed f g) 'YOUR-CODE-HERE
  (lambda (x) (f (g x)))
)

(define (repeat f n) 'YOUR-CODE-HERE
  (lambda (x)
    (cond
      ((= n 0) x)
      ((= n 1) (f x))
      ((> n 1) ((repeat f (- n 2)) ((composed f f) x))) 
    )
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 'YOUR-CODE-HERE
  (cond
    ((zero? a) b)
    ((zero? b) a)
    ((= 0 (modulo (max a b) (min a b))) (min a b))
    (else (gcd (min a b) (modulo (max a b) (min a b))))  
  )



)
