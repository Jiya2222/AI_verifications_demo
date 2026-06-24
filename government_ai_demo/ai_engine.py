from ollama import chat
import json

def analyze_document(text):

    prompt = f"""
Return ONLY valid JSON.

{{
  "category":"",
  "priority":"",
  "summary":""
}}

Document:
{text}
"""

    response = chat(
        model="llama2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    sample_text = """
    Court hearing regarding land dispute.
    Appearance required within 7 days.
    """

    result = analyze_document(sample_text)

    print(result)