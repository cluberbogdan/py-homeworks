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
  `check_out_date` date
);

CREATE TABLE `reviews` (
  `review_id` int PRIMARY KEY,
  `reservation_id` int,
  `rating` int,
  `review_text` text,
  `review_date` date
);

CREATE TABLE `payment` (
  `transaction_id` int PRIMARY KEY,
  `guest_id` int,
  `room_id` int,
  `payment_date` date,
  `total_price` decimal,
  `payment_status` varchar(255),
  `reservation_id` int
);

CREATE TABLE `hostReviews` (
  `host_review_id` int PRIMARY KEY,
  `guest_id` int,
  `host_id` int,
  `review_text` text,
  `review_date` date
);

ALTER TABLE `users` ADD FOREIGN KEY (`user_id`) REFERENCES `rooms` (`host_id`);

CREATE TABLE `reservations_users` (
  `reservations_guest_id` int,
  `users_user_id` int,
  PRIMARY KEY (`reservations_guest_id`, `users_user_id`)
);

ALTER TABLE `reservations_users` ADD FOREIGN KEY (`reservations_guest_id`) REFERENCES `reservations` (`guest_id`);

ALTER TABLE `reservations_users` ADD FOREIGN KEY (`users_user_id`) REFERENCES `users` (`user_id`);


ALTER TABLE `reservations` ADD FOREIGN KEY (`reservation_id`) REFERENCES `payment` (`reservation_id`);

ALTER TABLE `reservations` ADD FOREIGN KEY (`reservation_id`) REFERENCES `reviews` (`reservation_id`);

ALTER TABLE `reservations` ADD FOREIGN KEY (`guest_id`) REFERENCES `hostReviews` (`guest_id`);
