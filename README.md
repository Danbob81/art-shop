<h1 align="center"><strong>Art Shop</strong></h1>

View live site [here.]()

![Main Site Image]()

# **User Experience (UX)** 

## **Brief**



#
## **User Stories**


[Back to top](#user-experience-ux)

#
## **Design**
### **Colour Scheme:**
  - 

### **Typography:**
  - Google Fonts

### **Imagery**


### **Wireframes**

Wireframes for desktop, tablet and mobile views created using Balsamiq.

PDF links here:
  - [Desktop]()
  - [Tablet]()
  - [Mobile]()

[Back to top](#user-experience-ux)

#
## **Features**

### **Implemented**


### **Future features**


[Back to top](#user-experience-ux)

#
## **Database Design**


![Entity Relationship Diagram]()

(created using LucidChart - [link](https://bit.ly/3qHI00n))

[Back to top](#user-experience-ux)

#
## **Technologies Used**

### **Languages:**
  - HTML 5
  - CSS 3
  - Javascript (JQuery)
  - Python

### **Frameworks, libraries and programmes:**
  - 
  - JQuery - for JS functions
  - Pip - to install required dependencies
  - Git & Github - for version control and code storing
  - Balsamiq - for wireframes
  - LucidChart - for entity relationship diagram
  - Heroku - to deploy live site

### **Database Technologies**
  - 
  - 

### **Workspace**
  - Gitpod - VSCode based virtual IDE

[Back to top](#user-experience-ux)

#
## **Testing**

Chrome Developer Tool was used to simulate the different viewport sizes for desktop and laptop views, tablet views and mobile views. I used this throughout the development process as well as for testing the website once it was deployed to Heroku.

The deployed website was also tested using Chrome, Edge and Firefox as well as on mobile (using Chrome for Android)

More detailed information of the testing carried out can be viewed in [TESTING.md]()

[Back to top](#user-experience-ux)

#
## **Deployment**

### **Site deployed to Heroku**

**Requirements for Deployment:**
  - Python
  - MongoDB account and database
  - GitHub account
  - Heroku account

**Process:**


**Deployment to Heroku:**
  - create requirements.txt file and Procfile by running these commands in terminal:
    - `pip3 freeze --local > requirements.txt`
    - `echo web: python run.py > Procfile`
  - push to repository
  - create .gitignore file if you don't already have one
  - add `env.py` and `__pycache__/` to the .gitignore file and save it. Sensitive information will now not be added to your repository
  - create env.py file with the following information:
    - `import os`

    - `os.environ.setdefault("IP", "0.0.0.0")`
    - `os.environ.setdefault("PORT", "5000")`
    - `os.environ.setdefault("SECRET_KEY", " ## YOUR SECRET_KEY ## ")`
    - `os.environ.setdefault("MONGO_URI", " ## YOUR MONGO_URI ## ")`
    - `os.environ.setdefault("MONGO_DB", " ## YOUR MONGO_DBNAME ## ")`
  
  - log in to [Heroku](https://bit.ly/3HqWiYV)
  - select 'Create New App' in the dashboard
  - choose your app name, select the region nearest you and click 'Create App'
  - go to 'Deploy' tab, 'Deployment Method' and select 'GitHub'
  - search for your GitHub repo and click 'Connect'
  - go to 'Settings' tab, 'Config Vars' and select 'Reveal Config Vars'
  - enter key value pairs from your env.py file
  - go to 'Deploy' tab and select 'Enable Automatic Deployment'
  - choose the branch to deploy from
  - click 'Deploy Branch' to deploy your app onto Heroku servers
  - let app finish building then click 'Open App' to view your site

[Back to top](#user-experience-ux)

#
## **Credits**

### **Content:**
-

### **Code:**
  - 
  -  
  - 
 
### **Media:**
- 

### **Acknowledgements:**
- 

[Back to top](#user-experience-ux)
#