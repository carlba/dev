CREATE TABLE person
 (person_id SMALLINT UNSIGNED,
  fname VARCHAR(20),
  lname VARCHAR(20),
  gender ENUM('M','F'),
  birth_date DATE,
  street VARCHAR(30),
  city VARCHAR(20),
  state VARCHAR(20),
  country VARCHAR(20),
  postal_code VARCHAR(20),
  CONSTRAINT pk_person PRIMARY KEY (person_id)
 );
 
 
CREATE TABLE favorite_food
 (person_id SMALLINT UNSIGNED,
  food VARCHAR(20),
  CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
  CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id)
    REFERENCES person (person_id)
  );

INSERT INTO person (person_id, fname, lname, gender, birth_date) VALUES (null,'William', 'Turner', 'M', '1972-05-27');

INSERT INTO favorite_food (person_id, food) VALUES (1,'pizza');
insert into favorite_food (person_id, food) VALUES (1,'cookies');
insert into favorite_food (person_id, food) VALUES (1,'nachos');

INSERT INTO person (person_id, fname, lname, gender, birth_date, street, city, state, country, postal_code) Values (null, 'Susan','Smith','F','1975-11-02', '23 Maple St.', 'Arlington', 'VA', 'USA', 20220);

--- Update (Specify a range in the WHERE clause to update several rows.
UPDATE person SET street = '1225 Tremont St.', city = 'Boston', state = 'NA', country = 'USA', postal_code = '02138' WHERE person_id = 1;

--- Delete susan
DELETE FROM person WHERE person_id =2;

--- We can select any number of columns with the select statement and modify them with i.e inbuilt functions like upper
select LOWER(UPPER(LOWER(city))) from customer;
--- Shows db-version, current user, and currently selected db
SELECT VERSION(), USER(), DATABASE();
--- Show only unique matches
SELECT DISTINCT cust_id from account;
--- Be careful with using distinct since it requires the data to be sorted which can be timeconsuming
--- Show Firstname, lastname and department name. This gets the department name from the department table based on dept_id.
SELECT e.emp_id, e.fname, e.lname, d.name dept_name FROM employee AS e INNER JOIN department AS d ON e.dept_id = d.dept_id;
--- Query with multiple nested where clauses.
SELECT emp_id, fname, lname, start_date, title FROM employee WHERE (title = 'Head Teller' AND start_date > '2003-01-01') OR (title = 'Teller' and start_date > '2003-01-01');
--- Count number of employes for each department
SELECT d.name, count(e.emp_id) num_employees FROM department d INNER JOIN employee e   ON d.dept_id = e.dept_id GROUP BY d.name HAVING count(e.emp_id) > 2;
--- Show all employes that has openend an account.
SELECT DISTINCT open_emp_id FROM account;
--- Show all employes that has openend an account with name instead of id.
SELECT DISTINCT e.fname, e.lname, a.cust_id FROM account a INNER JOIN employee e on a.open_emp_id = e.emp_id;
