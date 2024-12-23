import re
import math

class MemoryAnalyzer:
    def __init__(self):
        """
        Initialize pattern detection system with compiled regex patterns for sensitive data types
        """
        self.patterns = {
            'credit_card': re.compile(r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}'),
            'social_security': re.compile(r'\d{3}[-\s]?\d{2}[-\s]?\d{4}'),
            'api_key': re.compile(r'[A-Za-z0-9_\-]{32,}'),
            'session_token': re.compile(r'[A-Za-z0-9_\-]{16,}')
        }


    def scan_memory_dump(self, memory_data):
        """
        Analyze memory dump for sensitive data patterns.
        """
        findings = {'credit_card': [], 'social_security': [], 'api_key': [], 'session_token': []}

        for pattern_name, pattern in self.patterns.items():
            matches = pattern.findall(memory_data)
            if matches:
                findings[pattern_name].extend(matches)

        return findings

    def analyze_string_pool(self, strings):
        """
        Analyze string constants in memory, including pattern matching, deduplication, entropy analysis, and length-based analysis.
        """
        unique_strings = set(strings)
        findings = {'random_strings': [], 'pattern_matches': []}
        
        for string in unique_strings:
            for pattern_name, pattern in self.patterns.items():
                if pattern.match(string):
                    findings['pattern_matches'].append((pattern_name, string))
            
            entropy_score = self._calculate_entropy(string)
            if entropy_score > 4.5: 
                findings['random_strings'].append(string)
        
        return findings
    
    def generate_report(self, findings):
        """
        Generate secure report of findings, sanitize data, categorize findings, and assess risk.
        """
        sanitized_findings = {'credit_card': [], 'social_security': [], 'api_key': [], 'session_token': []}
        risk_assessment = {'high': [], 'medium': [], 'low': []}

        for category, matches in findings.items():
            for match in matches:
                sanitized_findings[category].append(self._sanitize_data(match))

        # Categorize findings by risk
        for category, matches in sanitized_findings.items():
            if category == 'credit_card':
                risk_assessment['high'].extend(matches)
            elif category == 'social_security':
                risk_assessment['high'].extend(matches)
            elif category == 'api_key':
                risk_assessment['medium'].extend(matches)
            elif category == 'session_token':
                risk_assessment['medium'].extend(matches)
        
        return {
            'sanitized_findings': sanitized_findings,
            'risk_assessment': risk_assessment
        }

    def _calculate_entropy(self, string):
        """
        Calculate the Shannon entropy of a string to assess randomness.
        """
        char_count = {}
        for char in string:
            char_count[char] = char_count.get(char, 0) + 1
  
        entropy = 0
        for count in char_count.values():
            prob = count / len(string)
            entropy -= prob * math.log2(prob) 
        
        return entropy

    def _sanitize_data(self, data):
        """
        Sanitize sensitive data for reporting (e.g., credit cards, social security).
        """
        return '*' * len(data)


memory_analyzer = MemoryAnalyzer()
memory_data = "Here is a credit card 1234-5678-9876-5432 and an API key AB12CD34EF56GH78IJ90KL12MN34OP56."
findings = memory_analyzer.scan_memory_dump(memory_data)
print("Scan Results:", findings)

strings = ["1234-5678-9876-5432", "AB12CD34EF56GH78IJ90KL12MN34OP56", "random_string_123"]
string_findings = memory_analyzer.analyze_string_pool(strings)
print("String Analysis Results:", string_findings)

report = memory_analyzer.generate_report(findings)
print("Report:", report)
