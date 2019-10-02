from _Crypt import *

class Encryption:
      method,message,_key,_cipher = 0,'','',''
      def __init__(self,method= 5,message='',key=''):
            self.set_all(method,message,key)

      def set_all(self,method,message,key):
            self.set_method(method)
            self.set_message(message)
            self.set_key(key)

      def set_method(self,method = 5):
            if set_technique(method):
                  self.method = method
            else:
                  print('Invalid method it should be (4<= method <=8) {default = 5}')

      def set_message(self,message):
            self.message = message

      def append_message(self,append_string):
            self.message += append_string
            
      def set_key(self,key):
            if set_key(key):
                  self._key = key
            else:
                  raise 'Invalid Key, It should be valued 0< key <(2^(technique))'

      def set_limit(self,limit):
            set_limit(limit)

      def Encrypt(self,technique=0, message='', key=''):
            if technique == 0  : technique=self.method
            if message   == '' : message = self.message
            if key       == '' : key = self._key
            self.set_all(technique,message,key)
            _size          = get_size()
            _right_shift   = break_rshift(message)        #break and right shift the message
            _binary_msg    = unival_bin(_right_shift)     #UTF-8 formed binary of unicode value 
            _divided_bin   = ''                           #will hold the divided binary values(sized=_size+1)
            self._cipher   = ''                           #will hold the characters after encryption
            for i in range(0,len(_binary_msg),_size):     #divides the message chunk by chunk
                  temp_bin_str = _binary_msg[i:i+_size]
                  _divided_bin += divide(temp_bin_str)
            for i in range(0,len(_divided_bin),_size+1):  #will create the cipher text of _size+1 bit chunks
                  temp_bin_str = _divided_bin[i:i+_size+1]
                  self._cipher += bin_cipher(temp_bin_str)
            return self._cipher

class Decryption:
      method,cipher,_key,_message = 0,'','',''
      def __init__(self,method= 5,cipher='',key=''):
            self.set_all(method,cipher,key)

      def set_all(self,method,cipher,key):
            self.set_method(method)
            self.set_cipher(cipher)
            self.set_key(key)

      def set_method(self,method = 5):
            if set_technique(method):
                  self.method = method
            else:
                  print('Invalid method it should be (4<= method <=8) {default = 5}')

      def set_cipher(self,cipher):
            self.cipher = cipher
            
      def set_key(self,key):
            if set_key(key):
                  self._key = key
            else:
                  return 'Invalid Key, It should be valued 0< key <(2^(technique))'

      def set_limit(self,limit):
            set_limit(limit)

      def Decrypt(self,method=0,cipher='',key=''):
            if method == 0  : method = self.method
            if cipher == '' : cipher = self.cipher
            if key    == '' : key = self._key
            self.set_all(method,cipher,key)
            _size = get_size()
            _cipher_bin = cipher_bin(cipher)
            _mul_byte = ''
            self._message = ''
            for i in range(0,len(_cipher_bin),_size+1):
                  byte = _cipher_bin[i:i+_size+1]
                  _mul_byte += multiply(byte)
            _bin_unicode  = bin_unicode(_mul_byte)
            self._message = break_lshift(_bin_unicode)
            return self._message

