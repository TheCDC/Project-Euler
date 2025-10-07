from collections import Counter
from itertools import product
from pathlib import Path

plain1 = """
<p>Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.</p>
<p>A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.</p>
<p>For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.</p>
<p>Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.</p>
<p>Your task has been made easy, as the encryption key consists of three lower case characters. Using <a href="resources/documents/0059_cipher.txt">0059_cipher.txt</a> (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.</p>


"""

# plain1 = "catthehat"
key1 = "hat"
guess1 = "the"
dictionary = {
    "the",
    "has",
    "of",
    "so",
    "is",
    "to",
    "use",
    "from",
    "that",
    "then",
    "code",
    "using",
}


def keys():
    options = "abcdefghijklmnopqrstuvqxyz"
    for p in product(options, repeat=3):
        yield "".join(p)


def xor_string(a: str, b: str) -> list[str]:
    if len(a) != len(b):
        raise ValueError(f"{a=}!={b=}")
    return list(chr(ord(aa) ^ ord(bb)) for aa, bb in zip(a, b))


def cipher(plain: str, key: str) -> list[str]:
    key2 = key
    if len(key) < len(plain):
        diff = len(plain) - len(key)
        key2 = key + key * (diff // len(key)) + key[: diff % len(key)]
    return xor_string(plain, key2)


def v1():
    count = Counter()
    cipher1 = cipher(plain1, key1)
    # print(xor_string(guess1,cipher1))
    for i in range(len(cipher1)):
        s = cipher1[i : i + len(guess1)]
        try:
            ss = xor_string(guess1, s)
            count.update(["".join(ss)])
            print(ss)
        except ValueError:
            pass
    print(count.most_common())


def v2():
    count = Counter()
    cipher1 = cipher(plain1, key1)
    print(cipher1)
    # deciphered = cipher(cipher1,"hat")
    # print(''.join(deciphered))
    # quit()
    for index, key_guess in enumerate(keys()):
        if index % 10000 == 0:
            print(index, key_guess)
        deciphered = "".join(cipher(cipher1, key_guess))
        for word in dictionary:
            c = deciphered.count(word)
            count.update({key_guess: c})
    print(count.most_common(10))
    key = count.most_common(10)[0][0]
    print(cipher(cipher1, key))


def v3():
    count = Counter()

    target = Path(__file__).parent / "files" / "0059_cipher.txt"
    with open(target) as f:
        ciphered = list(chr(int(i)) for i in f.read().split(","))
    print(cipher)
    for index, key_guess in enumerate(keys()):
        if index % 10000 == 0:
            print(index, key_guess)
        deciphered = "".join(cipher(ciphered, key_guess))
        for word in dictionary:
            c = deciphered.count(word)
            count.update({key_guess: c})
    print(count.most_common(10))
    key = count.most_common(10)[0][0]
    plaintext_deciphered = "".join(cipher(ciphered, key))
    print(plaintext_deciphered)
    print(key, sum(ord(c) for c in plaintext_deciphered))


def v4():
    count = Counter()

    target = Path(__file__).parent / "files" / "0059_cipher.txt"
    with open(target) as f:
        ciphered = list(chr(int(i)) for i in f.read().split(","))
    print(cipher)
    for index, key_guess in enumerate(keys()):
        if index % 10000 == 0:
            print(index, key_guess)
        deciphered = "".join(cipher(ciphered, key_guess))
        c = deciphered.count(r"\x")
        count.update({key_guess: c})
    least_common = list(reversed(count.most_common()))
    print(least_common[:10])
    key = least_common[0][0]
    plaintext_deciphered = "".join(cipher(ciphered, key))
    print(plaintext_deciphered)
    print(key, sum(ord(c) for c in plaintext_deciphered))


def main():
    v3()


if __name__ == "__main__":
    main()
