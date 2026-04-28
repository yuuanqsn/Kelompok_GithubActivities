def inputnum(a):
    n=input(a)
    while not (n.isdigit() and isinstance(int(n), int)):
        print("[error] Input harus berupa angka! Coba lagi!")
        n=input(a)
    return int(n)
def cn(nt, nuts, nuas):
    return (0.3*nt) + (0.3*nuts) + (0.4*nuas)
def grade(nakhir):
    if nakhir>=85:print("( Grade A )")
    elif nakhir>=70:print("( Grade B )")
    elif nakhir>=60:print("(  Grade C )")
    else:print("( Grade D )")
def run():
    while True:
        print("\n====PROGRAM PENGHITUNG NILAI & GRADE SISWA====")
        nama=input("\nMasukkan Nama Siswa : ")
        nt=inputnum("\nMasukkan Nilai Tugas : ")
        nuts=inputnum("\nMasukkan Nilai UTS : ")
        nuas=inputnum("\nMasukkan Nilai UAS : ")
        print("\n=======REVIEW=======")
        print("Nama  : ", nama)
        print("\nNilai Tugas  : ", nt)
        print("Nilai UTS : ", nuts)
        print("Nilai UAS : ", nuas)
        nakhir=cn(nt, nuts, nuas)
        print("\nNilai Akhir : ", nakhir)
        grade(nakhir)
        print("\n--------------------")
        print("Apakah Anda ingin melanjutkan?")
        print("Ketik 1 untuk melanjutkan")
        print("Ketik 2 untuk selesai")
        loop=input("Pilih : ")
        if loop !="1":
            print("\n-------Selesai-------")
            break
run()