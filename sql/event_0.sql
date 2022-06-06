DROP EVENT IF EXISTS rsv_unvalid;
CREATE EVENT IF NOT EXISTS rsv_unvalid 
ON SCHEDULE EVERY 1 MINUTE STARTS '2022-06-06 10:36:00'
ON COMPLETION PRESERVE ENABLE
DO UPDATE reservation
SET rstate=999 WHERE DATEDIFF(rbegin, NOW()) < 0;
-- ALTER EVENT rsv_unvalid ON reservation PRESERVE ENABLE;