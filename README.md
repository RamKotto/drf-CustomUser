<h1>drf-CustomUser</h1>
<h2>API for CustomUser</h2>

<h3>User registration</h3>
<p><e>POST /rest-auth/registration/</e></p>
<br>
{
  "email": "test@test.com",
  "password1": "ujmik,ol.",
  "password2": "ujmik,ol."
}

<p>This will send out verification email with account confirmation URL looking like this: <br>
/accounts-rest/registration/account-confirm-email/MQ:1iU6Li:17ruSRLybL38zXvc91no26v2YGw/</p>
