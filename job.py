import requests
SCORING_ENDPOINT = "https://scoring-7f3a.a.run.app/predict"   # consumes (== svc-aurora provides)
for r in rows(): requests.post(SCORING_ENDPOINT, json=r)
