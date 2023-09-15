CREATE TABLE `users` (
  `user_id` int PRIMARY KEY,
  `username` varchar(255),
  `email` varchar(255),
  `password_hash` varchar(255),
  `user_type` varchar(255)
);

CREATE TABLE `rooms` (
  `room_id` int PRIMARY KEY,
  `host_id` int,
  `room_name` varchar(255),
  `max_residents` int,
  `price_per_night` decimal,
  `has_ac` boolean,
  `has_refrigerator` boolean
);

CREATE TABLE `reservations` (
  `reservation_id` int PRIMARY KEY,
  `guest_id` int,
  `room_id` int,
  `max_residence` int,
  `check_in_date` date,
  `check_out_date` date,
  `total_price` decimal
);

CREATE TABLE `reviews` (
  `review_id` int PRIMARY KEY,
  `reservation_id` int,
  `rating` int,
  `review_text` text,
  `review_date` date,
  `total_price` decimal
);

CREATE TABLE `paymentTransactions` (
  `transaction_id` int PRIMARY KEY,
  `guest_id` int,
  `room_id` int,
  `payment_date` date,
  `total_price` decimal,
  `payment_status` varchar(255)
);

CREATE TABLE `hostReviews` (
  `host_review_id` int PRIMARY KEY,
  `guest_id` int,
  `host_id` int,
  `review_text` text,
  `review_date` date
);

ALTER TABLE `users` ADD FOREIGN KEY (`user_id`) REFERENCES `rooms` (`host_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`user_id`) REFERENCES `reservations` (`guest_id`);

ALTER TABLE `rooms` ADD FOREIGN KEY (`room_id`) REFERENCES `reservations` (`room_id`);

ALTER TABLE `reservations` ADD FOREIGN KEY (`reservation_id`) REFERENCES `reviews` (`reservation_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`user_id`) REFERENCES `hostReviews` (`guest_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`user_id`) REFERENCES `paymentTransactions` (`guest_id`);

ALTER TABLE `rooms` ADD FOREIGN KEY (`room_id`) REFERENCES `paymentTransactions` (`room_id`);
