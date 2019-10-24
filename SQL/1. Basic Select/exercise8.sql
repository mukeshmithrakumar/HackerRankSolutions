-- Weather Observation Station 3 "https://www.hackerrank.com/challenges/weather-observation-station-3/problem"

select distinct city from STATION
    where MOD(id,2)=0;
