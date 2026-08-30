import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))

def analyze_code_and_generate_patch(vulnerability_title, vulnerable_code_snippet):
    """
    Passes vulnerable code extracted from the APK or API to AI.
    Returns AI security analysis and a recommended code patch.
    """
    prompt = f"""
    You are an AI Cyber Security Specialist.

    An automated scan detected:
    - Vulnerability: {vulnerability_title}
    - Snippet:
    ```
    {vulnerable_code_snippet}
    ```

    Tasks:
    1. Explain why this code/configuration is insecure in 2 sentences.
    2. Provide a secure code patch fix.
    """

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Fallback response if API key is not configured yet
        return f"AI Analysis Summary:\n{vulnerability_title} detected in source.\n\nRecommended Patch:\nReview component configuration and sanitize input parameters."
