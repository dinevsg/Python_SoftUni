SELECT
	v.name AS volunteers,
	v.phone_number AS phone_number,
	TRIM(v.address, '%Sofia ,%') AS address
    ----- OR ----
     SUBSTRING(TRIM(REPLACE(v.address, 'Sofia', '')), 3) AS address
	

FROM volunteers AS v
JOIN volunteers_departments AS vd
ON v.department_id = vd.id
WHERE vd.department_name = 'Education program assistant'
AND v.address LIKE '%Sofia%'
ORDER BY
	v.name ASC;