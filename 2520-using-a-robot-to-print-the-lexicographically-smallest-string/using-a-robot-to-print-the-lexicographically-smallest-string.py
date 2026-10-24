class Solution:
    def robotWithString(self, s: str) -> str:
        cnt, t, p = Counter(s), [], []

        for ch in s:
            t.append(ch)

            if cnt[ch] == 1:
                del cnt[ch]
            else:
                cnt[ch] -= 1

            while cnt and t and min(cnt) >= t[-1]:
                p+=t.pop()
        
        p += t[::-1]
        return ''.join(p)

