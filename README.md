# Email_sender

A django app that send emails to multiple receipiants

# Project idea

<p>Automate the process of sending emails with some customized features based on business requirements. You can have a list of email addresses and their respective names. Then you can modify the message and send emails to the target audience automatically.</p>

# Automation

-- Emails Table

- must have a list of users with there email addresses
<table>
<tr><td>email_id</td></tr>
<tr><td>name</td></tr>
<tr><td>email</td></tr>
</table>

-- Subscriptions

<table>
<tr><td>Subscriction_id</td></tr>
<tr><td>subscription_name</td></tr>
</table>

-- Subscribers

<table>
<tr><td>Subscriber_id</td></tr>
<tr><td>email</td></tr>
<tr><td>Subscriction_id<button>fk</button></td></tr>
</table>
