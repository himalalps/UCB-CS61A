(define nil '())
(define s (cons 1 (cons 2 nil)))
(cons (cons 4 (cons 3 nil)) s)
(car (cons (cons 4 (cons 3 nil)) s))
(cons s (cons s nil))

(list? s)
(null? nil)
(list 1 2 3 4)

(list 1 'a)
(car (cdr (car (cdr '(1 (2 3) 4)))))

(append s s)
(list s s s s)
(map even? s)
(filter even? s)
(apply quotient '(10 5))
(map + '(1 2 3 4))

;;; Non-empty subsets of integer list s that have an even sum
(define (even-subsets s) 
    (if (null? s) nil
        (append (even-subsets (cdr s))
                (map (lambda (t) (cons (car s) t))
                    (if (even? (car s))
                        (even-subsets (cdr s))
                        (odd-subsets (cdr s))))
                ; nothing if (car s) is odd or one thing
                (if (even? (car s)) (list (list (car s))) nil))))

;;; Non-empty subsets of integer list s that have an odd sum
(define (odd-subsets s) 
    (if (null? s) nil
        (append (odd-subsets (cdr s))
                (map (lambda (t) (cons (car s) t))
                    (if (odd? (car s))
                        (even-subsets (cdr s))
                        (odd-subsets (cdr s))))
                ; nothing if (car s) is even or one thing
                (if (odd? (car s)) (list (list (car s))) nil))))

;;; non-empty subsets of s
(define (nonempty-subsets s)
    (if (null? s) nil
        (let ((rest (nonempty-subsets (cdr s))))
            (append rest
                    (map (lambda (t) (cons (car s) t)) rest)
                    (list (list (car s)))))))

;;; non-empty subsets of integer list s that have an even sum
(define (even-subsets s)
    (filter (lambda (s) (even? (apply + s))) (nonempty-subsets s)))