# Write your MySQL query statement below
SELECT
    Employee.name
FROM
    Employee
INNER JOIN
    (SELECT 
        managerId, 
        COUNT(managerId) as report_count 
     FROM 
        Employee 
     GROUP BY 
        managerId
     HAVING
        report_count >= 5
    ) as count_emp
ON
    count_emp.managerId = Employee.id;