import vigenere
import string

CIPHERTEXT = 'NLZBTHMPSPFYMGPIYPIZRRZJPHMAWGSIXCXYLVSPVWNOCSYWFBEIKSZJ' \
    'EMHBUMNGZFOMHUVTJZTNBKOYSEIRDQAQQUYEQSNIGVSPKIYHSYFEWGYEICEBXZOAUXJODMN' \
    'USNDSIUEBXXCJVVNCQNAMSNIXCHSYLMDNIEOSLHWMEHRPNHLNBWBGFACWNBMPSYRANCQHTB' \
    'IEVEIRZZGIHHIINUZXXVHVKPZHSYFIRRTIIHCYLXSPKXJHSYHXWAZSIGZZFIBXZRYFPKNQF' \
    'RJXCOENAMMFYSPZOXXKZNIIOVPWTCGRJACWNBBUDRCXCSXNHBVRJIKOCUMQCA'

if vigenere.index_of_coincidence(CIPHERTEXT, 10) != 0.075:
    print("index_of_coincidence(CIPHERTEXT, 10) != 0.075")


if vigenere.guess_key_length(CIPHERTEXT) != 10:
    print("guess_key_length(CIPHERTEXT) != 10")

if vigenere.guess_caesar_key('DXVHZDNVRDXJILPZMZY') != 'V':
    print("guess_caesar_key('DXVHZDNVRDXJILPZMZY') != 'V'")
if vigenere.guess_caesar_key('JUUPJDURBMRERMNMRWCXCQANNYJACB') != 'J':
    print("guess_caesar_key('JUUPJDURBMRERMNMRWCXCQANNYJACB') != 'J'")
    
if vigenere.guess_vigenere_key(CIPHERTEXT) != 'REVOLUTION':
    print("guess_vigenere_key(CIPHERTEXT) != 'REVOLUTION'")

if vigenere.decrypt_file('AliceInWonderland') != 'THROUGHTHELOOKINGGLASS':
    print("decrypt_file('AliceInWonderland') != 'THROUGHTHELOOKINGGLASS'")
with open('AliceInWonderland-decrypted.txt', 'r') as f:
    s = f.read()
start = s[:25]
end = s[-6:]
if start != 'CHAPTERIDOWNTHERABBITHOLE' or end != 'THEEND':
    print("Alice in Wonderland was not decrypted correctly")


if vigenere.decrypt_file('JekyllAndHyde') != 'ROBERTLOUISSTEVENSON':
    print("decrypt_file('JekyllAndHyde') != 'ROBERTLOUISSTEVENSON'")
with open('JekyllAndHyde-decrypted.txt', 'r') as f:
    s = f.read()
start = s[:5]
end = s[-44:]
if start != 'STORY' or end != 'IBRINGTHELIFEOFTHATUNHAPPYHENRYJEKYLLTOANEND':
    print("Jekyll and Hyde was not decrypted correctly")


if vigenere.decrypt_file('PrideAndPrejudice1') != 'JANEAUSTEN':
    print("decrypt_file('PrideAndPrejudice1') != 'JANEAUSTEN'")
with open('PrideAndPrejudice1-decrypted.txt', 'r') as f:
    s = f.read()
start = s[:33]
end = s[-15:]
if start != 'ITISATRUTHUNIVERSALLYACKNOWLEDGED' or end != 'VISITINGANDNEWS':
    print("Pride And Prejudice was not decrypted correctly")
