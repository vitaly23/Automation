# Automation
selinium &amp; jMeter test cases.

In this project I was asked to create 10 test cases on a website of my choice , I chose the HR management mock-up web site: https://opensource-demo.orangehrmlive.com/
The test I have made are as follows:

1.	Login test – which tests the login with the credentials as as arguments.
2.	Performance test – tests a few drop downs and links 
3.	Table info test – tests extraction from a table, gathering data about the users and printing them into the logger file.
4.	Scroll down test – tests the scroll down inside the web page.
5.	Add entitlements – filling out a form and submitting it.
6&7. Testing of a few links in the web site including some more dropdowns.
8. Logout test – testing the logout function on the web site
9. Original website test – testing an external link to the real website.
10. https request using JMeter – I tested the congestion on the website,
using 100 threads to access the webpage and asserting the 200 OK reply.


If I had access to the sites data base and requirements (e.g no special characters in the username)
I would also test the register function with an input test and validation of the login using the database of the {‘username’ : password}.
All the functions in the main class include an output log to a logger whether it failed or succeeded,
furthermore I made the code to run asynchronically  with simple locks (acquire and release functions)
so the tests won’t interfere one another.
