s = "ABBBABABBBAABBBBABBA"
pref_s = [0] * (len(s) + 1)

for i in range(len(s)):
    pref_s[i + 1] = pref_s[i]
    if s[i] == 'A':
        pref_s[i + 1] += 1
    else:
        pref_s[i + 1] -= 1

print(pref_s)
d = {}
m = 0
for i in range(len(pref_s)):
    if pref_s[i] not in d:
        d[pref_s[i]] = i
    else:
        diff = i - d[pref_s[i]]
        m = max(m, diff)

print(m)
