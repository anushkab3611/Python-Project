from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    
    patients = {}
    fileName = "patients.txt"
    #Opening the file in read mode
    with open(fileName,"r") as file:
        # Read each line of the text file
        words = file.read().split()

        for i in words:
          line = i.split(",")         #making each line a list

          if len(line) != 8:          #checking the length of the list
            print(f"Invalid number of fields ({len(line)}) in line: {i}")
            continue

            # Check if the temperature value is within the range of 35 to 42
          if not (35 <= float(line[2]) <= 42):
                print(f"Invalid temperature value ({line[2]}) in line: {i}")
                continue

            # Check if the heart rate value is within the range of 30 to 180
          if not (30 <= int(line[3]) <= 180):
                print(f"Invalid heart rate value ({line[3]}) in line: {i}")
                continue

            # Check if the respiratory rate value is within the range of 5 to 40
          if not (5 <= int(line[4]) <= 40):
                print(f"Invalid respiratory rate value ({line[4]}) in line: {i}")
                continue

            # Check if the systolic blood pressure value is within the range of 70 to 200
          if not (70 <= int(line[5]) <= 200):
                print(f"Invalid systolic blood pressure value ({line[5]}) in line: {i}")
                continue

            # Check if the diastolic blood pressure value is within the range of 40 to 120
          if not (40 <= int(line[6]) <= 120):
                print(f"Invalid diastolic blood pressure value ({line[6]}) in line: {i}")
                continue

            # Check if the oxygen saturation value is within the range of 70 to 100
          if not (70 <= int(line[7]) <= 100):
                print(f"Invalid oxygen saturation value ({line[7]}) in line: {i}")
                continue

          try:
            patientsID = int(line[0])
            info = [line[j] for j in range(1,len(line))]

            if patientsID in patients:
              patients[patientsID].append(info)

            else:
              patients[patientsID] =[info]                    #storing the data in dictionary form as given


          except ValueError:
            print(f"Invalid data type in line: {i}")
            continue


          except FileNotFoundError:
            print(f"The file 'pateints.text' could not be found.")
            return None

          except:
            print("An unexpected error occurred while reading the file.")
            return None
    
    return patients           #returning the patient data dictionary
    


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    if patientId == 0:                                          # checking if the patientId is zero or not and if it is zero
      for i in patients:                                        # printing the details of all the patients one after the other
        print("\nPatient id",i)                                   # in a particular format
        for j in range(0,len(patients[i])):
          print("  Visit date",patients[i][j][0])
          print("    Temperature",patients[i][j][1],"C")
          print("    Heart rate",patients[i][j][2],"bpm")
          print("    Respriatory rate",patients[i][j][3],"bpm")
          print("    Systolyic bp",patients[i][j][4],"mmHg")
          print("    Diasystolyic bp",patients[i][j][5],"mmHg")
          print("    Oxygen saturation",patients[i][j][6],"%")

    elif patientId in patients:                                     # checking if the patientId is in the patients dationary or not
        print("Patient id",patientId)                               # and if found printing only that patients details
        for j in range(0,len(patients[patientId])):
          print("  Visit date",patients[patientId][j][0])
          print("    Temperature",patients[patientId][j][1],"C")
          print("    Heart rate",patients[patientId][j][2],"bpm")
          print("    Respriatory rate",patients[patientId][j][3],"bpm")
          print("    Systolyic bp",patients[patientId][j][4],"mmHg")
          print("    Diasystolyic bp",patients[patientId][j][5],"mmHg")
          print("    Oxygen saturation",patients[patientId][j][6],"%")
    else:
      print(" patient with id",patientId,"not found")





def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    try:  
      patientId = int(patientId)
    
      temp = hrate = res_rate =  sys_bp = dia_bp = o2_sat = c = 0
    
      if patientId == 0:                                              #checking if the patientid is zero or not if zero calculating
        print("Vital Signs for all patient")                          #and printing the average of the vital signs of all the patients        
        for i in patients:
          for j in range(0,len(patients[i])):  
             c = c+1
             temp += float(patients[i][j][1])
             hrate += int(patients[i][j][2])
             res_rate += int(patients[i][j][3])
             sys_bp += int(patients[i][j][4])
             dia_bp += int(patients[i][j][5])
             o2_sat += int(patients[i][j][6])
            
        print("   Average Temperature:", temp/c,"C")
        print("   Average Heart Rate:",hrate/c ,"bpm")
        print("   Average Respiratory Rate:",res_rate/c,"bpm")
        print("   Average Systolic Blood Pressure:", sys_bp/c,"mmHg")
        print("   Average Diastolic Blood Pressure:", dia_bp/c,"mmHg")
        print("   Average Oxygen Saturation:", o2_sat/c,"%") 
       
      elif patientId in patients:                                          #checking if a particular patientId is present in the list
        print("Vital signs for patient",patientId)                         #if yes calculating and printing the average of that particular
        for j in range(0,len(patients[patientId])):                        # patient
            c = c+1
            temp += float(patients[patientId][j][1])
            hrate += int(patients[patientId][j][2])
            res_rate += int(patients[patientId][j][3])
            sys_bp += int(patients[patientId][j][4])
            dia_bp += int(patients[patientId][j][5])
            o2_sat  += int(patients[patientId][j][6])   
        print("   Average Temperature:", temp/c,"C")
        print("   Average Heart Rate:",hrate/c,"bpm" )
        print("   Average Respiratory Rate:",res_rate/c,"bpm")
        print("   Average Systolic Blood Pressure:", sys_bp/c,"mmHg")
        print("   Average Diastolic Blood Pressure:", dia_bp/c,"mmHg")
        print("   Average Oxygen Saturation:", o2_sat/c,"%")     
      else:
       print( " patient with id",patientId,"not found")
     
    except Exception as a:
        print("Error:'patientId' should be an integer")
    






def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    
    try:
        # Check date format
        year, month, day = map(int, date.split("-"))
        if not (1900 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
            print("Invalid date. Please enter a valid date.")
            return
        
        # Check temperature
        if not (35.0 <= temp <= 42.0):
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
            return
        
        # Check heart rate
        if not (30 <= hr <= 180):
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
            return
        
        # Check respiratory rate
        if not (5 <= rr <= 40):
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
            return
        
        # Check systolic blood pressure
        if not (70 <= sbp <= 200):
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
            return
        
        # Check diastolic blood pressure
        if not (40 <= dbp <= 120):
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
            return
        
        # Check oxygen saturation level
        if not (70 <= spo2 <= 100):
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
            return
        
        # Add data to dictionary
        if patientId not in patients:
            patients[patientId] = []
        patients[patientId].append([ date, temp, hr, rr, sbp, dbp, spo2])
        
        # Append data to file
        with open(fileName, "a") as file:
            
            file.write("\n"+",".join(map(str, [patientId, date, temp, hr, rr, sbp, dbp, spo2])))
        
        print("Visit is saved successfully for Patient #",patientId)
        
    except ValueError:
        print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
    except Exception:
        print("An unexpected error occurred while adding new data.")



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    

    visits = []
    patientId_list=[key for key in patients] #appending the patient id's in a list

    #checking the conditions for year is given and month is not given in parameters or not
    if year!=None and month==None:
        if year>=1900 and len(str(year))==4:  #checking the validity of year
            for i in patientId_list:
                    for j in range(len(patients[i])):
                        #checking if the year matches in the dictionary
                        if int(patients[i][j][0][:4])==year:
                            data_tuple=(i,patients[i][j])          #storing it in a tuple first
                            visits.append(data_tuple)                        #appending that tuple in visits list

    #checking the conditions for both year and month are not given in parameters or not
    elif year!=None and month!=None:
        if year>=1900 and len(str(year))==4 and 1<=month<=12:                #checking the validity of both year and month
            for i in patientId_list:
                    for j in range(len(patients[i])):
                        #checking if the year and month matches in the dictionary
                        if int(patients[i][j][0][:4])==year and int(patients[i][j][0][5:7])==month:
                            data_tuple=(i,patients[i][j])
                            visits.append(data_tuple)

    #else block operates on all the years and months of dictionary
    else:
        for i in patientId_list:
            for j in range(len(patients[i])):
                data_tuple=(i,patients[i][j])
                visits.append(data_tuple)

    return visits
    


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []                                     
    for i in patients:                                  #checking if the heartrate, systolic bp, diastolic bp and oxygen saturation
          for j in range(0,len(patients[i])):           #of all patients are normal or not if not appending the patientId to the list
              if (int(patients[i][j][2]) not in range(60,101) or int(patients[i][j][4]) >140 or int(patients[i][j][5])>90 or int(patients[i][j][6])<90):
                 if i not in followup_patients:
                   followup_patients.append(i)
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    patientId = int(patientId)
    
    if patientId in patients:                     #checking if the patientId is the dictionary then deleting its value
      patients[patientId] = []
 
      print("Data for patient ID",patientId ,"has been deleted")
      with open(filename,"w") as file:
            for patient_id, visits in patients.items():             #loop to find the key that is patientId and visits that is        
                for visit in visits:                                #value in dictionary patients and writing this in a new file
                    file.write(','.join(map(str, [patient_id] + visit)) + '\n')

    else:
        print("No data found for patient with ID ",patientId) 
            

                

                


###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()

