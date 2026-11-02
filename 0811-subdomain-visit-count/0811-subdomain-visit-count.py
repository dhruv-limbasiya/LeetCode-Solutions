class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts = {}
        for item in cpdomains:
            parts = item.split(" ")
            count = int(parts[0])
            domain = parts[1]
            
            pieces = domain.split(".")
            for i in range(len(pieces)):
                subdomain = ".".join(pieces[i:])
                if subdomain in counts:
                    counts[subdomain] += count
                else:
                    counts[subdomain] = count
                    
        result = []
        for domain, count in counts.items():
            result.append(str(count) + " " + domain)
            
        return result