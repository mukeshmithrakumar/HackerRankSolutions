-- Weather Observation Station 7 "https://www.hackerrank.com/challenges/weather-observation-station-7/problem"


select distinct city from station where substr(lower(city), length(city), 1) in ('a','e','i','o','u');
