-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find the crime scene report for the duck theft on Humphrey Street on July 28, 2024
SELECT description FROM crime_scene_reports
WHERE street = 'Humphrey Street' AND day = 28 AND month = 7 AND year = 2024;

-- Check bakery security logs on July 28, 2024 around the time of the theft (assume ~10 AM)
-- Look for cars exiting shortly after the theft (e.g., between 10:15 and 10:25)
SELECT license_plate, activity, hour, minute
FROM bakery_security_logs
WHERE day = 28 AND month = 7 AND year = 2024
  AND hour = 10 AND minute >= 15 AND minute <= 25
  AND activity = 'exit';

-- Get names of people whose cars exited during that window
SELECT name FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE day = 28 AND month = 7 AND year = 2024
      AND hour = 10 AND minute BETWEEN 15 AND 25
      AND activity = 'exit'
);

-- Cross-reference with ATM withdrawals on Humphrey Street on same day
SELECT people.name
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.atm_location = 'Humphrey Street'
  AND atm_transactions.transaction_type = 'withdraw'
  AND atm_transactions.day = 28 AND atm_transactions.month = 7 AND atm_transactions.year = 2024;

-- Find people who BOTH exited bakery AND withdrew money
SELECT name FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE day = 28 AND month = 7 AND year = 2024
      AND hour = 10 AND minute BETWEEN 15 AND 25
      AND activity = 'exit'
)
AND id IN (
    SELECT person_id FROM bank_accounts
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
    WHERE atm_location = 'Humphrey Street'
      AND transaction_type = 'withdraw'
      AND day = 28 AND month = 7 AND year = 2024
);

-- Now check phone calls made by these suspects on July 28, 2024 (short calls likely to accomplice)
SELECT caller, receiver, duration
FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2024
  AND caller IN (
      SELECT phone_number FROM people WHERE name IN ('Bruce', 'Diana', 'Others from above')
  )
ORDER BY duration ASC;

-- Identify accomplice by receiver phone number
SELECT name FROM people WHERE phone_number = '(receiver from above)';

-- Find flights out of Fiftyville on July 28, 2024 after the theft (e.g., after 10:30 AM)
SELECT flights.id, airports.city, flights.hour, flights.minute
FROM flights
JOIN airports ON flights.destination_airport_id = airports.id
WHERE flights.origin_airport_id = (
    SELECT id FROM airports WHERE city = 'Fiftyville'
)
AND flights.day = 28 AND flights.month = 7 AND flights.year = 2024
AND (flights.hour > 10 OR (flights.hour = 10 AND flights.minute > 30))
ORDER BY flights.hour, flights.minute;

-- Get passport numbers of passengers on earliest flight
SELECT passport_number FROM passengers
WHERE flight_id = (earliest flight id from above);

-- Match thief's passport to passenger list
SELECT name FROM people
WHERE passport_number IN (
    SELECT passport_number FROM passengers WHERE flight_id = 36
)
AND name = 'Bruce';  -- or from suspect list

-- Confirm accomplice is the person Bruce called
-- (short call, likely < 60 seconds)
