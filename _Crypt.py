from math import log2

_size   = 32 #will define the Cryptographic method
_limit  = 15 #will define the maximum character-set
denum   = 1  #will be the decimal value of used key
rem_len = 0  #will be the length of binary reminder
que_len = 0  #will be the length of binary quetient

"""_____________________E_N_C_R_Y_P_T_I_O_N_____F_U_N_C_T_I_O_N_S__________________________"""

def break_rshift(msg):
      """Break the message into two parts and apply right shift on both"""
      half_len = round(len(msg)/2)
      part1 = msg[half_len-1]+msg[:half_len-1]
      part2 = msg[-1]+msg[half_len:-1]
      return part1+part2

def unival_bin(msg):
      """takes a msg then find unicode integer value for each
      character then format it into the UTF-8 binary form"""
      bin_msg,temp = '',''
      for char in msg:
            value = ord(char)
            bin_msg += reverse(mkform_UTF8(bin(value)[2:]))
      return complete_msg(bin_msg)

def divide(bin_str):
      """take a bin_str of set_size then divide it by the key"""
      global denum,rem_len,que_len
      num = int(bin_str,2)
      que = bin(num //denum)[2:]
      rem = bin(num % denum)[2:]
      return ('0'*(rem_len - len(rem))+rem)+ ('0'*(que_len - len(que))+que)

def bin_cipher(bin_str):
      """will take a bin string of size '_size+1' then return character for 20-20 chunks"""
      global _limit
      cipher = ''
      for i in range(0,len(bin_str),_limit):
            cipher += chr(int(bin_str[i:i+_limit],2))
      return cipher

"""_____________________D_E_C_R_Y_P_T_I_O_N_____F_U_N_C_T_I_O_N_S__________________________"""

def cipher_bin(cipher):
      """will return a binary string for cipher message"""
      global _size,_limit
      remaining = (_size+1)//_limit + 1
      bin_msg = ''
      for i in range(1,len(cipher)+1):
            binary = bin(ord(cipher[i-1]))[2:]
            if i%remaining == 0:
                  bin_msg += '0'*((_size+1)%_limit - len(binary)) + binary
            else:
                  bin_msg += '0'*(_limit - len(binary)) + binary
      return bin_msg

def multiply(bin_str):
      """will multiply the data with key to get real message"""
      global denum,_size,rem_len,que_len
      que  = int(bin_str[-que_len:],2)
      rem  = int(bin_str[: rem_len],2)
      rslt = bin(que * denum + rem)[2:]
      return '0'*(_size - len(rslt)) + rslt

def bin_unicode(bin_msg):
      """will give the real characters in original message"""
      global _size
      bin_msg = recover_msg(bin_msg)
      unicode_msg,binary,nxt = '','',0
      for i in range(len(bin_msg)-1,-1,-8):
            byte = bin_msg[i-7:i+1]
            tupl = deform_UTF8(byte,nxt)
            binary += reverse(tupl[0])
            nxt = tupl[1]
            if nxt<=0:
                  unicode_msg += chr(int(binary,2))
                  binary = ''
      return reverse(unicode_msg)

def break_lshift(msg):
      """will break the message and apply left shift
      on both parts It will return the actual message"""
      half_len = round(len(msg)/2)
      part1 = msg[1:half_len] + msg[0]
      part2 = msg[half_len+1:]+ msg[half_len]
      return part1+part2

"""__________________________O_T_H_E_R_____F_U_N_C_T_I_O_N_S______________________________"""

def set_technique(tech = 5):
      """will set the Cryptographic technique/method
      It will take the value from 4 to 8(16 to 256 bits)
      This function will Also define Your maximum key Length"""
      global _size
      key_size = 2**tech
      if log2(key_size) == int(log2(key_size)) and 16<=key_size<=256:
            _size = key_size
            if _size < 17:
                  global _limit
                  _limit = 11
            return True
      return False

def get_technique():
      """will return the Cryptographic method or Security level"""
      global _size
      return int(log2(_size))

def get_size():
      """will return the maximum possible value of key"""
      global _size
      return _size

def set_limit(limit):
      """will set the chunk size for bin2unicode and vice versa
      Here should be -> (2^technique and 10) < limit < 21"""
      global _size,uni_limit
      if 10 < limit < 21 and limit < _size:
            _limit = limit

def set_key(key):
      """will set the global values according to binary key"""
      global denum,_size,rem_len,que_len
      if 0 >= key >= 2**_size:
            raise "error"
      from math import ceil
      denum   = key
      rem_len = ceil(log2(denum))
      que_len = (_size+1) - rem_len
      return True

def mkform_UTF8(bnry):
      """Take a normal binary string then transform it in UTF-8 format"""
      l = len(bnry)
      if l<8:
            return ('0'    +'0'*( 7-l)+bnry)
      elif l<12:
            return ('110'  +'0'*(11-l)+bnry[:-6])  + ('10'+bnry[-6:])
      elif l<17:
            return ('1110' +'0'*(16-l)+bnry[:-12]) + ('10'+bnry[-12:-6])  + ('10'+bnry[-6:])
      elif l<22:
            return ('11110'+'0'*(21-l)+bnry[:-18]) + ('10'+bnry[-18:-12]) + ('10'+bnry[-12:-6])+('10'+bnry[-6:])

def deform_UTF8(bnry,nxt=0):
      """Take a UTF-8 string then transform it in normal Binary format"""
      if bnry[7]=='0':
            return bnry[:-1],0
      else:
            for i in range(6,2,-1):
                  if bnry[i]=='1':
                        continue
                  elif i == 6:
                        return bnry[:i],nxt-1
                  else:
                        return bnry[:i],6-i

def complete_msg(bin_msg):
      """complete the length of bin_str in multiple of crytographic technique"""
      global _size
      l = len(bin_msg)
      supply = _size - l%_size
      if l%_size == 0:
            return bin_msg + '110' + '0'*5
      else:
            return bin_msg + '0'*(supply) + '110' + '0'*(4-int(log2(supply//8))) + bin(supply//8)[2:]

def recover_msg(bin_msg):
      """will recover the appended binary msg completed with complete_msg()"""
      global _size
      appended = int(bin_msg[-6:],2)*8
      return bin_msg[:-appended-_size]

def reverse(_str):
      """will teke a binary string and return same sized reversed binary"""
      temp = ''
      for i in range(len(_str)):
            temp = _str[i] + temp
      return temp
