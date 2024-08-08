from web3 import Web3
import hashlib
import uuid

def uuid_to_hex(uuid_str):
    uuid_obj = uuid.UUID(uuid_str)
    return uuid_obj.hex

def format_for_ethereum(hex_value, length):
    if len(hex_value) > length:
        return hex_value[:length]
    return hex_value.zfill(length)

local_node_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(local_node_url))

if not web3.is_connected():
    print("Falha ao conectar à rede Ethereum")
    exit()

uuid_address = "060c11ff-4955-4167-b3ed-d1891094c991"
uuid_private_key = "e7a731a7-eda2-488b-ab2c-15b531baf30f"

ethereum_address = format_for_ethereum(uuid_to_hex(uuid_address), 40)
ethereum_private_key = format_for_ethereum(uuid_to_hex(uuid_private_key), 64)

def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.digest()  # Retornar bytes diretamente

def sign_message(message_bytes, private_key):
    account = web3.eth.account.from_key(private_key)
    message_hash = Web3.solidity_keccak(['bytes32'], [message_bytes])
    signed_message = account.signHash(message_hash)
    return signed_message

def verify_signature(message_bytes, signature, account_address):
    message_hash = Web3.solidity_keccak(['bytes32'], [message_bytes])
    recovered_address = web3.eth.account._recover_hash(
        message_hash, signature=signature
    )
    return recovered_address.lower() == account_address.lower()

file_path = "test.txt"

file_hash = calculate_file_hash(file_path)
print(f"Hash do arquivo: {file_hash.hex()}")

signed_file = sign_message(file_hash, ethereum_private_key)
print(f"Assinatura: {signed_file.signature.hex()}")
print(f"Hash da mensagem: {web3.to_hex(Web3.solidity_keccak(['bytes32'], [file_hash]))}")

is_valid = verify_signature(file_hash, signed_file.signature, ethereum_address)
print(f"A assinatura é válida: {is_valid}")
