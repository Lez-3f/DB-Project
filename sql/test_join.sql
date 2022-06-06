select * from court INNER JOIN reservation ON reservation.rcourt = court.cno        
WHERE reservation.rstate = 1 GROUP BY cno;