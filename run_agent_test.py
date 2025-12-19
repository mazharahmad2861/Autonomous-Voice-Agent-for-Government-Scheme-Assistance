from src.agentic_hindi.agent import Agent

def main():
    agent = Agent(lang="hi")

    user_text = "मुझे सरकारी योजनाओं के लिए आवेदन करना है"

    user_info = {
        "name": "Rahul",
        "age": 28,
        "income": 220000,
        "state": "Bihar",
        "category": "OBC",
        "employment": "unemployed"
    }

    print("\n--- AGENT THINKING ---")
    response, matches = agent.handle_user(user_text, user_info)
    print(response)

    if matches:
        scheme_id = matches[0]["id"]
        print(f"\nApplying to scheme: {scheme_id}")

        result = agent.apply_scheme(scheme_id, user_info)
        print("\n--- APPLY RESULT ---")
        print(result)

if __name__ == "__main__":
    main()
