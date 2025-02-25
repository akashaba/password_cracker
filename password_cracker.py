import hashlib

def crack_sha1_hash(hash, use_salts = False):
  pwd = open('top-10000-passwords.txt', 'r')
  
  if use_salts:
    slt = open('known-salts.txt', 'r')
    for x in pwd:
      slt.seek(0)
      for y in slt:
        salt = y.strip()
        digest = hashlib.sha1(bytes(salt + x.strip() + salt, 'utf-8')).hexdigest()
        if digest == hash:
          return x
          
  else:
    for x in pwd:
      digest = hashlib.sha1(bytes(x, 'utf-8')).hexdigest()
      if digest == hash:
        return x
        
  return "PASSWORD NOT IN DATABASE"
