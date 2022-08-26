-- 코드를 입력하세요
SELECT A.animal_id, A.name from animal_ins A
left join animal_outs B
on A.animal_id = B.animal_id
where B.datetime is not null
order by TIMESTAMPDIFF(DAY, A.DATETIME, B.DATETIME) DESC
limit 2;