create table employees(
	employee_id serial primary key,
	first_name varchar(30) not null,
	last_name varchar(30) not null,
	title varchar(100) not null,
	birth_date date,	
	notes text
);

create table customers(
	customer_id varchar(10) primary key,
	company_name varchar(100) not null,
	contact_name varchar(100) not null
);

create table orders(
	order_id int primary key,
	customer_id varchar(10) references customers(customer_id),
	employee_id int references employees(employee_id),
	order_date date,
	ship_city varchar(20)
);