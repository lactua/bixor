# Install
* Linux
    > python3 -m pip install bixor
* Windows
    > python -m pip install bixor

# Author

**Discord** : *Lactua#1806*

**Github**: *[https://github.com/lactua](https://github.com/lactua)*

# Documentation
    
* ## Encrypt
    
    To encrypt a string with Bixor, you need in a first time import bixor.
        
        import bixor
    
    Encryption needs a **key**, and a **content**. The key allows you to decrypt the content in the future, it's like a password to get acces to your content.

    To encrypt you have to call the function **encrypt** and put the content and the key in parameters.

    Example :
        
        content = 'hello'
        key = 'world'

        encrypted = encrypt(content, key)

        print(encrypted)
    
    Output :

        1111110 1011100 1001010 1100011 1111001

* ## Decrypt
    To encrypt a string with Bixor, you need in a first time import bixor.
    
        import bixor
    
    Decryption needs a **key**, and an **encrypted binary**. The key allows you to decrypt the encrypted binary.

    To decrypt you have to call the function **decrypt** and put the encrypted binary and the key in parameters.

    Example :
        
        encrypted_binary = '1111110 1011100 1001010 1100011 1111001'
        key = 'world'

        decrypted = encrypt(encrypted_binary, key)

        print(decrypted)
    
    Output :

        hello
    