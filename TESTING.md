#  **Testing**

Back to [README.md](README.md)

View live site [here.]()

![Main Site Image](docs/readme_items/responsive_img.png)

# 
The site has been tested using Google Chrome, Mozilla Firefox and Microsoft Edge on desktop/laptop as well as Chrome on Android mobile. The Google Developer tool has been used to check the sites responsiveness across various screen sizes (desktop, tablet, mobile).
# 

## **User Story Testing**

**Viewing and Navigation**
  - As a shopper:
    - I wish to navigate the site intuitively
        - The navigation bar is displayed clearly and is easy to understand taking the user to where they expect to be in the site
        - ![navigation](docs/readme_items/screenshots/navigation.png)
        - The Account dropdown menu displays differently according to a users access
        - ![sign in dropdown](docs/readme_items/screenshots/sign_in_dropdown.png)
          ![dropdown, admin](docs/readme_items/screenshots/account_dropdown.png)
          ![dropdown, standard user](docs/readme_items/screenshots/account_dropdown2.png)

        - Clicking on the logo takes the user back to the Home page
        - Buttons are clearly defined and uniform throughout, also giving visual feedback to the user when hovered over or clicked on
        - ![buttons1](docs/readme_items/screenshots/buttons1.png) ![buttons2](docs/readme_items/screenshots/buttons2.png)

    - I wish to get visual feedback on completion of all actions
        - Toast messages are displayed to show:
            - Success 
            - Error
            - Info
            - Warning
            - ![toast success](docs/readme_items/screenshots/toast_success.png) ![toast error](docs/readme_items/screenshots/toast_error.png)
        - Validation messages display on all forms

    - I wish to view all products clearly so that I can choose what to buy
        - Products are clearly displayed and if an item is sold out, a badge displays on the product image to indicate that
        - ![products](docs/readme_items/screenshots/products.png)
    - I wish to view full product information of a specific product, including the product image, description, price, sizes (if any)
        - Product information clearly displayed including an indicator of stock quantity when low
        - ![product detail](docs/readme_items/screenshots/product_detail.png)
    - I wish to easily see my basket total to see how much I am spending
        - Basket total is displayed under the basket icon in the top right corner of every page and is updated with each new item added
        - ![basket total](docs/readme_items/screenshots/basket_total.png)

**Registration and User Accounts**
  - As a site user:
    - I wish to create an account to store my order history and personal details including shipping address for future purchases
      - A user register for an account by clicking Register in the dropdown menu top right of the page
      - ![register](docs/readme_items/screenshots/sign_in_dropdown.png)
      - The user is taken to a Sign Up form; when they click Sign Up, a message informs that a confirmation email was sent to them asking them to confirm their email address; the link takes the user to the Confirm Email Address page.
      - ![verify email](docs/readme_items/screenshots/sign_up.png)
    - I wish to easily log in so that I can access my profile and manage my personal details
      - A user can log in from the dropdown menu. Once logged in they can select My Profile from the same dropdown menu which takes them to the Profile page. There they can update their personal information, including delivery address, and also view their Order History
      - ![my account](docs/readme_items/screenshots/account_dropdown2.png) ![profile](docs/readme_items/screenshots/profile.png)
    - I wish to easily log out when I have finished using the site
      - A user can click Logout in the My Account dropdown which takes them to a confirmation page
      - ![sign out confirmation](docs/readme_items/screenshots/sign_out.png)
    - I wish to be able to request a password reset via email in case of have forgotten it
      - A user can click Forgot Password? in the Sign Up page. This will take them to a page asking them to enter their email address. When they recieve the email, they must click the link in the email which takes them to a page where they can enter a new password; clicking on the Change Password button then takes them to a confirmation page telling them the password was successfully changed. After that the can sign in like usual
      - ![password reset 1](docs/readme_items/screenshots/password_reset.png) ![password reset 2](docs/readme_items/screenshots/password_reset2.png) ![password reset 3](docs/readme_items/screenshots/password_reset3.png) ![password reset 4](docs/readme_items/screenshots/password_reset4.png)

**Purchasing and Checkout**
  - As a shopper:
    - I wish to purchase items as a guest so that I can checkout without having to create an account
      - A guest user can purchase items without registering
    - I wish to be able to easily add items, update quantity, or remove items in the basket before checkout
      - The item quantity can be adjusted in the Product Detail page
      - The basket can be updated with items added, quantity adjusted or items removed before checkout
      - Visual feedback is given for any changes made via toast messages
      - ![basket](docs/readme_items/screenshots/basket_anon.png) ![basket updated toast](docs/readme_items/screenshots/toast_basket_updated.png)
    - I wish to be confident that my payment and personal information are secure during the checkout process
      - Stripe is used to handle all card payments on this site. Stripe is certified to PCI Service Provider Level 1, which is the most stringent level of certification available in the payments industry. All card numbers are encrypted with AES-256 (Advanced Encryption Standard - 256 bits), and decryption keys are stored on separate machines.
    - I wish to be able to easily enter my payment information
      - The place to enter payment information is clearly labelled along with the personal information and shipping address form
      - ![checkout form](docs/readme_items/screenshots/checkout_form.png)
    - I wish be able to view a summary of my order at checkout before completing my purchase
      - An order summery is displayed in the Checkout with a link to amend the order if necessary which takes the user back to the Basket page
      - ![checkout summary](docs/readme_items/screenshots/checkout_summary.png)
    - I wish to recieve a confirmation email for my purchase showing the order details so I can be confident the purchase has been made successfully
      - A confirmation email is sent to the user when they have clicked Complete Order in the checkout. A toast message is displayed telling the user that the email has been sent
      - ![confirmation email](docs/readme_items/screenshots/email_conf_anon.png)

**Admin and Store Management**
  - As the Store Owner:
    - I wish to be able to easily add new products to my store
      - As admin/superuser, a store owner can access Product Management where they can view a list of all products add new products
      - ![product management](docs/readme_items/screenshots/product_manage.png) ![add product](docs/readme_items/screenshots/product_add.png) ![preview added product](docs/readme_items/screenshots/product_add_preview.png)
    - I wish to be able to easily view and edit products to update their details or quantity information
      - A store owner can view and edit products by clicking the edit link either in the product detail page or in the product list in Product Management
      - ![edit product](docs/readme_items/screenshots/product_edit.png)
    - I wish to be able to delete products that I no longer wish to sell in my store
      - a product can be deleted via the button in the Edit Product page. A confirmation modal appears to prevent accidental deletion of a product
      - ![delete product](docs/readme_items/screenshots/product_delete_warn.png)



[Back to top](#testing)

#
## **Validator testing:**
### **HTML - [W3C Validator](https://bit.ly/3vkSIx1)** - *passed*
  - Home
    - ![html home]()
  - Gallery
    - ![html gallery]()
  - Shop
    - ![html shop]()
  - Products
    - ![html products]()
  - Product Details
    - ![html product details]()
  - Basket
    - ![html basket]()
  - Checkout
    - ![html checkout]()
  - Profile
    - ![html profile]()
  - Product Management - Add Product
    - ![html add product]()
  - Product Management - Edit Product
    - ![html edit product]()

#
### **CSS - [(Jigsaw) validator](https://bit.ly/3F29Zg1)** - *returned no errors*
  - Home
    - ![css home](docs/readme_items/screenshots/css_home.png)
  - Gallery
    - ![css gallery](docs/readme_items/screenshots/css_gallery.png)
  - Shop
    - ![css shop](docs/readme_items/screenshots/css_shop.png)
  - Products
    - ![css products](docs/readme_items/screenshots/css_products.png)
  - Product Details
    - ![css product details](docs/readme_items/screenshots/css_product_detail.png)
  - Basket
    - ![css basket](docs/readme_items/screenshots/css_basket.png)
  - Checkout
    - ![css checkout](docs/readme_items/screenshots/css_checkout.png)
  - Profile
    - ![css profile](docs/readme_items/screenshots/css_profile.png)
  - Product Management - Add Product
    - ![css add product](docs/readme_items/screenshots/css_product_add.png)
  - Product Management - Edit Product
    - ![css edit product](docs/readme_items/screenshots/css_product_edit.png)
  

#
### **Javascript - [JSHint](https://bit.ly/3jRVMKH)** - *returned no errors*
  - Product image
    - ![js product image](docs/readme_items/screenshots/js_product_image.png)
  - Product qunatity
    - ![js product quantity](docs/readme_items/screenshots/js_product_quantity.png)
  - Basket
    - ![js basket](docs/readme_items/screenshots/js_basket.png)
  - Country fields
    - ![js countryfields](docs/readme_items/screenshots/js_countryfields.png)
  - Checkout/Stripe Payments
    - ![js checkout](docs/readme_items/screenshots/js_checkout.png)

#
### **Python - [Pep8](https://bit.ly/3qXj7hD)** - *passed*

[Back to top](#testing)

#
## **Additional testing:**
Black box testing was also carried out on the final deployed website.
    
All tests passed. Results can be viewed [here]()

#
## **Bugs**

**Found and corrected**

**No known bugs left unfixed**

[Back to top](#testing)