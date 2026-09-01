class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to hold the matching pairs
        matching_bracket = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If the character is an opening bracket
            if char in matching_bracket.values():
                stack.append(char)
            # If the character is a closing bracket
            elif char in matching_bracket:
                if not stack:
                    return False  # No opening bracket to match with
                pair = stack.pop()
                if pair != matching_bracket[char]:  # Check if the brackets match
                    return False
            else:
                # If it's not a bracket (optional, depending on the problem's constraints)
                continue
        
        # Check if all opening brackets have been matched
        return not stack