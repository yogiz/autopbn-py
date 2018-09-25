# Autopbn - Wordpress Auto Poster


## Bulk PBN Domain Auto Poster with Python


This Python program using selenium to automate new post in wordpress.
Its can be work in self hosted wordpress (wordpress.org)

The reason i buidling this software, is to help internet marketer or SEO Specialist to do their job, for maintaining tons of PBN blog that they have.

This program allow you to post in bulk domain at once.

## Requirements

You must install all of the requirement in your computer

### Python 3.++

Install python 3

### Selenium

You can install selenium with this command

``pip install selenium``


Now you ready to run this app. But first, setup your campaign.

## Configuration

To starts your campain you must make setup first. Follow the step below:

**Adding Domain and Content**
 
*Domain* : List your website/ domain in file `web.txt`

*Content* : Add your content in separate file in folder `/konten`


**Open the *connfiguration.py* file in your editor**

Then setup the user and password for access wp-admin. *(All domain must have same  user and pass)*


### result

As for the result of this task, the app will report to you the list of url that he already created in `result.txt`