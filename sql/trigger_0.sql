DROP TRIGGER IF EXISTS rsv_rm_user;
CREATE TRIGGER rsv_rm_user
AFTER DELETE ON user
FOR EACH ROW
UPDATE reservation SET rstate=999 
WHERE rguest = OLD.uno;

DROP TRIGGER IF EXISTS rt_rm_user;
CREATE TRIGGER rt_rm_user
AFTER DELETE ON user
FOR EACH ROW
UPDATE rental SET rtstate=999 
WHERE rtguest = OLD.uno;

-- forbit court
DROP TRIGGER IF EXISTS rsv_fb_court;
CREATE TRIGGER rsv_fb_court
AFTER UPDATE ON court 
FOR EACH ROW
UPDATE reservation SET rstate=3 
WHERE rcourt=NEW.cno AND NEW.cstate=2;

DROP TRIGGER IF EXISTS eq_num_a_incre;
CREATE TRIGGER eq_num_a_incre
BEFORE INSERT ON equipment
FOR EACH ROW SET NEW.enum_a = NEW.enum_t;
