-- 코드를 입력하세요
select animal_type, case when name is null then 'No name' else name end as name, sex_upon_intake
from animal_ins order by animal_id;