def calculator(a: float, b: float, operation: str):
    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

    return "Error: Invalid operation"


from ddgs import DDGS


def web_search(query: str, max_results: int = 5):
    try:
        max_results = max(1, min(int(max_results), 5))

        results = DDGS().text(
            query,
            max_results=max_results
        )

        return [
            {
                "title": item.get("title", ""),
                "url": item.get("href", ""),
                "snippet": item.get("body", "")
            }
            for item in results
        ]

    except Exception as error:
        return {
            "error": f"Web search failed: {error}"
        }

if __name__ == "__main__":
    results = web_search(
        "Latest developments in AI agents"
    )

    for result in results:
        print(result)