from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

url_driver = os.getcwd() + '\\driver\\chromedriver.exe'

#buka list website
def buka_list(file) :
    with open(file, 'r') as f:
        list_web = f.readlines()
    list_web = [x.strip() for x in list_web]
    return list_web

def buka_utf(file) :
    with open(file, 'r',encoding='utf-8') as f:
        list_utf = f.readlines()
    list_utf = [x.strip() for x in list_utf]
    return list_utf

def lihat_folder_konten() :
    # detect the current working directory
    path = os.getcwd() + "\\konten"
    isi_dir = []
    # read the entries
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            # print all entries that are files
            if entry.is_file():
                isi_dir.append(entry.name)

    return isi_dir

# merubah url menjadi url admin
def admin_url (url) :
    eurl = len(url) - 1
    if url[eurl] == '/' :
        r_url = url + 'wp-admin/'
    else:
        r_url = url + '/wp-admin/'
    return r_url

# func untuk masuk ke admin (user pass udah di definisikan sama)
def masuk_admin (url) :
    hal_admin = admin_url(url)
    browser.get(hal_admin)
    user = browser.find_element_by_id('user_login')
    password = browser.find_element_by_id('user_pass')
    submit = browser.find_element_by_id('wp-submit')
    user.send_keys('admin')
    password.send_keys('demonk1ng')
    submit.click()
    # masuk ke add new post
    browser.get(hal_admin + 'post-new.php')

# proses publis konten
def tulis_konten(file,type=0) :
    # variabel yang di perlukan di halaman post new
    title = browser.find_element_by_id('title')
    sw_html = browser.find_element_by_id('content-html')
    konten = browser.find_element_by_id('content')
    publish = browser.find_element_by_id('publish')

    #baca file konten dengan fungsi buka list mode utf
    list_baris_konten = buka_utf('konten\\' + file)

    # Tulis title
    if type == 1 :
        string_title = file.rpartition('.')
        isi_title = string_title[0]
    else :
        isi_title = list_baris_konten[0]
    title.send_keys(isi_title)

    # Klik mode html di WP editor
    sw_html.click()

    #tulis kontennya
    for i in range(1, len(list_baris_konten)):
        isi_konten = str(list_baris_konten[i])
        konten.send_keys( isi_konten + '\n')

    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(1)
    publish.click()
    # time.sleep(10)
    #report url hasil create ke file hasil.txt
    hasil = browser.find_element_by_xpath('//*[@id="wp-admin-bar-view"]/a').get_attribute('href')
    with open('hasil.txt','a') as f :
        f.write(hasil + '\n')


##############################
# MULAI SKRIPNYA
###########################

browser = webdriver.Chrome(url_driver)
browser.implicitly_wait(30)
list_url = buka_list('web.txt')
banyak_web = len(list_url)
list_konten = lihat_folder_konten()

for x in range(banyak_web):
    masuk_admin(list_url[x])
    tulis_konten(list_konten[x])

browser.close()