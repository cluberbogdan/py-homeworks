SELECT u.username, u.user_id
FROM users u
JOIN (
    SELECT guest_id, COUNT(*) AS num_reservations
    FROM reservations
    GROUP BY guest_id
) r ON u.user_id = r.guest_id
ORDER BY num_reservations DESC
LIMIT 1;
