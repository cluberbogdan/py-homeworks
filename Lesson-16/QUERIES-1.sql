CREATE TABLE "users" (
  "user_id" int PRIMARY KEY,
  "username" varchar,
  "email" varchar,
  "password_hash" varchar,
  "user_type" varchar
);

CREATE TABLE "rooms" (
  "room_id" int PRIMARY KEY,
  "host_id" int,
  "room_name" varchar,
  "max_residents" int,
  "price_per_night" decimal,
  "has_ac" boolean,
  "has_refrigerator" boolean
);

CREATE TABLE "reservations" (
  "reservation_id" int PRIMARY KEY,
  "guest_id" int,
  "room_id" int,
  "max_residence" int,
  "check_in_date" date,
  "check_out_date" date
);

CREATE TABLE "reviews" (
  "review_id" int PRIMARY KEY,
  "reservation_id" int,
  "rating" int,
  "review_text" text,
  "review_date" date
);

CREATE TABLE "payment" (
  "transaction_id" int PRIMARY KEY,
  "payment_date" date,
  "total_price" decimal,
  "payment_status" varchar,
  "reservation_id" int
);

CREATE TABLE "hostReviews" (
  "host_review_id" int PRIMARY KEY,
  "reservation_id" int,
  "guest_id" int,
  "host_id" int,
  "rating" int,
  "review_text" text,
  "review_date" date
);

ALTER TABLE "rooms" ADD FOREIGN KEY ("host_id") REFERENCES "users" ("user_id");

ALTER TABLE "reservations" ADD FOREIGN KEY ("guest_id") REFERENCES "users" ("user_id");

ALTER TABLE "reservations" ADD FOREIGN KEY ("room_id") REFERENCES "rooms" ("room_id");

ALTER TABLE "payment" ADD FOREIGN KEY ("reservation_id") REFERENCES "reservations" ("reservation_id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("reservation_id") REFERENCES "reservations" ("reservation_id");

ALTER TABLE "hostReviews" ADD FOREIGN KEY ("reservation_id") REFERENCES "reservations" ("reservation_id");
