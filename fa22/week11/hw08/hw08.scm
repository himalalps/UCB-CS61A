(define (my-filter pred s) 
	(if (null? s) s
		(if (pred (car s)) (cons (car s) (my-filter pred (cdr s))) (my-filter pred (cdr s)))))

(define (interleave lst1 lst2) 
	(if (null? lst1) lst2
		(if (null? lst2) lst1
			(cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))))

(define (accumulate joiner start n term)
	(joiner start
		(fact_fn joiner n term)))

(define (fact_fn joiner n term)
	(if (= n 1) (term n)
		(joiner (term n) (fact_fn joiner (- n 1) term))))

(define (no-repeats lst) 
	(if (null? lst) lst
		(cons (car lst) (no-repeats (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst))))))
