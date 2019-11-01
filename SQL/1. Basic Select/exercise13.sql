-- Weather Observation Station 8 "https://www.hackerrank.com/challenges/weather-observation-station-8/problem"


select distinct city from station
where (substr(lower(city), 1, 1) in ('a','e','i','o','u')
    and
    substr(lower(city), length(city), 1) in ('a','e','i','o','u'));
