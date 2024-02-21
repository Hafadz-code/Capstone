from tabulate import tabulate

# data tabel awal
data = [
	    {'Nomor': 1,'Nama Mobil':'Lykan Hypersport','Harga Sewa ($/hari)':500 ,'Warna':'Merah', 'Tahun':2022}, 
	    {'Nomor': 2,'Nama Mobil':'Aston Martin Vanquish','Harga Sewa ($/hari)':360,'Warna':'Biru', 'Tahun':2023},
	    {'Nomor': 3,'Nama Mobil':'Koenigsegg CCXR Trevita','Harga Sewa ($/hari)':620,'Warna':'putih', 'Tahun':2022},
	      {'Nomor': 4,'Nama Mobil':'Bugatti Veyron','Harga Sewa ($/hari)':540,'Warna':'Hitam', 'Tahun':2023},
		{'Nomor': 5,'Nama Mobil':'Rolls-Royce Sweptail','Harga Sewa ($/hari)':480,'Warna':'Hitam', 'Tahun':2022},
    ]

# Tampilkan data (dalam hal ini data tabel)
def read_data():
	    print(tabulate(data, headers = 'keys', tablefmt='fancy_grid'))



# Input data baru (dalam hal ini pemberi sewa) - belum selesai
def create_data():
      print('''
      SILAHKAN DAFTARKAN MOBIL ANDA!
      ''')
      Mobil_baru = input("Masukkan Nama Mobil: ")                
      Biaya  = int(input("Masukkan Biaya sewa: "))                
      Color = input("Masukkan Warna Mobil: ")
      Tahun = input("Masukkan Tahun Mobil: ")
      
      new_data = {"Nomor": (len(data))+1, "Nama Mobil": Mobil_baru, "Harga Sewa ($/hari)": Biaya+(1/10*Biaya), "Warna": Color, 'Tahun': Tahun}  
      data.append(new_data)
      read_data()                                                 
      print("Penyewaan Mobil telah diterima, terima kasih")
      exit()

# Hapus data (dalam hal ini pengurangan mobil oleh penyewa)
def hapus_data(): 
     while True:
          inputan = input('Masukkan nama Anda:')
          if inputan.isalpha():
                  print(f'Halo {inputan}')
          
                  while True:
                        umur = input('Berapa umur anda?')
                        if int(umur) <= 19:
                              print(f'Maaf, Umur anda belum cukup!')
                              continue
                        else :print('''****** Pilih mobil yang akan anda sewa ******''')
                        read_data()
                  
                        
                        while True:
                              hapus_data = input('Silahkan pilih mobil anda!')           
                              if int(hapus_data) >= (len(data)+1):
                                    continue
                              else:
                                    hari_sewa = input("Berapa hari anda ingin menyewa?")
                                    a = data[int(hapus_data)-1]
                                    b = a['Harga Sewa ($/hari)']*int(hari_sewa)
                                    print (f'total biaya anda adalah: $',{b})
                                    del data [int(hapus_data)-1]
                                    print('Berikut sisa mobil yang masih tersedia')  
                                    read_data()
                                    exit()                                                 
                                    break
                        break       
                  break
          else:
                print("Tolong ketik Nama anda kembali!")

def input_int():
      while True:
            try:
                  inputan = int(input())
                  return inputan
                  break
            except:
                  print('yang anda masukkan salah')

# Update data tabel terbaru (menggantikan data value nya dengan yang lain) dengan menggunakan user admin
def update_data(): 
      while True:
            print('Masukkan User Admin: ')
            username = input()
            if username.capitalize() != 'Farhan':
                  print(f'Username {username} tidak terdaftar')
                  continue
    
            while True:
                  password = input('Hello, Farhan. Silahkan input Pin anda!')
                  if int(password) != 123:
                        print(f'Pin anda salah!')
                        continue
                  else :print('''
                  ****** Menu Pengkinian Data ******''')             
        
                
                  
        
                  print ('''
                  Pilih data yang ingin anda ganti 
                  ''')
                  read_data()
                  baris_data = int(input('Masukan angka Nomor mobil!'))
                  
                  print(''' Pilih item yang akan di ubah dengan ketik angka berikut:
                        1. Nomor Mobil
                        2. Nama Mobil
                        3. Harga Sewa $/hari
                        4. Warna
                        5. Tahun
                        ''')
                  
                  c = int(input('Masukan data yang ingin anda perbaharui'))
                  if c == 1:
                        y = data[baris_data-1]
                        y['Nomor']= input("input data baru")
                  elif c == 2:
                        y = data[baris_data-1]
                        y['Nama Mobil']= input("input nama Mobil terbaru")                                                 
                  elif c == 3:
                        y = data[baris_data-1]
                        y['Harga Sewa ($/hari)']= input("input Harga terbaru")                                        
                  elif c == 4:                                                      
                        y = data[baris_data-1]
                        y['Warna']= input("input Warna mobil terbaru")                                            
                  elif c == 5:                                                      
                        y = data[baris_data-1]
                        y['Tahun']= input("input data Tahun Mobil terbaru")
                                                             
                        
                  read_data()
                  print ('Data berhasil di ubah')
                                                                        
                  while True:
                        print(''' Apakah masih ada yang ingin anda ubah:
                        1. Kembali Updating data
                        2. Kembali ke Menu utama
                        3. Keluar     
                        ''')
                        try:
                              back = int(input('Masukan angka menu!'))
                              if back == 1:
                                    update_data()                                           
                              elif back == 2:
                                    main()                                         
                              elif back == 3:
                                    exit()                                                                                      
                              
                                                                                          
                        except:
                              print ('Tolong masukan angka sesuai pilihan tersedia (1-5)!')

                        break                 
                  break
            break

# menu kembali kemenu utama atau keluar
def exit():
      while True:
            print('''
                  (apakah anda telah selesai?)
                  1. Kembali ke Menu utama
                  2. Keluar  
   
                  ''')
            try:
                  menu_exit = int(input('Masukan angka menu (1/2)'))
                  if menu_exit == 1:     
                        main()                                                       
                  elif menu_exit == 2:                                                        
                        print ('Terima kasih telah berkunjung dan sehat selalu')
                        break
                        
            except:
                  print ('Tolong masukan angka sesuai pilihan tersedia (1/2)!')
                  
            break 

# menu utama
def main():
      while True:
            print('''
                              ####### HALO SELAMAT DATANG DI HYPE-RENTAL! ######
                  KAMI ADALAH PERUSAHAAN SEWA MENYEWA MOBIL-MOBIL BERKELAS DI JAKARTA
        


          
                  Log-in terlebih dahulu   
                  (Masuk sebagai apakah yang anda inginkan?)
                  1. Hanya Tampilkan Daftar Mobil
                  2. Penyewa Mobil 
                  3. Pemberi sewa Mobil 
                  4. Administrator (jika ingin update data)   
                  5. Keluar     
                  ''')
            try:
                  menu = int(input('Masukan angka menu!'))
                  if menu == 1:
                        read_data()                                           
                  elif menu == 2:
                        hapus_data()                                         
                  elif menu == 3:
                        create_data()                                         
                  elif menu == 4:
                        update_data()                                          
                  elif menu == 5:
                        exit()
                        break                                                 
                  else :
                        menu < 1 or menu > 5
                        main()
                                                                              
            except:
                  print ('Tolong masukan angka sesuai pilihan tersedia (1-5)!')


main()