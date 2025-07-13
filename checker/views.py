import requests
from django.shortcuts import render

def check_plagiarism(request):
    report = None
    if request.method == "POST":
        user_text = request.POST.get("text", "")
        api_url = "https://api.gowinston.ai/v2/plagiarism"
        headers = {
            "Authorization": f"Bearer <API_KEY>",  # Replace with your actual API key
            "Content-Type": "application/json",
        }
        payload = {
            "text": user_text,
            "language": "en",
            "country": "us"
        }

        resp = requests.post(api_url, json=payload, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            score = data.get("result", {}).get("score", "N/A")
            sources = data.get("sources", [])
            lines = [f"Plagiarism Score: {score}%\n"]
            for src in sources:
                lines.append(f"- {src.get('title')} ({src.get('url')}): {src.get('plagiarismWords')} words")
            report = "\n".join(lines)
        else:
            report = f"Error: {resp.status_code} {resp.text}"

    return render(request, "index.html", {"result": report})

