if __name__ == '__main__':
   as_str = 'qwertyuioplkjhgfdsazxcvbnm0987654321'
   as_num = 79495849566202193863718934176854772085778985434624775545L
   num = int( as_str, 36 )
   assert num == as_num
   res = format( num, 36 )
   assert res == as_str
