CREATE TABLE IF NOT EXISTS dssa.DATE as (SELECT DISTINCT rental_date as sk_date, Extract(QUARTER FROM rental_date) as quarter, Extract(year FROM rental_date) as year, Extract(month FROM rental_date) as month, Extract(day FROM rental_date) as day FROM RENTAL)