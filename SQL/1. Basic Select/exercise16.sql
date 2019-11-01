-- Weather Observation Station 11 "https://www.hackerrank.com/challenges/weather-observation-station-11/problem"


select distinct city from station
where (substr(lower(city), 1, 1) not in ('a','e','i','o','u')
    or
    substr(lower(city), length(city), 1) not in ('a','e','i','o','u'));
