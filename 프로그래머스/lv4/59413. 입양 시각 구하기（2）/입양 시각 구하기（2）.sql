-- 코드를 입력하세요

SET @HOUR = -1;
SELECT @HOUR := @HOUR + 1 AS HOUR, (select count(*)  from animal_outs where hour(datetime) = @hour) AS COUNT 
FROM ANIMAL_OUTS  
GROUP BY HOUR 
HAVING HOUR BETWEEN 0 AND 23;