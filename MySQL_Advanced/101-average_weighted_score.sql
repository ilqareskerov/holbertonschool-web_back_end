-- This is a line of text
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE sum_average FLOAT;
	SET
sum_average = (SELECT (SUM(score * weight)/SUM(weight))
	FROM corrections INNER JOIN projects ON project_id = id WHERE corrections.user_id=user_id);
UPDATE users SET average_score=sum_average WHERE id=user_id;
END $$
DELIMITER ;
