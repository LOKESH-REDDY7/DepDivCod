select e.name as Employee from Employee e INNER JOin Employee m ON e.managerId = m.id where 
e.salary > m.salary;
