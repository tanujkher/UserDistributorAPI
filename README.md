# UserDistributorAPI
A simple API that validates a Users Login. Checks if the user is admin or not and provides the functionality of accessing, deleting, editing and adding records to User and Distributor array. Uses Flask-Restful APIs for reading and sending requests.

![ProjectFlow](./ssUserDistributorDetails/Projectflow.JPG)

## Entering Correct Password and Login(POST REQUEST)

![Login](./ssUserDistributorDetails/correctpass.JPG)

## Entering Wrong Password Error

![Login](./ssUserDistributorDetails/wrongpass.JPG)

## Post Request is Made to Login Resource to match Password

![Login](./ssUserDistributorDetails/correctpasspost.JPG)

## User Functions by Selecting U after Login

![Login](./ssUserDistributorDetails/functionsinuser.JPG)

## Using a Function

![Login](./ssUserDistributorDetails/usingafunction.JPG)

# Search Function(GET REQUEST)

## Search uses GET Request

![Login](./ssUserDistributorDetails/searchrequests.JPG)

## Search by Name

![Login](./ssUserDistributorDetails/searchbyname.JPG)

## Search All

![Login](./ssUserDistributorDetails/searchall.JPG)

## Searching Not Present

![Login](./ssUserDistributorDetails/searchingnotpresent.JPG)

# Adding New User(POST REQUEST)

## New User Created

![Login](./ssUserDistributorDetails/newuser.JPG)

## New User is Created by POST request

![Login](./ssUserDistributorDetails/newuserPOST.JPG)

# Edit User Details

![Login](./ssUserDistributorDetails/putreq.JPG)

## Trying to Edit non present user

![Login](./ssUserDistributorDetails/putrequestnon.JPG)

# Deleting User(DELETE REQUEST)

![Login](./ssUserDistributorDetails/deletinguser.JPG)

## Trying to delete non present user

![Login](./ssUserDistributorDetails/delnonpresent.JPG)

# Non Admin Trying to access Delete, Add and Edit Menu

![Login](./ssUserDistributorDetails/nonadminuseraccess.JPG)

### Non Admin user cann't Delete, Add and Edit User details or Distributor details just View them

# Distributor Menu

![Login](./ssUserDistributorDetails/distributormenu.JPG)

# Search in distributors(GET REQUEST)

![Login](./ssUserDistributorDetails/distributorfindall.JPG)

Similar to User search

# Adding distributor(POST REQUEST)

![Login](./ssUserDistributorDetails/addingdistributor.JPG)

# Extending distributor contract by changing created at to current time stamp(PUT REQUEST)

![Login](./ssUserDistributorDetails/extendingcontract.JPG)

## Trying to Extend Contract of Non Present User

![Login](./ssUserDistributorDetails/notpresentdis.JPG)

# Canceling Distributor Contract(DELETE REQUEST)

![Login](./ssUserDistributorDetails/cancelingcontract.JPG)

# When non Admin User tries to Edit, Delete or Add Distributor

![Login](./ssUserDistributorDetails/distributornotadmin.JPG)

Non Admin user can only view Distributor records not Edit, Delete or Add them