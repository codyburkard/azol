import ctypes
import ctypes.wintypes
import os
import json

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
    return decrypted_data

def get_azure_cli_credential_file_contents():
    os_name = os.name
    home_directory = os.path.expanduser ("~")
    azure_directory = home_directory + "/.azure"
    msal_file = azure_directory + "/msal_token_cache.bin"
    #throw exception if directory doesnt exist
    if not os.path.isdir(azure_directory):
        raise Exception("Could not find an Azure CLI directory in the user's home directory")
    dir_contents = os.listdir(azure_directory)
    if not os.path.isfile(msal_file):
        raise Exception("msal_token_cache not found in the user's .azure directory")
    fp = open(msal_file, "rb")
    contents = fp.read()
    fp.close()
    if os_name == "nt":
        contents = decrypt_dpapi(contents).decode('utf-8')
    return json.loads(contents)
