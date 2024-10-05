SELECT FROM students
SELECT * FROM students WHERE age > 18
SELECT * FROM students WHERE name = "Smith" AND average_score > 7
SELECT students.name, COUNT(students.average_score) 
FROM students
WHERE students.average_score > 8