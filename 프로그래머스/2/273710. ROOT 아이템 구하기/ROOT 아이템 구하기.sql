-- 코드를 작성해주세요
SELECT b.ITEM_ID , a.ITEM_NAME
FROM ITEM_INFO as a
inner join ITEM_TREE as b
on a.ITEM_ID = b.ITEM_ID
WHERE b.PARENT_ITEM_ID is null