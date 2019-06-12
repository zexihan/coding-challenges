"""
String
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            emailConverted = self.convert(email)
            emailSet.add(emailConverted)
        return len(emailSet)

    def convert(self, str):
        local, domain = str.split('@')
        local = local.replace('.', '')
        local = local.split('+')[0]
        return local + '@' + domain
