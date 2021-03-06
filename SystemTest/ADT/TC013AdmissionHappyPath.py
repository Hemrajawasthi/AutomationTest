#-------------Objective of this script----------
# To verify successful admission of newly registered patient.

from TestActionLibrary import A

#------------Local Veriables-------------------
#labitem = "Urine RE/ME"
#imagingitem ="USG ABDOMEN & PELVIS"
deposit = 0

#-------------Script Owner: Hari----------------
#Scripted on: 12.05.2077

ADT = A()

ADT.openBrowser()
ADT.login("billing1", "pass123")
ADT.patientRegistration()
ADT.counteractivation()
ADT.admitDisTrans(1, 0, 0, deposit)
ADT.logout()
ADT.closeBrowser()
print("\033[1;32;40m TC013 AdmissionHappyPath: Passed  \n")
