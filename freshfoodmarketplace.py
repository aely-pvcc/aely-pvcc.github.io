# Names: Kayla Shifflett & Addison Ely
# Program Purpose: This program calculates the weekly pay of 4 different categories of employees.


import datetime

######## define global variables #########
# define rates based on job
CASHIER_WAGE = 16.50
STOCKER_WAGE = 15.75
JANITOR_WAGE = 15.75
MAINTENANCE_WAGE = 19.50

FIT = .12
SIT = .03
SS = .062
MED = .0145

# define global variables
fit_amt = 0
sit_amt = 0
ss_amt = 0
med_amt = 0

job_cat = ""
g_pay = 0
net_pay = 0
num_hour_work = 0
total_ded = 0

######## define program functions ########
def main():
    more_data = True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nDo you want to calculate pay for another employee? : ")
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for using this program!")
            print("To see our other programs, go to: \n\thttps://kshifflett-pvcc.github.io/ and https://aely-pvcc.github.io/")
            

def get_user_data():
    global job_cat, num_hour_work
    job_cat =(input("Job category:\nEnter\n C for Cashier \n S for Stocker \n J for Janitor \n M for Maintenance."))
    num_hour_work = int(input("Number of hours worked: "))

def perform_calculations():
    global job_cat, num_hour_work, g_pay, total_ded, net_pay, fit_amt, sit_amt, med_amt, ss_amt
    if job_cat == "C" or job_cat == "c":
        g_pay = num_hour_work * CASHIER_WAGE
        fit_amt = g_pay * FIT
        sit_amt = g_pay * SIT
        ss_amt = g_pay * SS
        med_amt = g_pay * MED
        total_ded = fit_amt + sit_amt + ss_amt + med_amt
        net_pay = g_pay - total_ded

    if job_cat == "S" or job_cat == "s":
        g_pay = num_hour_work * STOCKER_WAGE
        fit_amt = g_pay * FIT
        sit_amt = g_pay * SIT
        ss_amt = g_pay * SS
        med_amt = g_pay * MED
        total_ded = fit_amt + sit_amt + ss_amt + med_amt
        net_pay = g_pay - total_ded

    if job_cat == "J" or job_cat == "j":
        g_pay = num_hour_work * JANITOR_WAGE
        fit_amt = g_pay * FIT
        sit_amt = g_pay * SIT
        ss_amt = g_pay * SS
        med_amt = g_pay * MED
        total_ded = fit_amt + sit_amt + ss_amt + med_amt
        net_pay = g_pay - total_ded

    if job_cat == "M" or job_cat == "m":
        g_pay = num_hour_work * MAINTENANCE_WAGE
        fit_amt = g_pay * FIT
        sit_amt = g_pay * SIT
        ss_amt = g_pay * SS
        med_amt = g_pay * MED
        total_ded = fit_amt + sit_amt + ss_amt + med_amt
        net_pay = g_pay - total_ded

def display_results():
    line = '--------------------------------------------------'
    print(line)
    print('****          Fresh Food Marketplace          ****')
    print('****      Employee Weekly Pay Calculator      ****')
    print(line)
    print('Gross pay                       $ ' + format(g_pay,     '8,.2f'))
    print('Deductions Total                $ ' + format(total_ded, '8,.2f'))
    print('\tFederal Income Tax      $ ' + format(fit_amt,   '8,.2f'))
    print('\tState Income Tax        $ ' + format(sit_amt, '8,.2f'))
    print('\tSocial Security Tax     $ ' + format(ss_amt,  '8,.2f'))
    print('\tMedicare Tax            $ ' + format(med_amt, '8,.2f'))
    print('Net Pay                         $ ' + format(net_pay,   '8,.2f'))
    print(line)
    print(str(datetime.datetime.now()))
            
######### call on main program to execute ########
main()
