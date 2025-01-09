

# Agentic AI Series - Class 04

## **Introduction**

Welcome to Class 04 of the Agentic AI Series! In this session, we are building a Video Summarizer Agentic AI using Phidata and Google Gemini. By the end of this class, you will have a functional AI agent capable of summarizing videos and conducting supplementary web research.

---

## **Step 1: Setting Up the Environment**

1. **Create a folder named `Video Summarizer`** and open it with VS Code.

2. **Create and activate a Python environment.**

3. **Create `requirements.txt`**  
   Add the following libraries:
   ```plaintext
   streamlit
   phidata
   google-generativeai
   duckduckgo-search
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Step 2: Building `video_summarizer.py`**

1. Create a new file named `video_summarizer.py`.

2. Add the following code:

   ```python
   import streamlit as st 
   from phi.agent import Agent
   from phi.model.google import Gemini
   from phi.tools.duckduckgo import DuckDuckGo
   from google.generativeai import upload_file, get_file
   import google.generativeai as genai

   import time
   from pathlib import Path

   import tempfile

   from dotenv import load_dotenv
   load_dotenv()

   import os

   API_KEY = os.getenv("GOOGLE_API_KEY")
   if API_KEY:
       genai.configure(api_key=API_KEY)

   # Page configuration
   st.set_page_config(
       page_title="Multimodal AI Agent- Video Summarizer",
       page_icon="🎥",
       layout="wide"
   )

   st.title("Phidata Video AI Summarizer Agent 🎥🎤🖬")
   st.header("Powered by Gemini 2.0 Flash Exp")

   @st.cache_resource
   def initialize_agent():
       return Agent(
           name="Video AI Summarizer",
           model=Gemini(id="gemini-2.0-flash-exp"),
           tools=[DuckDuckGo()],
           markdown=True,
       )

   ## Initialize the agent
   multimodal_Agent = initialize_agent()

   # File uploader
   video_file = st.file_uploader(
       "Upload a video file", type=['mp4', 'mov', 'avi'], help="Upload a video for AI analysis"
   )

   if video_file:
       with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
           temp_video.write(video_file.read())
           video_path = temp_video.name

       st.video(video_path, format="video/mp4", start_time=0)

       user_query = st.text_area(
           "What insights are you seeking from the video?",
           placeholder="Ask anything about the video content. The AI agent will analyze and gather additional context if needed.",
           help="Provide specific questions or insights you want from the video."
       )

       if st.button("🔍 Analyze Video", key="analyze_video_button"):
           if not user_query:
               st.warning("Please enter a question or insight to analyze the video.")
           else:
               try:
                   with st.spinner("Processing video and gathering insights..."):
                       # Upload and process video file
                       processed_video = upload_file(video_path)
                       while processed_video.state.name == "PROCESSING":
                           time.sleep(1)
                           processed_video = get_file(processed_video.name)

                       # Prompt generation for analysis
                       analysis_prompt = (
                           f"""
                           Analyze the uploaded video for content and context.
                           Respond to the following query using video insights and supplementary web research:
                           {user_query}

                           Provide a detailed, user-friendly, and actionable response.
                           """
                       )

                       # AI agent processing
                       response = multimodal_Agent.run(analysis_prompt, videos=[processed_video])

                   # Display the result
                   st.subheader("Analysis Result")
                   st.markdown(response.content)

               except Exception as error:
                   st.error(f"An error occurred during analysis: {error}")
               finally:
                   # Clean up temporary video file
                   Path(video_path).unlink(missing_ok=True)
   else:
       st.info("Upload a video file to begin analysis.")

   # Customize text area height
   st.markdown(
       """
       <style>
       .stTextArea textarea {
           height: 100px;
       }
       </style>
       """,
       unsafe_allow_html=True
   )
   ```

---

## **Step 3: Configuring Google API**

1. Go to **Google AI Studio** and get your API key.

2. Create a file named `.env`.

3. Add the API Key as an environment variable:
   ```plaintext
   GOOGLE_API_KEY=""
   ```

---

## **Step 4: Running the Video Summarizer**

1. Run the following command in your terminal:
   ```bash
   streamlit run video_summarizer.py
   ```

2. Upload a video file and test it by writing a prompt like:
   ```plaintext
   Summarize the video and list the key points and also search the web about the topic that is mentioned in the video.
   ```

3. Click on **Analyze Video** to see the results.

---

## **Class Summary**

By the end of this class, you will have:

- Set up a video summarizer using Agentic AI.
- Built an interactive web application for video analysis and summarization.
- Integrated supplementary web research into the summarization process.

---

### **Notes**

- Ensure your API key is kept secure.
- Use a supported video format for analysis (`mp4`, `mov`, `avi`).

---

Happy coding! 😊