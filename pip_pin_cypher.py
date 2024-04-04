#Pig_Pin cypher python implementation amateur
def pigpen_cipher(message):
    # Define the pigpen cipher key
    pigpen_key = {
        'A': '🞂', 'B': '🞃', 'C': '🞁', 'D': '🞄',
        'E': '🞀', 'F': '🞅', 'G': '🞉', 'H': '🞇',
        'I': '🞁', 'J': '🞈', 'K': '🞄', 'L': '🞃',
        'M': '🞁', 'N': '🞅', 'O': '🞀', 'P': '🞉',
        'Q': '🞂', 'R': '🞈', 'S': '🞄', 'T': '🞃',
        'U': '🞀', 'V': '🞂', 'W': '🞅', 'X': '🞉',
        'Y': '🞇', 'Z': '🞈',
        ' ': ' '
    }

    encoded_message = ""
    
    # Encode each character of the message
    for char in message:
        # If the character is a letter, look up its corresponding pigpen symbol
        if char.upper() in pigpen_key:
            encoded_message += pigpen_key[char.upper()]
        else:
            # If the character is not a letter, keep it unchanged
            encoded_message += char

    return encoded_message

# Get user input
user_input = input("Enter the message to encode using Pigpen Cipher: ")

# Encode the user input using Pigpen Cipher
encoded_message = pigpen_cipher(user_input)

# Print each step of the encoding process
print("\nStep-by-step encoding process:")
print("--------------------------------")
print("Original Message:", user_input)
print("Encoded Message: ", encoded_message)
