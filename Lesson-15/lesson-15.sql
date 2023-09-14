CREATE TABLE `users` (
  `user_id` integer PRIMARY KEY,
  `username` integer,
  `email` varchar(255),
  `password_hash` varchar(255),
  `user_type` varchar(255)
);

CREATE TABLE `rooms` (
  `room_id` integer PRIMARY KEY,
  `host_id` integer,
  `room_name` varchar(255),
  `max_residents` varchar(255),
  `price_per_night` integer,
  `has_ac` varchar(255),
  `has_refrigerator` varchar(255)
);

CREATE TABLE `reservations` (
  `reservation_id` integer PRIMARY KEY,
  `guest_id` varchar(255),
  `room_id` integer,
  `check_in_date` date,
  `check_out_date` date,
  `total_price` integer
);

CREATE TABLE `reviews` (
  `review_id` integer PRIMARY KEY,
  `guest_id` varchar(255),
  `room_id` integer,
  `rating` integer,
  `review_text` text,
  `review_date` date,
  `total_price` integer
);

ALTER TABLE `users` ADD FOREIGN KEY (`user_id`) REFERENCES `rooms` (`host_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`user_id`) REFERENCES `reservations` (`guest_id`);

ALTER TABLE `rooms` ADD FOREIGN KEY (`room_id`) REFERENCES `reviews` (`room_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`user_id`) REFERENCES `reviews` (`guest_id`);

ALTER TABLE `rooms` ADD FOREIGN KEY (`room_id`) REFERENCES `reservations` (`room_id`);
