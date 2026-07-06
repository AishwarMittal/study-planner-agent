import os
import asyncio
from dotenv import load_dotenv

# This line reads your API key from the .env file
load_dotenv()

from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

# -------------------------------------------------------
# CREATING THE AGENT
# Think of this as giving the AI its "job description"
# -------------------------------------------------------
root_agent = Agent(
    name="study_planner",
    model="gemini-2.5-flash",
    description="An agent that creates personalized study plans for students",
    instruction="""
    You are a friendly and helpful study planner agent for students.
    
    When a student tells you a subject and their exam date:
    - Calculate how many days they have left
    - Create a detailed, realistic day-by-day study plan
    - Break each day into specific topics to study
    - Keep it encouraging and motivating
    
    When they ask follow-up questions, adjust the plan as needed.
    Always be supportive and specific.
    """
)

# App settings
APP_NAME = "study_planner_app"
USER_ID = "student_001"

# -------------------------------------------------------
# MAIN FUNCTION — this runs when you type: python main.py
# -------------------------------------------------------
async def main():
    # Create a session (like opening a new conversation)
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID
    )

    # Create the runner (this is what actually runs the agent)
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    print("=" * 50)
    print("   STUDY PLANNER AGENT - Ready to help!")
    print("=" * 50)
    print("Tell me your subject and exam date.")
    print("Example: 'I have a Math exam on July 25'")
    print("Type 'quit' to exit.\n")

    # This loop keeps the conversation going
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Good luck with your studies!")
            break

        if not user_input.strip():
            continue
            

        # Package the user's message in the format ADK expects
        message = types.Content(
            role='user',
            parts=[types.Part(text=user_input)]
        )

        # Send message to agent and get response
        print("Agent: ", end="", flush=True)

        async for event in runner.run_async(
            user_id=USER_ID,
            session_id=session.id,
            new_message=message
        ):
            if event.is_final_response():
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            print(part.text)
                            print()

# Run the program
if __name__ == "__main__":
    asyncio.run(main())