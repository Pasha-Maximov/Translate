from collections import Counter
pt = ""
ct = "rday m kagzs msq, qgxqd dqoquhqp eotaaxuzs uz ymftqymfuoe rday tue rmftqd, ita tmp fmwqz oagdeqe rday vmoan nqdzagxxu eayq kqmde qmdxuqd mf ftq gzuhqdeufk ar nmeqx. mdagzp ftq msq ar qustf, qgxqd ime eqzf fa xuhq mf tue ymfqdzmx sdmzpyaftqd'e tageq mzp qzdaxxqp uz ftq xmfuz eotaax uz nmeqx. uz mppufuaz, tq dqoquhqp bduhmfq fgfaduzs rday vatmzzqe ngdowtmdpf, m kagzs ftqaxasumz iuft m wqqz uzfqdqef uz ymftqymfuoe."
count = Counter(ct)
count.pop(" ")
print(count.most_common(3))
mostcommon = count.most_common(1)
mostcommon = mostcommon[0][0]
print (mostcommon)
difference = ord(mostcommon) - ord("e")

for letter in ct:
    if not letter in [".",","," "]:
        letter = chr((ord(letter) - 97 - (difference)) % 26 + 97)
    pt += letter
print(pt)
pt = ""


mostcommon = count.most_common(2)
mostcommon = mostcommon[1][0]
print (mostcommon)
difference = ord(mostcommon) - ord("e")

for letter in ct:
    if not letter in [".",","," "]:
        letter = chr((ord(letter) - 97 - (difference)) % 26 + 97)
    pt += letter
print(pt)
pt = ""


mostcommon = count.most_common(3)
mostcommon = mostcommon[2][0]
print (mostcommon)
difference = ord(mostcommon) - ord("e")

for letter in ct:
    if not letter in [".",","," "]:
        letter = chr((ord(letter) - 97 - (difference)) % 26 + 97)
    pt += letter
print(pt)