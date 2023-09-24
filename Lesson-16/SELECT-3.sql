SELECT u.username, u.user_id
FROM users u
JOIN rooms r ON u.user_id = r.host_id
JOIN reservations res ON r.room_id = res.room_id
WHERE res.reservation_id IN (
    SELECT hr.reservation_id
    FROM hostReviews hr
    GROUP BY hr.reservation_id
    ORDER BY AVG(hr.rating) DESC
    LIMIT 1
);

