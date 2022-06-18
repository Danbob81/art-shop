<h1 align="center"><strong>Art Shop</strong></h1>

View live site [here.](https://danbob81-art-shop.herokuapp.com/)

![Main Site Image](docs/readme_items/responsive_img.png)

# **User Experience (UX)** 

## **Brief**
Local artist Lindsey Higginson wishes to showcase and sell her artwork online. She requires a website that will enable her to do just that. The site is to be clean and modern looking and needs to accept online credit card payments. It also needs the facility to easily update, add and remove items within the shop if/when required.


#
## **User Stories**

**Viewing and Navigation**
  - As a shopper:
    - I wish to navigate the site intuitively
    - I wish to get visual feedback on completion of all actions
    - I wish to view all products clearly so that I can choose what to buy
    - I wish to view full product information of a specific product, including the product image, description, price, sizes (if any)
    - I wish to easily see my basket total to see how much I am spending

**Registration and User Accounts**
  - As a site user:
    - I wish to create an account to store my order history and personal details including shipping address for future purchases
    - I wish to easily log in so that I can access my profile and manage my personal details
    - I wish to easily log out when I have finished using the site
    - I wish to be able to request a password reset via email in case of have forgotten it

**Purchasing and Checkout**
  - As a shopper:
    - I wish to purchase items as a guest so that I can checkout without having to create an account
    - I wish to be able to easily add items, update quantity, or remove items in the basket before checkout
    - I wish to be confident that my payment and personal information are secure during the checkout process
    - I wish to be able to easily enter my payment information
    - I wish be able to view a summary of my order at checkout before completing my purchase
    - I wish to recieve a confirmation email for my purchase showing the order details so I can be confident the purchase has been made successfully

**Admin and Store Management**
  - As the Store Owner:
    - I wish to be able to easily add new products to my store
    - I wish to be able to easily view and edit products to update their details or quantity information
    - I wish to be able to delete products that I no longer wish to sell in my store

[Back to top](#user-experience-ux)

#
## **Design**
### **Colour Scheme:**
  - Monochromatic black and white scheme with the only colour coming from the logo, artwork images in the gallery and shop products.

### **Typography:**
  - Google Fonts
    - Main text - [Raleway](https://fonts.google.com/share?selection.family=Raleway)

### **Imagery**
  - [Font Awesome](https://bit.ly/3tfSjJN) used for icons throughout
  - [Canva](https://bit.ly/3Ol5jGJ) was used to create the logos in the header and footer of the site
  - Images in the Welcome, Gallery and Originals section of the shop are scans of original artworks by Lindsey Higginson
  - Images in the Prints and Merchandise sections of the shop are from [RedBubble](https://rdbl.co/3xHi7Ro)


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

**All users:**
  - Header, to display consistently throughout, containing:
    - logo
    - main nav and mobile nav showing:
      - Home
      - Gallery
      - Shop - with dropdown menu linking to:
        - Prints
        - Originals
        - Merchandise
    - Sign In/My Account - with dropdown menu linking to:
      - Product Management (admin/superuser only)
      - My Profile
      - Sign Out
    - Basket - showing the basket total cost when items are in the basket
  - Welcome page featuring an image and 'about me' text with external link to Instagram
  - Gallery page featuring images of artwork
  - Shop page featuring links to three products pages for:
    - Prints
    - Originals
    - Merchandise
  - Products pages displaying products which link to:
    - Product details page displaying the individual products information and options to choose quantity and size if available, and add to basket
  - Shopping basket page displaying items in the basket with basket subtotal and options to update quantity or remove item. Also links to Checkout or back to Shop
  - Checkout displaying item(s), a form to enter information including shipping address, payment section and Complete Order button
  - Order confirmation page displaying the order information for purchase immediately made
  - Profile page displaying logged in users information, with ability to amend their information, and order history
  - Log out redirects user back to home page
  - Footer, to display consistently throughout, featuring a disclaimer, copyright and social media links

**Admin/Superuser only:**
  - Product Management page displaying list of all products, links to Edit Product page, and Add Product form
  - Edit Product page displaying a preview of the product being edited and a form to edit the product, which includes option to delete the product also

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
  - sqlite3 in Django development environment
  - PostgreSQL in deployment

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