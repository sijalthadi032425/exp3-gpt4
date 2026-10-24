import os
from datetime import datetime

from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import generate_summary

def main():
    print("="*50)
    print("        Intelligent Email Assistant (CLI)        ")
    print("="*50)

    # 1. User Input
    print("\n--- 1. Input Details ---")
    customer_name = input("Enter Customer Name: ")
    subject = input("Enter Subject: ")
    print("Enter Customer Email (Press Enter twice to finish):")
    
    email_lines = []
    while True:
        line = input()
        if not line:
            break
        email_lines.append(line)
    customer_email = "\n".join(email_lines)

    print("\n[Input Summary]")
    print(f"Name: {customer_name}")
    print(f"Subject: {subject}")
    print(f"Email:\n{customer_email}")

    if not customer_email.strip():
        print("Error: Email content cannot be empty.")
        return

    # 2. Intent Detection
    print("\n--- 2. Intent Detection ---")
    print("Detecting intent...")
    intent = detect_intent(customer_email)
    print(f">> Detected Intent: {intent}")

    # 3. Retrieval
    print("\n--- 3. Similar Email Retrieval ---")
    print("Searching historical records...")
    prev_email, prev_reply = retrieve_similar_email(customer_email)
    if prev_email and prev_reply:
        print(f">> Most Similar Past Email:\n{prev_email}")
        print(f"\n>> Previous Reply:\n{prev_reply}")
    else:
        print(">> No similar emails found in the database.")
        prev_reply = "Please write a polite response addressing the customer's issue."

    # 4. Reply Generation
    print("\n--- 4. AI Reply Generation ---")
    print("Generating professional reply...")
    generated_reply = generate_reply(customer_email, prev_reply)
    print("\n>> Generated Reply:")
    print("-" * 40)
    print(generated_reply)
    print("-" * 40)

    # 5. Tone Improver
    print("\n--- 5. Tone Improver ---")
    tone_choice = input("Do you want to change the tone? [friendly/formal/empathetic/none]: ").strip().lower()
    
    if tone_choice in ['friendly', 'formal', 'empathetic']:
        print(f"Rewriting in {tone_choice} tone...")
        generated_reply = improve_tone(generated_reply, tone_choice)
        print("\n>> Updated Reply:")
        print("-" * 40)
        print(generated_reply)
        print("-" * 40)

    # 6. Summary
    print("\n--- 6. Conversation Summary ---")
    print("Generating summary...")
    summary = generate_summary(customer_email)
    print("\n>> Summary:")
    print(summary)

    # 7. Save
    print("\n--- 7. Save Reply ---")
    save_choice = input("Do you want to save this conversation? (y/n): ").strip().lower()
    if save_choice == 'y':
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_dir = os.path.join(os.path.dirname(__file__), 'outputs')
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'generated_reply.txt')
        
        content = f"Date: {date_str}\n"
        content += f"Intent: {intent}\n"
        content += f"Customer Email:\n{customer_email}\n\n"
        content += f"Generated Reply:\n{generated_reply}\n"
        content += "-" * 40 + "\n"
        
        with open(output_file, 'a') as f:
            f.write(content)
            
        print(f">> Conversation saved to {output_file}")
    
    print("\nProcess Complete. Thank you!")

if __name__ == '__main__':
    main()
