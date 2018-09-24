# autopbn Wordpress Auto Poster


##Private Blog Network Tools For Seo Practicioner


This Python program using selenium to automate new post in wordpress.
Its can be work in self hosted wordpress (wordpress.org)

The reason i buidling this software, is to help internet marketer or SEO Specialist to do their job, for maintaining tons of PBN blog that they have.

This program allow you to post in bulk domain at once.

##Requirements


### Python 3.++

Install python 3

### Selenium

You can install selenium with this command

``pip install selenium``



##Configuration


**Domain** : List your website/ domain in file `web.txt`

**Content** : Add your content in separate file in folder `/konten`


####Note


For content, default title will be first line in the file. 
if you want to change title as file name. Modify the code in `app.py` at this line of codes

`tulis_konten(list_konten[x])`

change with adding another paramaeter with value `1`. So the code will be look like this :

`tulis_konten(list_konten[x],1)`