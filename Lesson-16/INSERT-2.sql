INSERT INTO "users" ("username", "email", "password_hash", "user_type")
VALUES ('user1', 'user1@example.com', 'hashed_password1', 'guest'),
       ('user2', 'user2@example.com', 'hashed_password2', 'host'),
       ('user3', 'user3@example.com', 'hashed_password3', 'guest'),
       ('user4', 'user3@example.com', 'hashed_password4', 'guest'),
       ('user5', 'user3@example.com', 'hashed_password5', 'host'),
       ('user6', 'user3@example.com', 'hashed_password6', 'guest');

INSERT INTO "rooms" ("host_id", "room_name", "max_residents", "price_per_night", "has_ac", "has_refrigerator")
VALUES (2, 'Room 101', 2, 70.0, TRUE, TRUE),
       (2, 'Room 102', 3, 60.0, TRUE, FALSE),
       (5, 'Room 103', 2, 50.0, FALSE, TRUE),
       (5, 'Room 104', 2, 60.0, FALSE, TRUE);

INSERT INTO "reservations" ("guest_id", "room_id", "max_residence", "check_in_date", "check_out_date")
VALUES (1, 1, 2, '2023-09-01', '2023-09-04'),
       (3, 2, 3, '2023-09-10', '2023-09-15'),
       (1, 3, 2, '2023-09-17', '2023-09-20');
       (4, 4, 2, '2023-09-04', '2023-09-08'),
       (6, 2, 3, '2023-09-10', '2023-09-13'),

INSERT INTO "reviews" ("reservation_id", "rating", "review_text", "review_date")
VALUES (1, 5, 'Great experience!', '2023-09-06'),
       (2, 4, 'Nice room, good service.', '2023-09-16'),
       (3, 3, 'Average stay.', '2023-09-26');

INSERT INTO "payment" ("payment_date", "total_price", "payment_status", "reservation_id")
VALUES ('2023-09-10', 350.0, 'success', 1),
       ('2023-09-10', 300.0, 'success', 2),
       ('2023-09-20', 150.0, 'success', 3);
       ('2023-09-04', 240.0, 'success', 4),
       ('2023-09-10', 280.0, 'success', 5),

INSERT INTO "hostReviews" ("reservation_id", "guest_id", "host_id", "review_text", "review_date", "rating")
VALUES (1, 1, 2, 'Good host!', '2023-09-07', 5),
       (2, 3, 2, 'Host could improve.', '2023-09-17', 3),
       (3, 1, 2, 'Nice host!', '2023-09-27', 4);
       (4, 4, 5, 'Good host!', '2023-09-27', 4),
       (5, 6, 5, 'Host could improve.', '2023-09-27', 4),