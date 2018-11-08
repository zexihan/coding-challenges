# Write your MySQL query statement below
SELECT Id
  FROM Weather
  JOIN (
      SELECT DATE_ADD(RecordDate, INTERVAL +1 DAY) FormerDate,
             Temperature
        FROM Weather
  ) former_day
    ON former_day.FormerDate = Weather.RecordDate
 WHERE former_day.Temperature < Weather.Temperature;
