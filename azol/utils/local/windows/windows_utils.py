import ctypes
import ctypes.wintypes

def decrypt_dpapi(encrypted_data):

    buffer = ctypes.create_string_buffer(len(encrypted_data))
    buffer[:len(encrypted_data)] = encrypted_data

    # Call CryptUnprotectData
    class DATA_BLOB(ctypes.Structure):
        _fields_ = [("cbData", ctypes.wintypes.DWORD),
                    ("pbData", ctypes.POINTER(ctypes.c_char))]

    encrypted_blob = DATA_BLOB(len(encrypted_data), buffer)
    decrypted_blob = DATA_BLOB()

    result = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(encrypted_blob),
        None,
        None,
        None,
        None,
        0,
        ctypes.byref(decrypted_blob)
    )

    if not result:
        raise ctypes.WinError()

    # Extract the decrypted data
    decrypted_data = ctypes.string_at(decrypted_blob.pbData, decrypted_blob.cbData)
    ctypes.windll.kernel32.LocalFree(decrypted_blob.pbData)
    return decrypted_data.decode('utf-8')