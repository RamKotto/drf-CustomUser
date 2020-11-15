<h1>drf-CustomUser</h1>
<h2>API for CustomUser</h2>

<h3>User registration</h3>
<p><em>POST /rest-auth/registration/</em></p>
<br>
<pre>{
  "email": "test@test.com",
  "password1": "ujmik,ol.",
  "password2": "ujmik,ol."
}</pre>

<p>This will send out verification email with account confirmation URL looking like this: <br>
/accounts-rest/registration/account-confirm-email/MQ:1iU6Li:17ruSRLybL38zXvc91no26v2YGw/</p>
<hr>
<hr>
<h3>User login</h3>
<p>Login is denied before user confirms his email.</p>
<p><em>POST /rest-auth/login/</em></p>
<br>
<pre>{
  "email": "test@test.com",
  "password": "ujmik,ol."
}</pre>
<hr>
<hr>
<h3>User logout</hr>
<p><em>POST /rest-auth/logout/</em></p>
<hr>
<hr>
<h3>Password change</h3>
<p>User must be logged in to change password</p>
<p><em>POST /rest-auth/password/change/</p></em>
<pre>{
  "new_password1": ".lo,kimju",
  "new_password2": ".lo,kimju"
}</pre>
<hr>
<hr>
<h3>Currently logged in user</h3>
<p><em>GET /rest-auth/user/</em></p>
<hr>
<hr>
