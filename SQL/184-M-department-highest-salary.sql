# Write your MySQL query statement below
SELECT d.Name Department,
       e.Name Employee,
       agg.Salary Salary
  FROM (
    SELECT e.DepartmentId DepartmentId,
           MAX(e.Salary) Salary
      FROM Employee e
     GROUP BY
         e.DepartmentId
   ) agg
 JOIN Employee e
   ON agg.Salary = e.Salary AND
      agg.DepartmentId = e.DepartmentId
 JOIN Department d
   ON d.Id = agg.DepartmentId;