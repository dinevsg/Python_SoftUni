SELECT
	o.name AS owner,
	COUNT(owner_id) AS count_of_animals
	

FROM animals AS a
JOIN owners AS o
ON o.id = a.owner_id
GROUP BY o.name
ORDER BY
	count_of_animals DESC,
	owner ASC
LIMIT 5

