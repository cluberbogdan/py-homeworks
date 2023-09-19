SELECT "username", "user_id"
FROM "users"
WHERE "user_id" = (
  SELECT "host_id"
  FROM "rooms"
  WHERE "room_id" IN (
    SELECT "room_id"
    FROM "reservations"
    WHERE "reservation_id" IN (
      SELECT "reservation_id"
      FROM "hostReviews"
      GROUP BY "reservation_id"
      ORDER BY AVG("rating") DESC
      LIMIT 1
    )
  )
);
