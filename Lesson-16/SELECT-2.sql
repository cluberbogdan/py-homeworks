SELECT
    u.user_id AS host_id,
    u.username AS host_name,
    SUM(p.total_price) AS total_earnings
FROM
    users u
JOIN
    rooms r ON u.user_id = r.host_id
JOIN
    reservations res ON r.room_id = res.room_id
JOIN
    payment p ON res.reservation_id = p.reservation_id
GROUP BY
    u.user_id, u.username
ORDER BY
    total_earnings DESC
LIMIT 1;

