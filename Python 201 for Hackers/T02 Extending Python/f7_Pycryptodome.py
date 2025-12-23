"""
PyCryptodome – Ethical Hacking Oriented Demonstration Script

This script demonstrates:
1. Hashing (password analysis)
2. HMAC (API / token verification)
3. AES encryption (secure vs insecure usage)
4. RSA key generation (public/private key concepts)
5. Key Derivation (password storage security)
6. Secure random number generation

Use this ONLY in labs, CTFs, or authorized testing environments.
"""

# ===============================
# 1. HASHING – PASSWORD ANALYSIS
# ===============================

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Hash import SHA256, MD5

password = b"password123"

# Weak hashing example (MD5) – insecure
md5_hash = MD5.new(password).hexdigest()
print("[+] MD5 Hash (Weak):", md5_hash)

# Strong hashing example (SHA-256)
sha256_hash = SHA256.new(password).hexdigest()
print("[+] SHA256 Hash (Strong):", sha256_hash)

"""
Ethical hacking relevance:
- Identify weak hashing in databases
- Crack MD5/SHA1 faster
- Recommend stronger hashing + salting
"""

print("\n" + "="*50 + "\n")

# ===============================
# 2. HMAC – TOKEN / API SECURITY
# ===============================


secret_key = b"supersecretkey"
message = b"user=admin&role=admin"

# Create HMAC signature
hmac_obj = HMAC.new(secret_key, message, digestmod=SHA256)
signature = hmac_obj.hexdigest()

print("[+] HMAC Signature:", signature)

"""
Ethical hacking relevance:
- Understand API request signing
- Detect weak secret keys
- Attempt token forgery in bug bounties
"""

print("\n" + "="*50 + "\n")

# ===============================
# 3. AES – SYMMETRIC ENCRYPTION
# ===============================


# Generate random AES key (secure)
aes_key = get_random_bytes(16)

# Use EAX mode (secure: encryption + authentication)
cipher = AES.new(aes_key, AES.MODE_EAX)

plaintext = b"Sensitive malware config data"

ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("[+] AES Ciphertext:", ciphertext)
print("[+] AES Authentication Tag:", tag)

"""
Ethical hacking relevance:
- Malware config decryption
- Identify AES mode misuse (ECB is dangerous)
- Detect hardcoded keys & reused IVs
"""

# Decryption
cipher_dec = AES.new(aes_key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted_data = cipher_dec.decrypt_and_verify(ciphertext, tag)

print("[+] Decrypted AES Data:", decrypted_data)

print("\n" + "="*50 + "\n")

# ===============================
# 4. RSA – ASYMMETRIC ENCRYPTION
# ===============================


# Generate RSA key pair
rsa_key = RSA.generate(2048)

private_key = rsa_key.export_key()
public_key = rsa_key.publickey().export_key()

print("[+] RSA Public Key Generated")
print("[+] RSA Private Key Generated")

# Encrypt with public key
rsa_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
encrypted_msg = rsa_cipher.encrypt(b"Secret API key")

# Decrypt with private key
rsa_decipher = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted_msg = rsa_decipher.decrypt(encrypted_msg)

print("[+] RSA Decrypted Message:", decrypted_msg)

"""
Ethical hacking relevance:
- Detect weak RSA key sizes
- Identify exposed private keys
- Analyze incorrect padding usage
"""

print("\n" + "="*50 + "\n")

# ===============================
# 5. KEY DERIVATION – PASSWORD STORAGE
# ===============================


password = "password123"
salt = get_random_bytes(16)

derived_key = PBKDF2(
    password,
    salt,
    dkLen=32,
    count=100000  # Higher = harder to brute-force
)

print("[+] Derived Key using PBKDF2:", derived_key)

"""
Ethical hacking relevance:
- Audit password storage mechanisms
- Low iteration count = vulnerability
- Missing salt = critical issue
"""

print("\n" + "="*50 + "\n")

# ===============================
# 6. SECURE RANDOM – TOKENS & SESSIONS
# ===============================

secure_token = get_random_bytes(32)
print("[+] Secure Random Token:", secure_token)

"""
Ethical hacking relevance:
- Session hijacking prevention
- Password reset token testing
- Detect use of insecure random generators
"""

print("\n[✔] Script execution completed successfully.")
