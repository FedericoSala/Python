import ldap

conn = ldap.initialize('ldap://host')
try:
    conn.simple_bind_s('user@domain', 'password')
except ldap.INVALID_CREDENTIALS:
    user_error_msg('wrong password provided')
