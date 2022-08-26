-- 코드를 입력하세요
SELECT A.animal_id, B.name from animal_outs A
left join animal_ins B
on A.animal_id = B.animal_id
where A.datetime < B.datetime
order by B.datetime ;