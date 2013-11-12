class NameDescriptor(object):

    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
		ucase_name = value.upper()
		instance._value = ucase_name

    def __delete__(self, instance):
        del(instance._value)

	def __len__(self, instance):
		return len(instance._value)
	


class Person(object):
	
	name = NameDescriptor()

		
		
if __name__ == '__main__':
	n = Person()
	n.name = 'Brent'
	n.hat = 'bowler'
	print(dir(n))
	print(vars(n))
	print(n.name)
	print(n.hat)
	print(len(n.name))
	