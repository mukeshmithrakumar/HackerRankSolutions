-- Weather Observation Station 6 "https://www.hackerrank.com/challenges/weather-observation-station-6/problem"


select city from station where substr(city, 1, 1) in ('A','E','I','O','U');
