class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        # Check IPv4
        if "." in queryIP:
            parts = queryIP.split(".")

            if len(parts) != 4:
                return "Neither"

            for part in parts:
                if not part:
                    return "Neither"

                # No leading zeros
                if len(part) > 1 and part[0] == "0":
                    return "Neither"

                # Only digits allowed
                if not part.isdigit():
                    return "Neither"

                # Must be between 0 and 255
                if int(part) < 0 or int(part) > 255:
                    return "Neither"

            return "IPv4"

        # Check IPv6
        elif ":" in queryIP:
            parts = queryIP.split(":")

            if len(parts) != 8:
                return "Neither"

            for part in parts:
                if not part or len(part) > 4:
                    return "Neither"

                # Only hexadecimal characters allowed
                for char in part:
                    if char not in "0123456789abcdefABCDEF":
                        return "Neither"

            return "IPv6"

        return "Neither"