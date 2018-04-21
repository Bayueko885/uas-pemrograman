import texttable as tt
import getpass
from uas.penilaian import nilai_mahasiswa
from uas.pembayaran import pembayaran
from uas.calculator import pilihan

def menu():
    print("==========================================")
    print("\n\t----pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. calculator")
    
    pilih=input("\n\tsilakan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2":
        pembayaran()
    elif pilih == "3":
        pilihan()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y\t)?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input................!!!")

username=input("\nUsername : ")
password=getpass.getpass()
print("======================================================")
if username == "bayu" and password == "qwerty":
    menu()

else:
    print("maaf password salah...!!!")

    
          
