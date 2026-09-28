

def main():    
    list1=[30,20,3000,5000, None, None]
    list2=[list1[0], list1[1]]
    x=dashboard()
    y=1

    while (y==1):
        if (x==2):              
            list2=available_bedcount(list1)
            list1[4]=list2[0]
            list1[5]=list2[1]        
            x=dashboard(*list1)
                       

       
        elif (x==1):               
            list1=modify_admin_info() 
            list2=[list1[0], list1[1]]      
            list1[4]=list2[0]
            list1[5]=list2[1] 
            x = dashboard(*list1)
        
        else:
            y=2
            break

       

def dashboard(num1=30, num2=20, rate1=3000, rate2=5000, avail1=30, avail2=20):
    
    print("-"*100)
    print(" ICU BED LIVE DASHBOARD")
    print()
    print("-"*100)
    print(" Arogya Hospital & Research Centre, Bongaigaon, Assam")
    print()
    print("-"*100)    
    print("Total no. of ICU bed: ", num1 + num2)
    print()
    print("-"*100)
    print("Total normal ICU bed without ventilator: ", num1)
    print("Currently occupied normal ICU bed without ventilator: ", num1-avail1)
    print("Available ICU bed without ventilator: ", avail1)
    print("Rate: ₹",rate1)    
    print()
    print("-"*100)
    print("Total normal ICU bed with ventilator: ", num2)
    print("Currently occupied ICU bed with ventilator: ", num2-avail2)
    print("Available ICU bed with ventilator: ", avail2)
    print("Rate: ₹", rate2)    
    print()
    print("-"*100)    
    return int(input("Press 1 to go to Admin login || Press 2 to modify occupancy: "))

    
    
def modify_admin_info():
    print()
    print("-"*100)
    print("ADMIN LOGIN")
    print("-----this edit will change the live bed count-----")
    bednum1=int(input("Enter the total no. of ICU bed without ventilor: "))
    bednum2=int(input("Enter the total no. of ICU bed with ventilor: "))
    bedrate1=int(input("Enter the rate of ICU bed without ventilor in ₹: "))
    bedrate2=int(input("Enter the rate of ICU bed with ventilor in ₹: "))
    return [bednum1, bednum2, bedrate1, bedrate2, None, None]



def available_bedcount(list3):
    print()
    print("-"*100) 
    occupancy1=int(input("Enter occupancy of ICU bed without ventilator: "))
    occupancy2=int(input("Enter occupancy of ICU bed with ventilator: "))
    bedcount1= list3[0]- occupancy1
    bedcount2= list3[1]- occupancy2
    return [bedcount1, bedcount2]


if __name__=="__main__":
    main()

