from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import configuration

url_driver = os.getcwd() + '\\driver\\chromedriver.exe'

#function to open file and make it as a list
def open_list(file) :
    with open(file, 'r') as f:
        list_item = f.readlines()
    list_item = [x.strip() for x in list_item]
    return list_item

#same like open_list() but with capability to process html
def open_list_utf(file) :
    with open(file, 'r',encoding='utf-8') as f:
        list_utf = f.readlines()
    list_utf = [x.strip() for x in list_utf]
    return list_utf

#look for content/ dir and make the list of all file
def list_folder_content() :
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

#change web url to admin path
def admin_url (url) :
    eurl = len(url) - 1
    if url[eurl] == '/' :
        r_url = url + 'wp-admin/'
    else:
        r_url = url + '/wp-admin/'
    return r_url

# function for enter admin-wp
def enter_admin_page (url,wp_user,wp_pass) :
    page_admin = admin_url(url)
    browser.get(page_admin)
    user = browser.find_element_by_id('user_login')
    password = browser.find_element_by_id('user_pass')
    submit = browser.find_element_by_id('wp-submit')
    user.send_keys(wp_user)
    password.send_keys(wp_pass)
    submit.click()
    # go to new-post page
    browser.get(page_admin + 'post-new.php')

# process for writing the content
def write_content(file,type=0) :
    # declare the element
    title = browser.find_element_by_id('title')
    sw_html = browser.find_element_by_id('content-html')
    content = browser.find_element_by_id('content')
    publish = browser.find_element_by_id('publish')

    # read the content file
    lines_of_content = open_list_utf('konten\\' + file)

    # The title
    if type == 1 :
        string_title = file.rpartition('.')
        the_title = string_title[0]
    else :
        the_title = lines_of_content[0]
    title.send_keys(the_title)

    # click mode html in editor
    sw_html.click()

    #writing the content
    for i in range(1, len(lines_of_content)):
        the_content = str(lines_of_content[i])
        content.send_keys( the_content + '\n')

    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(2)
    publish.click()
    time.sleep(2)

    #report the created post in result.txt
    result = browser.find_element_by_xpath('//*[@id="wp-admin-bar-view"]/a').get_attribute('href')
    with open('result.txt','a') as f :
        f.write(result + '\n')

    #delete content file that already use
    os.remove('konten\\'+ file )



##############################
# start the fun part
###########################

browser = webdriver.Chrome(url_driver)
browser.implicitly_wait(30)
list_url = open_list('web.txt')
web_count = len(list_url)
list_of_content = list_folder_content()

for x in range(web_count):
    enter_admin_page(list_url[x],def_user,def_pass)
    write_content(list_of_content[x],type_of_content)

browser.close()