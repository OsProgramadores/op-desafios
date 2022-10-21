#lang racket

(require math/bigfloat)

(define lines (file->lines "d12.txt" #:mode 'text))

(define (check n)
  (define nn (bf n))
  (cond
    [(bf= nn (bf 0)) (displayln "0 false")]
    [(bf= nn (bf 1)) (displayln "1 true 0")]
    [(bf= (bf 0) (bf- (bflog2 nn) (bftruncate (bflog2 nn))))
     (displayln (string-append n " true " (bigfloat->string (bftruncate (bflog2 nn)))))]
    [else (displayln (string-append n " false"))]))
  
(for ([i (in-list lines)])
  (check i))