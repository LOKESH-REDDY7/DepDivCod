# Write your MySQL query statement below
delete p from Person p JOIN Person q ON p.email = q.email and p.id > q.id;
