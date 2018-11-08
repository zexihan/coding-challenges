/* Write your T-SQL query statement below */
WITH 
helper AS (
SELECT d.Name Department,
       e.Name Employee,
       e.Salary Salary,
       DENSE_RANK() OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC) AS Rank  
  FROM Employee e
  JOIN Department d
    ON e.DepartmentId = d.Id
)
SELECT Department,
       Employee,
       Salary
  FROM helper
 WHERE Rank IN (1,2,3)