SELECT
	a.name,
	CASE
		WHEN EXTRACT (HOUR FROM c.start) BETWEEN 6 AND 20 THEN 'Day'
		ELSE 'Night'
	END AS day_time,
	c.bill,
	cl.full_name,
	cr.make,
	cr.model,
	cat.name AS category_name
FROM
	courses AS c
JOIN
	clients AS cl
ON 
	cl.id = c.client_id
JOIN
	cars AS cr
ON 
	cr.id = c.car_id
JOIN 
	categories AS cat
ON 
	cat.id = cr.category_id
JOIN
	addresses AS a
ON
	a.id = c.from_address_id
ORDER BY
	c.id;

