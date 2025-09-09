 
import sqlite3 as s 
con=s.connect('doctor.db')
cur=con.cursor()
#table='create table PATIENT_DETAILS(PATIENT_ID int ,NANE_PATIENT varchar(50) ,AGE int ,GENDER varchar(5) ,ADDRESS varchar(150) ,DISEASE varchar(50) ,SYMPTOMS varchar(150),DATE date,PHONE_NO int,PRIMARY KEY(PATIENT_ID))'
#cur.execute(table);

print('             * * *                                                                           * * *')                       
print('             * * *                                                                           * * *')
print('             * * *                                                                           * * *')
print('             * * *                                                                           * * *')
print('    * * * * * * * * * * * *                 +--------+              * * * * * * * * * * * *')
print('    * * * * * * * * * * * *                 ****HEALTH IS WEALTH****              * * * * * * * * * * * *')
print('    * * * * * * * * * * * *                 +--------+              * * * * * * * * * * * *')
print('             * * *                                                                           * * *')
print('             * * *                                                                           * * *')
print('             * * *                                                                           * * *')     
print('             * * *                                                                           * * *')
print('1. LOGIN\n2. EXIT')
ch1=input("If you want to login enter space else enter any other key to exit..\n")
if ch1==' ':
    user=input('USERNAME-')
    if user=='MSSTCS':
        pswd=input('PASSWORD-')
        if pswd==('12252731cs'):
            print('LOGGED IN')
            print('\n                              ++ WELCOME TO THE SYSTEM ++')
            print("\n\n\n1. ADD PATIENT DETAILS\n2. UPDATE PATIENT DETAILS\n3. SEARCH PATIENT DETAILS\n4. DELETE PATIENT RECORD\n5. DISPLAY ALL PATIENT DETAILS")
           
            
            def add():
                n=int(input("NO. OF PATIENT'S DATA TO BE ADDED:  "))
                for i in range (n): 
                    P_ID=int(input("PATIENT_ID >"))
                    P_NAME=input("PATIENT_NAME >")
                    P_AGE=int(input("AGE >"))
                    P_G=input("GENDER(M/F) >")
                    P_ADD=input("ADDRESS >")
                    P_D=input("DISEASE >")
                    P_SYMP=input("SYMPTOMS >")
                    DATE=input("TODAY'S DATE(YYYY-MM-DD) >")
                    P_PH=int(input("PHONE NO. OF PATIENT >"))
                    insert= 'insert into PATIENT_DETAILS values({},"{}",{},"{}","{}","{}","{}","{}",{})'.format(P_ID,P_NAME,P_AGE,P_G,P_ADD,P_D,P_SYMP,DATE,P_PH)
                    cur.execute(insert)
                    con.commit()
              
            def update():
                D={1:"PATIENT_ID",2:"NAME_PATIENT",3:"AGE",4:"GENDER",5:"ADDRESS",6:"DISEASE",7:"SYMPTOMS",8:"DATE",9:"PHONE_NO"}
                MC=input("NAME OF COLUMN TO MODIFY:")
                P_id=input("PATIENT ID:")
                Q='select * from PATIENT_DETAILS'
                cur.execute(Q)
                rec=cur.fetchall()
                for i in rec:
                    for k in D:
                        if D[k]==MC:
                            if type(i[k-1])==int:
                                ask=input('if u want to INCREASE or DECREASE the value of data then press {M}\nif you want to simly update the data by other number then press {U}\n>>>') 
                                if ask=='M':
                                    O=int(input('enter the number that u want to add into your data '))   
                                    update='update PATIENT_DETAILS set {}={}+{} where PATIENT_ID={}'.format(MC,MC,O,P_id)
                                    cur.execute(update)
                                    con.commit()
                                    return
                                elif ask=='U':
                                    MD=input('MODDIFIED DATA:')
                                    update='update PATIENT_DETAILS set {}={} where PATIENT_ID={}'.format(MC,MD,P_id)
                                    cur.execute(update)
                                    con.commit()
                                    return
                            elif type(i[k-1])==str:
                                MD=input('MODDIFIED DATA:') 
                                update='update PATIENT_DETAILS set {}="{}" where PATIENT_ID={}'.format(MC,MD,P_id)
                                cur.execute(update)
                                con.commit()
                                return
                            elif i[k-1]==None:
                                MD=input('MODDIFIED DATA:')
                                update='update PATIENT_DETAILS set {}="{}" where PATIENT_ID={}'.format(MC,MD,P_id)
                                cur.execute(update)
                                con.commit()
                                return
                        else:        
                            k+=1
            def search():
                n=int(input("NO. OF PATIENT'S DATA YOU WANT TO SEARCH: "))
                for i in range (n): 
                    W=input('IF YOU WANT TO SEE ALL THE DETAILS OF A PATIENT PRESS {Y}\nIF YOU WANT TO SEE A SPECIFIC DETAIL OF A PATIENT PRESS{N}')
                    P_id=int(input('PATIENT ID:'))
                    Ph=int(input('PHONE NO.'))
                    if W=='Y':
                        search='select * from PATIENT_DETAILS where PATIENT_ID={} or PHONE_NO={}'.format(P_id,Ph)
                        cur.execute(search)
                        print(cur.fetchall())
                    elif W=='N':
                        S=input('WHAT DO YOU WANT TO SEARCH:')
                        search='select {} from PATIENT_DETAILS where PATIENT_ID={} or PHONE_NO={}'.format(S,P_id,Ph)                                                                                  
                        cur.execute(search)
                        print(cur.fetchall())

            def delete():
                n=int(input("NO. OF PATIENT'S DATA TO BE DELETED: "))
                for i in range (n):
                    P_id=int(input('PATIENT ID:'))
                    Ph=int(input('PHONE NO.'))
                    delete='delete from PATIENT_DETAILS where PATIENT_ID={} or PHONE_NO={} '.format(P_id,Ph)
                    cur.execute(delete)
                    con.commit()
            
            def display():
                cur.execute('select * from PATIENT_DETAILS ORDER BY PATIENT_ID asc')
                print("((PATIENT_ID  ,NAME_PATIENT  ,AGE ,GENDER ,ADDRESS ,DISEASE ,SYMPTOMS ,DATE ,PHONE NO.))")
                while True:
                    F=cur.fetchone()
                    print(F)
                    if F==None:
                        break
               
               
                
            
            while True:
                ch2=input('\n\nENTER YOUR CHOICE FROM 1 TO 5 AS PER MENU GIVEN ABOVE >>')
                if ch2=='1':
                    add()
                elif ch2=='2':
                    update()
                elif ch2=='3':
                    search()
                elif ch2=='4':
                    delete()
                elif ch2=='5':
                    display()
                else:
                    con.close()
                    break       
        else:
            print('incorrect password')
        
else:
      exit()