# Test Cases — Demo Web Shop

**Tested site:**  
https://demowebshop.tricentis.com/

---

## TC-01 Successful new account registration

**Preconditions:**
- User is on the main page
- User does not use an already registered email

**Steps:**
1. Click “Register” in the top right corner
2. Choose gender
3. Enter first name
4. Enter last name
5. Enter email
6. Enter password
7. Confirm password
8. Click “Register”

**Expected Result:**
- User is redirected to a page with a successful registration message
- Account is created successfully
- User is logged in

---

## TC-02 Registration with empty “First name” field

**Preconditions:**
- User is on the main page

**Steps:**
1. Click “Register”
2. Choose gender
3. Leave “First name” empty
4. Enter last name
5. Enter email
6. Enter password
7. Confirm password
8. Click “Register”

**Expected Result:**
- Account is not created
- Error message is displayed near “First name” field

---

## TC-03 Log in with an incorrect password

**Preconditions:**
- User is registered
- User is logged out
- User is on the main page

**Steps:**
1. Click “Log in”
2. Enter registered email
3. Enter incorrect password
4. Click “Log in”

**Expected Result:**
- User is not logged in
- Error message “The password is incorrect” is displayed

---

## TC-04 Successful log in

**Preconditions:**
- User is registered
- User is logged out
- User is on the main page

**Steps:**
1. Click “Log in”
2. Enter registered email
3. Enter correct password
4. Click “Log in”

**Expected Result:**
- User is redirected to the main page
- User is logged in successfully

---

## TC-05 Product search

**Preconditions:**
- User is on any page of the site

**Steps:**
1. Enter “book” in the search field
2. Click the search button

**Expected Result:**
- Search results page is displayed
- Products related to “book” are shown
