# Email_sender

A django app that send emails to multiple receipiants

# Project idea

<p>Automate the process of sending emails with some customized features based on business requirements. You can have a list of email addresses and their respective names. Then you can modify the message and send emails to the target audience automatically.</p>

# Automation

<h3> Emails Table</h3>

- must have a list of users with there email addresses
<table>
<tr><td>email_id</td></tr>
<tr><td>name</td></tr>
<tr><td>email</td></tr>
</table>

<h3> Subscriptions</h3>

<table>
<tr><td>Subscriction_id</td></tr>
<tr><td>subscription_name</td></tr>
</table>

<h3> Subscribers</h3>

<table>
<tr><td>Subscriber_id</td></tr>
<tr><td>email<small bg-color='blue'><button>(1:1)</button></small></td></tr>
<tr><td>Subscriction_id <small bg-color='blue'><button>FK</button></small></td></tr>
</table>

<h1>Email Form</h1>

- get the subscription type
- the subject of the email
- the message
- cc self checkbox
