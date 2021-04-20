from staff import staff
from sql import sql1
class Main:
    def __init__(self):

        pass

    def selection(self):

        print('Function:')
        print('1=Display all employee records       2=Add new employee        3=Delete employee')
        print('4=Update employee payroll records      5=print monthly payslip   6= Quit program')
        question = input("What you want to do: ")
        while question.isdigit() ==False or question < '1' or question > '6':
            print("Invalid input")
            question = input("What you want to do: ")
        if question == '1':
            self.display_employee_records()
        elif question == '2':
            self.add_new_employee()
        elif question == '3':
            self.delete_employee()
        elif question == '4':
            self.update_payroll_detail()
    def display_employee_records(self):
        DB = sql1()
        final_id_list = []
        final_name_list = []
        final_department_list = []
        final_designation_list = []
        final_basic_pay_list = []
        final_working_hrs_list = []
        final_overtime_hrs_list = []
        final_allowance_list = []
        final_CPF_list = []
        final_net_pay_list = []
        final_leave_list = []
        full_staff_list = DB.fetchall('SELECT * FROM staff')
        full_salary_list = DB.fetchall('SELECT * FROM salary')
        for employee in full_staff_list:
            final_id_list.append(employee[0])
            final_name_list.append(employee[1])
            final_department_list.append(employee[2])
            final_designation_list.append(employee[3])
        for salary in full_salary_list:
            final_basic_pay_list.append(salary[1])
            final_working_hrs_list.append(salary[2])
            final_overtime_hrs_list.append(salary[3])
            final_allowance_list.append(salary[4])
            final_CPF_list.append(salary[5])
            final_net_pay_list.append(salary[6])
            final_leave_list.append(salary[7])
        print('{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format('Employee ID', 'Employee Name', "Department", "Designation","Basic pay","Wokring hrs","Overtime hrs","Allowance","Leave","CPF","Net pay"))
        for i in range(len(final_id_list)):
            print('{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format(final_id_list[i],final_name_list[i],final_department_list[i],final_designation_list[i],final_basic_pay_list[i],
                  final_working_hrs_list[i],final_overtime_hrs_list[1],final_allowance_list[i],final_leave_list[i],final_CPF_list[i],final_net_pay_list[i]))
        DB.close()
    def add_new_employee(self):
        DB = sql1()
        ID = input("Please enter employee ID:")
        # name = input("Please enter employee name:")
        # Dep  = input("Please enter employee department")
        # Des  = input("Please enter employee designation:")
        while ID.isdigit() == False:
            print("Please enter employee ID as number!")
            ID = input("Please enter employee ID:")
        name = input("Please enter employee name:")
        Department = input("Please enter employee department:")
        Designation = input("Please enter employee designation:")
        Basic = input("How much basic pay:")
        while Basic.isdigit() == False:
            print("Please enter Basic as number!")
            Basic = input("Please enter basic pay:")
        Insert_data = '''INSERT INTO staff VALUES({},'{}','{}','{}');'''.format(ID, name, Department, Designation)
        Insert_salary = '''INSERT INTO salary VALUES({},{},{},{},{},{},{},{});'''.format(ID, Basic, 0, 0, 0, 0, 0, 0)
        DB.execute(Insert_data)
        DB.execute(Insert_salary)
        DB.close()
        # Work = input("Does this worker work in this month(y/n)?")
        # while Work != 'Y' and Work != 'y' and Work != 'N' and Work != "n":
        #     print("Please enter Yes(y) or No(n)!")
        #     Work =input("Does this worker work this month(y/n)?")
        # if Work == 'y' or Work == 'y':
        #     Working_hrs = input("Please enter working hours:")
        #     while Working_hrs.isdigit() == False:
        #         print("Please enter working hours as number!")
        #         Working_hrs = input("Please enter working hours:")
        #     Overtime_hrs = input("Please enter overtime hours:")
        #     while Overtime_hrs.isdigit() == False:
        #         print("Please enter overtime hours as number!")
        #         Overtime_hrs = input("Please enter overtime hours:")
        #     Allowance = input("Please enter allowance:")
        #     while Allowance.isdigit() == False:
        #         print("Please enter allowance as number!")
        #         Allowance = input("Please enter allowance:")
        #     Leave = input("Please enter leave days:")
        #     while Leave.isdigit() == False:
        #         print("Please enter leave days as number!")
        #         Leave = input("Please enter leave days:")
    def delete_employee(self):
        DB = sql1()
        full_list = DB.fetchall('SELECT * FROM staff')
        print("Employee List:")
        print('{:<20}{:<20}{:<20}{:<20}'.format('Employee ID', 'Employee Name', "Department", "Designation"))
        for employee in full_list:
            print('{:<20}{:<20}{:<20}{:<20}'.format(employee[0], employee[1], employee[2], employee[3]))
        print("Which employee you want to delete?")
        question = input("Please enter employee id:")
        while question.isdigit() == False:
            question = input("Please enter employee id as number:")
        validation = DB.fetchall("SELECT Employee_ID FROM staff WHERE Employee_ID='{}'".format(question))
        if not validation:
            print("The employee id you entered is not exist in database!")
        else:
             delete_staff = 'DELETE FROM staff WHERE Employee_ID={} '.format(question)
             delete_salary = 'DELETE FROM salary WHERE Employee_ID={} '.format(question)
             DB.execute(delete_salary)
             DB.execute(delete_staff)
             DB.close()
             print("The employee has been removed from the database!")
        self.selection()
    def update_payroll_detail(self):
        loop = True
        while loop:
            self.display_employee_records()
            DB =sql1()
            print("Which employee payroll detail you want to update")
            question = input("Please enter employee id:")
            while question.isdigit() == False:
                question = input("Please enter employee id as number:")
            validation = DB.fetchall("SELECT Employee_ID FROM staff WHERE Employee_ID='{}'".format(question))
            if not validation:
                print("The employee id you entered is not exist in database!")
            else:
                Database_basic_pay = DB.fetchone('SELECT Basic_pay FROM salary where Employee_ID = {}'.format(question))
                Basic_pay =  Database_basic_pay[0]
                Working_hrs = input("How many hours this employee worked on this month:")
                while Working_hrs.isdigit() == False:
                    print("Please enter working hours as number!")
                    Working_hrs = input("How many hours this employee worked on this month:")
                if float(Working_hrs) < 160:
                    Overtime_hrs = 0
                    Overtime_pay = 0
                else:
                    Overtime_hrs = float(Working_hrs) - 160
                    Overtime_pay = ((Basic_pay/160)*1.5)*Overtime_hrs
                Allowance = input("Please enter amount of allowance:")
                while Allowance.isdigit() == False:
                    print("Please enter allowance amount as number!")
                    Allowance = input("Please enter amount of allowance:")
                Leave = input("Does this employee has unpaid leave(y/n):")
                while Leave != 'y' and Leave != 'Y' and Leave != 'N' and Leave != 'n':
                    print("Please enter yes(y) or no(n)!")
                    Leave = input("Does this employee has unpaid leave(y/n):")
                if Leave == 'y' or Leave == 'y':
                    day = input("How many day of unpaid leave:")
                    while day.isdigit() == False:
                        print("Please enter unpaid leave as number!")
                        day = input("How many day of unpaid leave:")
                    deduct_unpaid = (float(Basic_pay) / 20)* int(day)
                elif Leave == 'N' or Leave == 'n':
                    deduct_unpaid = 0
                    day = 0
                CPF = (float(Basic_pay) + float(Overtime_pay) - float(deduct_unpaid)) * 0.15
                Net_pay = float(Basic_pay)+float(Overtime_pay)+float(Allowance)-float(deduct_unpaid)-float(CPF)
                Insert = '''UPDATE salary SET Working_hrs = {},Overtime_hours ={},Allowance = {},CPF = {},Net_pay = {},Leave = {} WHERE Employee_ID = {}; '''.format(Working_hrs,Overtime_hrs,Allowance,CPF,Net_pay,day,question)
                DB.execute(Insert)
                print(Insert)
                print("Update successfully!")
                DB.close()
            loop_question = input("Do you want to continue update payroll detail(y/n)?")
            while loop_question != 'Y' and loop_question !='y' and loop_question != 'N' and loop_question != 'n':
                print("Please enter yes(y) or no(n)!")
                loop_question = input("Do you want to continue update payroll detail(y/n)?")
            if loop_question == 'y' or loop_question == 'Y':
                loop = True
            else:
                loop = False
                self.selection()



start=Main()
start.selection()