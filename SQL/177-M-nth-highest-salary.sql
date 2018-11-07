CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      Select DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT N, 1
  );
END