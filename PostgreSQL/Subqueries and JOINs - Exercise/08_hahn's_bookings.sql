SELECT 
	COUNT(*)
FROM	
	bookings
JOIN
	customers AS C
USING	
	(customer_id)
WHERE
	c.last_name = 'Hahn'