# Last updated: 10/14/2026, 6:26:28 PM
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.lower()
            name,domain=s.split('@')
            return name[0]+"*****"+name[-1] + "@"+domain
        else:
            digits = ""
            for ch in s:
                if ch.isdigit():
                    digits +=ch
            last_four = digits[-4:]
            country_code = len(digits)-10
            if country_code == 0:
                return "***-***-"+last_four
            else:
                return "+"+"*"* country_code + "-***-***-"+last_four
        