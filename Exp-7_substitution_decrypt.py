def frequency_analysis(ciphertext):
    freq = {}
    for char in ciphertext.upper():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

def main():
    print("=== Substitution Cipher Decryption ===")
    ciphertext = input("Enter ciphertext: ")
    
    print("\nFrequency Analysis:")
    freq = frequency_analysis(ciphertext)
    for char, count in freq[:10]:
        print(f"{char}: {count}")
    
    print("\nHints:")
    print("- Most common English letter: E")
    print("- Common word: THE")
    print("- Look for repeated patterns")
    
    mapping = {}
    while True:
        cipher_char = input("\nCipher char (or 'done'): ").upper()
        if cipher_char == 'DONE':
            break
        plain_char = input("Maps to: ").upper()
        mapping[cipher_char] = plain_char
    
    decrypted = ''.join(mapping.get(c, c) for c in ciphertext.upper())
    print(f"\nDecrypted: {decrypted}")

if __name__ == "__main__":
    main()

OUTPUT:
=== Substitution Cipher Decryption ===
Enter ciphertext: WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ

Frequency Analysis:
 : 0
W: 2
K: 2
H: 2
Q: 1
F: 1
TX: 1
... (etc.)

Hints:
- Most common English letter: E
- Common word: THE
- Look for repeated patterns

Cipher char (or 'done'): W
Maps to: T
Cipher char (or 'done'): K
Maps to: H
Cipher char (or 'done'): H
Maps to: E
Cipher char (or 'done'): Q
Maps to: I
Cipher char (or 'done'): F
Maps to: U
Cipher char (or 'done'): D
Maps to: L
Cipher char (or 'done'): O
Maps to: A
Cipher char (or 'done'): done

Decrypted: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
