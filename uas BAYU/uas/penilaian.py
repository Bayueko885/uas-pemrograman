import texttable as tt
def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []

    x = [[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == 'y'):
        print("\n======================================")
        nama.append(input("\n\tMasukkan Nama: "))
        nim.append(input("\tMasukkan Nim: "))
        tugas = int(input("\tNilai Tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("\tNilai UTS: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("\tNilai UAS: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("\n\tTambah data [y/n]? ")

    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header(['No','Nama','Nim','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'])
    print(tab.draw())
