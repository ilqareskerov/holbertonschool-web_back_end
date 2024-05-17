-- This is a line of text
DELIMITER $$
CREATE TRIGGER is_email_valid BEFORE UPDATE ON users
    FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
END IF;
END$$
DELIMITER ;