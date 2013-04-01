#!/usr/bin/env python
#
# [SNIPPET_NAME: Facade]
# [SNIPPET_CATEGORIES: Patterns]
# [SNIPPET_DESCRIPTION: Demonstrates using a facade pattern.]
# [SNIPPET_AUTHOR: Evan Briones <evan_time@hotmail.com>]
# [SNIPPET_LICENSE: GPL]

# http://en.wikipedia.org/wiki/Facade_pattern

'''A Facade is an abstract of another interface.
This example uses a Facade to simplify the Account class.
Giving a much easier to use interface.
'''

class Account:
	def __init__(self, user, passwd, role, name, email):
		self._user = user 
		self._passwd = passwd
		self._role = role
		self._name = name
		self._email = email
		self._attempts = 0
	
	def get_role(self):
		return self._role

	def set_role(self, role):
		self._role = role

	def get_user(self):
		return self._user
	
	def get_password(self):
		return self._passwd

	def set_password(self, newpass):
		self._passwd = newpass

	def check_password(self, passwd):
		if self._passwd == passwd:
			self._attempts = 0
			return True
		else:
			self._attempts += 1
			return False

	def get_name(self):
		return self._name

	def get_email(self):
		return self._email

	def set_email(self, email):
		self._email = email

	def get_attempts(self):
		return self._attempts


# This facade makes dealing with accounts simple.
# With for simple operations (create,view,update,delete)
class AccountFacade:
	def __init__(self, max_attempts, default_role):
		self._accounts = {}
		self._max_attempts = max_attempts
		self._default_role = default_role
		
	# Provides an interface to create an account.
	def create_account(self, user, passwd, name, email):
		if user in self._accounts:
			print "This user already exists."		
			return

		account = Account(user, passwd, self._default_role, name, email)
		self._accounts[user] = account
		
	# Provides an interface that displays 
	# The details of the account class are hidden.
	# (like: password checking, password attempts)
	def view_account(self, user, passwd):
		if user not in self._accounts:
			print "Account does not exist."
			return

		account = self._accounts.get(user)
		if account.get_attempts() > self._max_attempts:
			print "Too many password attempts."
			return

		if not account.check_password(passwd):
			print "Password is incorrect."
			return

		print "User: " + account.get_user()
		print "Password: " + account.get_password()
		print "Role: " +  account.get_role()
		print "Name: " + account.get_name()
		print "Email: " + account.get_email()
		print
		
	# Provides an interface for updating account.
	# This hides all the complexity of the Account class.
	def update_account(self, user, passwd, newrole, newpass, newemail):
		if user not in self._accounts:
			print "Account does not exist."
			return

		account = self._accounts.get(user)
		if account.get_attempts() > self._max_attempts:
			print "Too many password attempts."
			return
		
		if not account.check_password(passwd):
			print "Password is incorrect."
			return

		if newpass != "":
			print "Your password was changed."
			account.set_password(newpass)

		if newrole != "":
			print "Your role was changed."
			account.set_role(newrole)

		if newemail != "":
			print "Your email address was changed."
			account.set_email(newemail)

	# Provides an interface for removing an account
	def delete_account(self, user, passwd):
		if user not in self._accounts:
			print "Account does not exist."
			return

		account = self._accounts.get(user)			
		if account.get_attempts() > self._max_attempts:
			print "Too many password attempts."
			return
			
		if not account.check_password(passwd):
			print "Password is incorrect."
			return
		
		del self._accounts[user]
		print "Account was deleted."
		
# Example Use of a Facade
if __name__ == '__main__':
	facade = AccountFacade(3, "user")
	
	facade.create_account("joe120", "12ab345", "joe", "joe120@joe120.com")
	facade.view_account("joe120", "12ab345")

	facade.update_account("joe120", "12ab345", "admin",
		"ab123", "admin@joe120.com")
	facade.view_account("joe120", "ab123")

	facade.delete_account("joe120", "ab123")
	facade.view_account("joe120", "ab123")

