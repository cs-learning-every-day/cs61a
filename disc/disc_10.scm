
(define (replicate x n)
    (if (= 0 n)
        nil
        (cons x (replicate x (- n 1)))))

(define (my-append a b)
    (if (null? a)
        b
        (cons (car a) (my-append (cdr a) b))))

(define (uncompress s)
    (if (null? s)
        nil
        (my-append (replicate (car (car s)) 
                              (car (cdr (car s))))
                   (uncompress (cdr s)))))

(define (map fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst))
              (map fn (cdr lst)))))

(define (make-tree label branches) (cons label branches))
(define (label tree)
    (car tree))
(define (branches tree)
    (cdr tree))

(define (tree-sum tree)
    (cond ((null? (branches tree))
            (label tree))
          (else (+ (label tree) (tree-sum (branches tree))))))

(define (factors n)
    (define (factors-helper i n)
        (if (= i n)
            nil
            (if (= (modulo n i) 0)
                (cons i (factors-helper (+ i 1) n))
                (factors-helper (+ i 1) n))))
    (factors-helper 1 n))

(define (square x)
    (* x x))
(define (deep-squares lol)
    (cond ((null? lol) '())
            ((list? (car lol))
                (cons (deep-squares (car lol))
                    (deep-squares (cdr lol))))
            (else (cons (square (car lol))
                    (deep-squares (cdr lol))))))