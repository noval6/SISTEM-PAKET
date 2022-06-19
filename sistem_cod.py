import os
import ast
cwd = os.getcwd()
def main():
    
    print("[*] Sistem Check Resi Cash On Delivery.")
    data_input = input("[*] Masukkan Kode Resi: ")
    #memanggil funggsi data
    list_resi = data_resi()
 
    #memanggil fungsi checking untuk check resi
   
    checking(list_resi, data_input)

def checking(list_resi, data_input):
    data_input = data_input
    list_resi = list_resi 
     
    #checking data cod
    if list_resi[f'{data_input}'][2] in 'Cash On Delivery':
        print("[*] Resi merupakan Pembayaran Cash On Delivery/COD.")
        print("[*] =========== Rincian ==========")
        print(f"[*] Kode Resi: {data_input}")
        print(f"[*] Alamat: {list_resi[f'{data_input}'][0]}")
        print(f"[*] Status: {list_resi[f'{data_input}'][1]}")

    elif list_resi[f'{data_input}'][2] in 'Transfer':
        print("[*] Resi merupakan Pembayaran Transfer.")
        print("[*] =========== Rincian ==========")
        print(f"[*] Kode Resi: {data_input}")
        print(f"[*] Alamat: {list_resi[f'{data_input}'][0]}")
        print(f"[*] Status: {list_resi[f'{data_input}'][1]}")
    else:
        print("[*] Resi Tidak Ditemukan.")
    pilihan = input("[*] Periksa Resi lagi? (Y/T)")   
     
    if pilihan == "y" or pilihan == "Y":
        main()
    else:
        print("[*] Finish, Thank you!")

def data_resi():
    #nama file yang akan dibuka
    try:
        file = "resi.txt"
        #membuka file 
        hasil = openfile(file)
        return hasil
 
    except:
        print("[*] File Resi Tidak Ditemukan!")

def openfile(file_list):

    file_list = file_list
    myfile = open(f"{cwd}/{file_list}","r")
    #membaca file
    contents = myfile.read()
    dictionary = ast.literal_eval(contents)
    myfile.close()
    #print(dictionary)
    return dictionary

main()