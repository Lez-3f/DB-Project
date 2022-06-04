-- DROP TRIGGER rsv_rm_user;
CREATE TRIGGER rsv_rm_user
AFTER DELETE ON user
FOR EACH ROW
UPDATE reservation SET rstate=999 
WHERE rguest = OLD.uno;

-- DROP TRIGGER rt_rm_user;
CREATE TRIGGER rt_rm_user
AFTER DELETE ON user
FOR EACH ROW
UPDATE rental SET rtstate=999 
WHERE rtguest = OLD.uno;

-- 禁用场地
CREATE TRIGGER rsv_fb_court
AFTER UPDATE ON court 
FOR EACH ROW
UPDATE reservation SET rstate=3 
WHERE rcourt=NEW.cno AND NEW.cstate=2
