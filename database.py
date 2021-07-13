import sqlite3

#creating database for other FIRS:

def otherfir(name,mobile_no,aadhar_no,email,dob,problem):
        conn_other = sqlite3.connect('other_fir.db') #connecting to other firs database
        c = conn_other.cursor()# creating cursor        
        many_inputs = [name,mobile_no,aadhar_no,email,dob,problem]     

        c.executemany("INSERT INTO other_firs VALUES(?,?,?,?,?,?)", (many_inputs,)) #inserting values 
        conn_other.commit()
        print("added to other fir db")
        
        conn_other.close()
# connecting database for vehicle theft FIRS

def vehicletheft(name, mobile_no,aadhar_no,email, dob,vehicle,number_plate,colour,last_seen,anything_else):
        conn_other = sqlite3.connect('vehicletheft_fir.db')
        c = conn_other.cursor()
       
        many_inputs = [(name, mobile_no,aadhar_no,email, dob,vehicle,number_plate,colour,last_seen,anything_else)]
        c.executemany("INSERT INTO vehicle_theft  VALUES(?,?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values 
        conn_other.commit()

        conn_other.close()

#connecting Database for goods theft FIR

def goods_theft(name, mobile_no,aadhar_no,email, dob,goods_stolen,date_time,last_seen,anything_else):
        conn_other = sqlite3.connect('goodstheft_fir.db')
        c = conn_other.cursor()
       
        many_inputs = [(name, mobile_no,aadhar_no,email, dob,goods_stolen,date_time,last_seen,anything_else)]
        c.executemany("INSERT INTO goods_theft  VALUES(?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values 
        conn_other.commit()

        conn_other.close()

#connecting database for missing person FIR

def missingperson(name, mobile_no,aadhar_no, email, dob, name_of_missing_person, age_of_mm, sex_of_mm, clothes_of_mm, last_seen, anything_else):
        conn_other = sqlite3.connect('missing_person_fir.db')
        c = conn_other.cursor()        
        many_inputs = [(name, mobile_no,aadhar_no,email, dob,name_of_missing_person,age_of_mm,sex_of_mm,clothes_of_mm,last_seen,anything_else)]
        c.executemany("INSERT INTO missing_person  VALUES(?,?,?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values 
        conn_other.commit()

        conn_other.close()

#connecting database for lost and find FIR

def lostandfound(name, mobile_no,aadhar_no,email, dob,lost_or_found,item_lost_or_found,location_of_item,anything_else):
        conn_other = sqlite3.connect('lostandfound_fir.db')
        c = conn_other.cursor()
        many_inputs = [(name, mobile_no,aadhar_no,email, dob,lost_or_found,item_lost_or_found,location_of_item,anything_else)]
        c.executemany("INSERT INTO lostandfound  VALUES(?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values 
        conn_other.commit()

        conn_other.close()

#connecting Database for assault FIRS

def assault(name, mobile_no,aadhar_no,email, dob, complaint_against,assault_description,anything_else):
        conn_other = sqlite3.connect('assault_fir.db')
        c = conn_other.cursor()     
        many_inputs = [(name, mobile_no,aadhar_no,email, dob, complaint_against,assault_description,anything_else)]
        c.executemany("INSERT INTO assault  VALUES(?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values 
        conn_other.commit()

        conn_other.close()

#connecting Database for civic grievance FIRS 

def civic_grievance(name, mobile_no,aadhar_no,civic_grievance, location,state, landmark, anything_else):
        conn_other = sqlite3.connect('civic_grievance.db')
        c = conn_other.cursor()
        
        many_inputs = [(name, mobile_no,aadhar_no,civic_grievance, location,state, landmark, anything_else)]
        c.executemany("INSERT INTO civic_grievance  VALUES(?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values 
        conn_other.commit()

        conn_other.close()

#connecting database for dl motorcycle without gear        
def dl_mc_gearless( learners_licence_no, name ,age , dob, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment ):
        conn_other = sqlite3.connect('driving_licence.db') 
        c = conn_other.cursor()
        many_inputs = [( learners_licence_no, name ,age , dob, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment )]
        c.executemany("INSERT INTO dl_motorcycle_gearless  VALUES(?,?,?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values
        conn_other.commit()

        conn_other.close() 
#connecting database for motorcycle with gear
def dl_mc_gear( learners_licence_no, name ,age , dob, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment ):
        conn_other = sqlite3.connect('driving_licence.db') 
        c = conn_other.cursor()
        many_inputs = [( learners_licence_no, name ,age , dob, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment )]
        c.executemany("INSERT INTO dl_motorcycle_gear  VALUES(?,?,?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values
        conn_other.commit()

        conn_other.close() 
#connecting database for chv or transport vehicle
def dl_chv( learners_licence_no, name ,age , dob, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment ):
        conn_other = sqlite3.connect('driving_licence.db') 
        c = conn_other.cursor()
        many_inputs = [( learners_licence_no, name ,age , dob, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment )]
        c.executemany("INSERT INTO chv  VALUES(?,?,?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values
        conn_other.commit()

        conn_other.close() 

#connecting database for ll motorcycle without gear 
def ll_mc_gearless(name ,age , dob, pob, citizenship_type, education, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment ) :
        conn_other = sqlite3.connect('learners_licence.db')      
        c = conn_other.cursor()
        many_inputs = [( name ,age , dob, pob, citizenship_type, education, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment)]
        c.executemany("INSERT INTO chv  VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values
        conn_other.commit()

        conn_other.close() 
#connecting database for motorcycle with gear        

def ll_mc_gear(name ,age , dob, pob, citizenship_type, education, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment ) :
        conn_other = sqlite3.connect('learners_licence.db')      
        c = conn_other.cursor()
        many_inputs = [( name ,age , dob, pob, citizenship_type, education, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment)]
        c.executemany("INSERT INTO ll_motorcycle_gear VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values
        conn_other.commit()

        conn_other.close() 

#connecting database for chv or transport vehicle

def ll_chv(name ,age , dob, pob, citizenship_type, education, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment ) :
        conn_other = sqlite3.connect('learners_licence.db')      
        c = conn_other.cursor()
        many_inputs = [( name ,age , dob, pob, citizenship_type, education, mobile_no , aadhar_no , current_address ,city,pincode ,date_for_appointment ,slot_for_appointment)]
        c.executemany("INSERT INTO ll_chv VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (many_inputs)) #inserting values
        conn_other.commit()

        conn_other.close() 

#connecting database for hospitals
def hospital(name_of_ailment,name,age ,dob,blood_group, sex,marital_status,mobile_no,aadhar_no,current_address ,city, pincode ):
        conn_other = sqlite3.connect('hospital.db')
        c = conn_other.cursor()
        many_inputs = [(name_of_ailment,name,age ,dob,blood_group, sex,marital_status,mobile_no,aadhar_no,current_address ,city, pincode )]
        c.executemany("INSERT INTO hospital VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (many_inputs))

        conn_other.commit()
        conn_other.close()

def police_no(city):
        conn_other = sqlite3.connect('police_no.db')
        c = conn_other.cursor()
        city= city.lower()
        try: 
                if (city == 'mumbai'):
                        c.execute("SELECT * FROM mumbai ")
                        return(c.fetchall())
                elif (city == 'chandigarh'):
                        c.execute("SELECT * FROM chandigarh ")
                        return(c.fetchall())
                elif (city == 'delhi'):
                        c.execute("SELECT * FROM delhi ")
                        return(c.fetchall())
        except: 
                c.execute("SELECT * FROM india ")
                return(c.fetchall()) 

        conn_other.commit()
        conn_other.close()                          


#print(police_no('delhi'))


# conn_other = sqlite3.connect('police_no.db')
# c = conn_other.cursor()
# c.execute(""" CREATE TABLE india(
#                 service text,
#                 number text) """)

# many_inputs= [('NATIONAL EMERGENCY NUMBER','112'),
# ('POLICE','100'),
# ('FIRE','101'),
# ('AMBULANCE','102'),
# ('Disaster Management Services','108'),('Women Helpline','1091'),
# ('Women Helpline - ( Domestic Abuse )','181'),('Air Ambulance','9540161344 '),('Aids Helpline','1097')] 

# c.executemany("INSERT INTO india VALUES(?,?)", (many_inputs))
# conn_other.commit()
# print("done")
# conn_other.close()                
#####################
# conn_other = sqlite3.connect('driving_licence.db') 
# c = conn_other.cursor()
# c.execute(""" CREATE TABLE ll_chv(
                        
#                     name text,
#                     age text,
#                     dob text,
#                     pob text,
#                     citizenship_type text,
#                     education text,
#                     mobile_no text,
#                     aadhar_no text,
#                     current_address text,
#                     city text,
#                     pincode text,
#                     date_for_appointment text,
#                     slot_for_appointment text
#                     )""")
# conn_other.commit()
# c.execute("SELECT * FROM dl_motorcycle_gearless")
# print(c.fetchall())
# print("done")
# conn_other.commit()
# conn_other.close()

# conn_other = sqlite3.connect('civic_grievance.db')
# c= conn_other.cursor()
# # c.execute(""" CREATE TABLE missing_person(
                        
# #                     name text,
# #                     mobile_no text,
# #                     aadhar_no text,
# #                     email text, 
# #                     dob text, 
# #                     name_of_missing_person text, 
# #                     age_of_mm text, 
# #                     sex_of_mm text, 
# #                     clothes_of_mm text, 
# #                     last_seen text, 
# #                     anything_else text)""") 
# c.execute("""ALTER TABLE lostandfound
#                 RENAME TO civic_grievance""")

# conn_other.commit()
# print("done")
# conn_other.close()

# conn_other = sqlite3.connect('lostandfound_fir.db')
# c= conn_other.cursor()
# c.execute(""" CREATE TABLE lostandfound (
#         name text,
#         mobile_no text, 
#         aadhar_no text,
#         email text,
#         dob text,
#         lost_or_found text,
#         item_lost_or_found text,
#         location_of_item text,
#         anything_else text
#         )""")
# conn_other.commit()
# print("done")
# conn_other.close()