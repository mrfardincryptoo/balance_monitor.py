def get_mock_balance(address):
    # Simulated balance check
    balance_map = {
        "0x123...": 0.5,
        "0xabc...": 2.1
    }
    return balance_map.get(address, 0.0)

test_address = "0xabc..."
print(f"Address {test_address} Balance: {get_mock_balance(test_address)} ETH")
