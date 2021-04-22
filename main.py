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
        elif question == '5':
            self.print_monthly_payslip()
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
                  final_working_hrs_list[i],final_overtime_hrs_list[i],final_allowance_list[i],final_leave_list[i],final_CPF_list[i],final_net_pay_list[i]))
        DB.close()
        self.selection()

    def display_all_employee_records(self):
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
                  final_working_hrs_list[i],final_overtime_hrs_list[i],final_allowance_list[i],final_leave_list[i],final_CPF_list[i],final_net_pay_list[i]))
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
        self.selection()
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
            confirmation = input("Are you sure u want to delete this employee from database? (y/n): ")
            while confirmation != 'y' and confirmation != 'Y' and confirmation != 'N' and confirmation != 'n':
                print("Please enter yes(y) or no(n)!")
                confirmation = input("Are you sure u want to delete this employee from database? (y/n): ")
            if confirmation =='Y' or confirmation =='y':
                delete_staff = 'DELETE FROM staff WHERE Employee_ID={} '.format(question)
                delete_salary = 'DELETE FROM salary WHERE Employee_ID={} '.format(question)
                DB.execute(delete_salary)
                DB.execute(delete_staff)
                DB.close()
                print("The employee has been removed from the database!")
            elif confirmation =='N' or confirmation =='n':
                reselect = input("Do you still want to delete any employee from the database? (y/n): ")
                while reselect != 'y' and reselect != 'Y' and reselect != 'N' and reselect != 'n':
                    print("Please enter yes(y) or no(n)!")
                    reselect = input("Do you still want to delete any employee from the database? (y/n): ")
                if reselect == 'Y' or reselect == 'y':
                    self.delete_employee()
                elif reselect =='N' or reselect =='n':
                    pass
        self.selection()
    def update_payroll_detail(self):
        loop = True
        while loop:
            self.display_all_employee_records()
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
                    Overtime_pay_float = '{0:.2f}'.format(Overtime_pay)

                Allowance = input("Please enter amount of allowance:")
                while Allowance.isdigit() == False:
                    print("Please enter allowance amount as number!")
                    Allowance = input("Please enter amount of allowance:")
                Leave = input("Does this employee has unpaid leave(y/n):")
                while Leave != 'y' and Leave != 'Y' and Leave != 'N' and Leave != 'n':
                    print("Please enter yes(y) or no(n)!")
                    Leave = input("Does this employee has unpaid leave(y/n):")
                if Leave == 'y' or Leave == 'Y':
                    day = input("How many day of unpaid leave:")
                    while day.isdigit() == False:
                        print("Please enter unpaid leave as number!")
                        day = input("How many day of unpaid leave:")
                    deduct_unpaid = (float(Basic_pay) / 20)* int(day)
                    deduct_unpaid_float = '{0:.2f}'.format(deduct_unpaid)
                elif Leave == 'N' or Leave == 'n':
                    deduct_unpaid_float = '0'
                    day = 0
                CPF = (float(Basic_pay) + float(Overtime_pay_float) - float(deduct_unpaid_float)) * 0.15
                CPF_float = '{0:.2f}'.format(CPF)

                Net_pay = float(Basic_pay)+float(Overtime_pay_float)+float(Allowance)-float(deduct_unpaid_float)-float(CPF_float)
                Net_pay_float = '{0:.2f}'.format(Net_pay)
                Insert = '''UPDATE salary SET Working_hrs = {},Overtime_hours ={},Allowance = {},CPF = {},Net_pay = {},Leave = {} WHERE Employee_ID = {}; '''.format(Working_hrs,Overtime_hrs,Allowance,CPF_float,Net_pay_float,day,question)
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

    def print_monthly_payslip(self):
        self.display_all_employee_records()
        DB = sql1()
        print("Which employee payroll you want to print out? ")
        question = input("Please enter employee id:")
        while question.isdigit() == False:
            question = input("Please enter employee id as number:")
        validation = DB.fetchall("SELECT Employee_ID FROM staff WHERE Employee_ID='{}'".format(question))
        if not validation:
            print("The employee id you entered is not exist in database!")
        else:
            db_employee_details = DB.fetchall("SELECT * FROM staff WHERE Employee_ID='{}'".format(question))
            db_salary_details = DB.fetchall("SELECT * FROM salary WHERE Employee_ID='{}'".format(question))
            employee_details = []
            salary_details = []
            for x in db_salary_details:
                for y in x:
                    salary_details.append(y)
            for x in db_employee_details:
                for y in x:
                    employee_details.append(y)

            employee_id = employee_details[0]
            employee_name = employee_details[1]
            employee_department = employee_details[2]
            employee_desgination = employee_details[3]

            basic_pay = salary_details[1]
            working_hours = salary_details[2]
            overtime_hours = salary_details[3]
            allowance = salary_details[4]
            cpf = salary_details[5]
            netpay = salary_details[6]
            leave = salary_details[7]

            overtime_pay = (basic_pay / 160)* 1.5 * overtime_hours
            overtime_pay_float = '{0:.2f}'.format(overtime_pay)
            unpaid_leave_amount = ((basic_pay) / 20) * leave
            unpaid_leave_amount_float = '{0:.2f}'.format(unpaid_leave_amount)
            total_deduction = cpf + float(unpaid_leave_amount_float)
            total_earning = basic_pay + float(overtime_pay_float) + allowance
        fileName = '{}.pdf'.format(employee_name)
        documentTitle = 'Document title!'
        title = 'Lenviva Computer Sdn Bhd '
        subTitle = 'Pay Slip for Feb 2021'
        PDF_Employee_ID = 'Employee_ID:'
        PDF_ID = '{}'.format(employee_id)
        PDF_Employee_Name = 'Employee_Name:'
        NAME = '{}'.format(employee_name)
        PDF_Department = 'Department:'
        Department_name = '{}'.format(employee_department)
        PDF_Designation = 'Designation:'
        Designation_name = '{}'.format(employee_desgination)
        PDF_Earnings = 'Earnings'
        Basic_pay_amount = '{}'.format(basic_pay)
        Overtime_pay_amount = '{}'.format(overtime_pay_float)
        Allowance_amount = '{}'.format(allowance)
        Total_earnings = '{}'.format(total_earning)
        Deductions = 'Deductions'
        Amount = 'Amount'
        Basic_pay = 'Basic pay'
        PDF_Overtime_pay = 'Overtime pay'
        PDF_Allowance = 'Allowance'
        PDF_Unpaid_leave = 'Unpaid leave'
        Unpaid_leave_amount = "{}".format(unpaid_leave_amount_float)
        PDF_CPF = 'CPF'
        CPF_amount = "{}".format(cpf)

        Hrs = '({}Hrs)'.format(overtime_hours)
        Day = '({}days)'.format(leave)

        Total_Earning = 'Total Earnings:'
        Total_Deductions = 'Total Deductions:'
        Total_Deductions_amount = '{}'.format(total_deduction)
        PDF_Net_pay = 'Net Pay:'
        Net_pay_amount = '{}'.format(netpay)

        # textLines = [
        # 'The Tasmanian devil (Sarcophilus harrisii) is',
        # 'a carnivorous marsupial of the family',
        # 'Dasyuridae.'
        # ]
        #
        # image = 'tasmanianDevil.jpg'
        #

        # ###################################
        # 0) Create document
        from reportlab.pdfgen import canvas

        pdf = canvas.Canvas(fileName)
        pdf.setTitle(documentTitle)

        # drawMyRuler(pdf)
        # ###################################
        # 1) Title :: Set fonts
        # # Print available fonts
        # for font in pdf.getAvailableFonts():
        #     print(font)

        # Register a new font
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfbase import pdfmetrics

        # pdfmetrics.registerFont(
        #     TTFont('abc', 'SakBunderan.ttf')
        # )
        pdf.setFont('Courier-Bold', 36)
        pdf.drawCentredString(300, 790, title)

        # ###################################
        # 2) Sub Title
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 20)
        pdf.drawCentredString(290, 750, subTitle)

        # ###################################
        # 3) Draw a line
        pdf.line(163, 745, 415, 745)

        # ###################################
        # 2) PDF_Employee_ID
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(80, 700, PDF_Employee_ID)

        # ###################################
        # 2) PDF_Employee_ID
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        a = 150 + ((len(PDF_ID) - 1) * 6)

        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(a, 700, PDF_ID)

        # ###################################
        # 2) Employee_name
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(90, 670, PDF_Employee_Name)

        # ###################################
        # 2) Employee_name
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        b = 175 + ((len(NAME) - 1) * 6)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(b, 670, NAME)

        # ###################################
        # 2) Department
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(73, 640, PDF_Department)

        # ###################################
        # 2) Department
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        c = 135 + ((len(Department_name) - 1) * 6)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(c, 640, Department_name)
        # ###################################
        # 2) Designation
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(78, 610, PDF_Designation)

        # ###################################
        # 2) Designation
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        d = 150 + ((len(Designation_name) - 1) * 6)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(d, 610, Designation_name)

        # ###################################
        # 2) Earnings
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(55, 557, PDF_Earnings)

        # ###################################
        # 2) Amount
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(265, 557, Amount)

        # ###################################
        # 2) Deductions
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(362, 557, Deductions)

        # ###################################
        # 2) Amount
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 18)
        pdf.drawCentredString(545, 557, Amount)

        # ###################################
        # 2) Basic pay
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(55, 525, Basic_pay)

        # ###################################
        # 2) Basic pay
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        e = 240 + ((len(Basic_pay_amount) - 1) * 6)

        g = len(Overtime_pay_amount) - len(Basic_pay_amount)
        if g == 2:
            e -= 12
        elif g == 1:
            e -= 6
        else:
            e = 240 + ((len(Basic_pay_amount) - 1) * 6)

        # e = 240 +((len(Basic_pay_amount)-1)*6)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(e, 525, Basic_pay_amount)

        # ###################################
        # 2) overtime pay
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(67, 495, PDF_Overtime_pay)

        # ###################################
        # 2) overtime pay
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        # g = len(Basic_pay_amount)-len(Overtime_pay_amount)
        # if g == 2:
        #     Overtime_pay_amount = "  "+Overtime_pay_amount
        # elif g == 1:
        #     Overtime_pay_amount = " "+Overtime_pay_amount
        # f = 240 +((len(Overtime_pay_amount)-1)*6)
        h = len(Basic_pay_amount) - len(Overtime_pay_amount)
        if h == 2:
            Overtime_pay_amount = "  " + Overtime_pay_amount
        elif h == 1:
            Overtime_pay_amount = " " + Overtime_pay_amount
        f = 240 + ((len(Overtime_pay_amount) - 1) * 6)

        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(f, 495, Overtime_pay_amount)

        # ###################################
        # 2) overtime pay
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        print(len(Hrs))
        j = 150 + ((len(Hrs) - 6) * 6)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(j, 495, Hrs)

        # ###################################
        # 2) allowance
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(55, 465, PDF_Allowance)

        # ###################################
        # 2) allowance
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        # j =len(Basic_pay_amount)- len(Overtime_pay_amount)
        # if h == 2:
        #     Overtime_pay_amount = "  "+Overtime_pay_amount
        # elif h == 1:
        #     Overtime_pay_amount = " "+Overtime_pay_amount
        i = len(Overtime_pay_amount) - len(Allowance_amount)
        if i == 3:
            Allowance_amount += "  "
        elif i == 1:
            Allowance_amount = " " + Allowance_amount

        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(f, 465, Allowance_amount)

        # ###################################
        # 2) unpaid leave
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(358, 525, PDF_Unpaid_leave)

        # ###################################
        # 2) unpaid leave
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        l = 528 + ((len(Unpaid_leave_amount) - 3) * 6)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(l, 525, Unpaid_leave_amount)

        # ###################################
        # 2) PDF_CPF
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(320, 495, PDF_CPF)

        # ###################################
        # 2) CPF
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        m = 528 + ((len(CPF_amount) - 3) * 6)
        n = len(Unpaid_leave_amount) - len(CPF_amount)
        if n == 3:
            CPF_amount = "  " + CPF_amount

        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(m, 495, CPF_amount)
        # ###################################
        # 2) Day
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        k = 442 + ((len(Day) - 7) * 6)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(k, 525, Day)

        # ###################################
        # 2) Day
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 12)
        pdf.drawCentredString(69, 360, Total_Earning)

        # ###################################
        # 2) Day
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        p = 240 + ((len(Total_earnings) - 3) * 6)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(p, 360, Total_earnings)

        # ###################################
        # 2) Day
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 12)
        pdf.drawCentredString(365, 360, Total_Deductions)

        # ###################################
        # 2) Day
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(l, 360, Total_Deductions_amount)

        # ###################################
        # 2) Day
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 12)
        pdf.drawCentredString(335, 325, PDF_Net_pay)

        # ###################################
        # 2) Day
        # RGB - Red Green and Blue
        # pdf.setFillColorRGB(0, 0, 255)

        pdf.setFont("Courier-Bold", 15)
        pdf.drawCentredString(l, 325, Net_pay_amount)

        #
        # # ###################################
        # # 4) Text object :: for large amounts of text
        # from reportlab.lib import colors
        #
        # text = pdf.beginText(40, 680)
        # text.setFont("Courier", 18)
        # text.setFillColor(colors.red)
        # for line in textLines:
        #     text.textLine(line)
        #
        # pdf.drawText(text)
        # column 1
        pdf.line(10, 580, 580, 580)
        pdf.line(10, 545, 580, 545)

        # column 2
        pdf.line(10, 380, 580, 380)
        pdf.line(10, 345, 580, 345)

        # centerline
        pdf.line(300, 580, 300, 345)

        # surronding line 4
        pdf.line(10, 820, 580, 820)
        pdf.line(10, 820, 10, 20)
        pdf.line(580, 820, 580, 20)
        pdf.line(10, 20, 580, 20)

        # column 2
        pdf.line(10, 310, 580, 310)

        # # ###################################
        # # 5) Draw a image
        # pdf.drawInlineImage(image, 130, 400)

        pdf.save()



start=Main()
start.selection()