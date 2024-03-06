SELECT 
	c.id AS car_id,
	c.make AS make,
	c.mileage AS mileage,
	COUNT(co.id) AS count_of_courses,
	ROUND(AVG(co.bill), 2) AS average_bill
FROM 
	cars AS c
LEFT JOIN 
	courses AS co
ON 
	co.car_id = c.id
GROUP BY 
	c.id
HAVING
	COUNT(co.id) <> 2
ORDER BY
	count_of_courses DESC,
	c.id ASC;
