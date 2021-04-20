from sql import sql1
staff_db = sql1()

staff ='''CREATE TABLE staff(
     Employee_ID Integer Primary key,
     Employee_name Varchar(255) NOT NULL,
     Department Varchar(255) NOT NULL,
     Designation Varchar(255) NOT NULL
 );'''

salary = '''CREATE TABLE salary(
     Employee_ID Integer Primary key,
     Basic_pay Float NOT NULL,
     Working_hrs Float NOT NULL,
     Overtime_hours Float NOT NULL,
     Allowance Float NOT NULL,
     CPF Float NOT NULL,
     Net_pay Float NOT NULL,
     Leave Integer NOT NULL
 );'''



if staff_db is not None:
    staff_db.execute(staff)
    staff_db.execute(salary)



staff_db.close()

