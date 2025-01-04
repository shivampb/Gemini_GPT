
---

# **Generative AI ChatGPT App using Gemini Model**

## **Overview**
- This project is a local ChatGPT-style app built using the **Gemini large language model** via **Google Generative AI API**.
- The frontend is developed using **Streamlit**, providing an interactive user interface.
- The app allows users to input queries and receive AI-generated responses in real-time.
- A history feature is implemented to display past interactions in reverse order.

---

## **Features**
1. **Interactive User Interface**:  
   Built with Streamlit for a simple and clean user experience.

2. **AI-Powered Responses**:  
   Utilizes the **Gemini 2.0 flash-exp model** from Google Generative AI to generate responses.

3. **History Functionality**:  
   - Displays past queries and responses in reverse chronological order (latest query first).  
   - Retains interaction history during the session using `st.session_state`.

4. **Environment Variable Configuration**:  
   API key is securely managed using **python-dotenv**.

---

## **Technologies Used**
1. **Streamlit** – For building the user interface.
2. **Google Generative AI** – For using the Gemini large language model.
3. **Python-Dotenv** – For loading API keys from a `.env` file.

---

## **Installation Instructions**
1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Upgrade pip**:
   ```bash
   pip install --upgrade pip
   ```

4. **Install required packages**:
   ```bash
   pip install streamlit python-dotenv git+https://github.com/google/generative-ai-python
   ```

5. **Create a `.env` file**:
   ```bash
   touch .env  # On macOS/Linux
   echo GOOGLE_API_KEY=your_actual_api_key_here > .env
   ```

---

## **Usage**
1. **Run the Streamlit app**:
   ```bash
   streamlit run your_script_name.py
   ```

2. **Enter a query** in the text input field and click **"Generate Response"**.
3. View the generated response along with the history of past interactions.

---

## **File Structure**
- `app.py`: Main script containing the Streamlit app.
- `.env`: File to store the Google API key securely.
- `requirements.txt`: List of dependencies (optional if using virtual environment).
  
---

## **Future Enhancements**
1. Add support for more AI models.
2. Implement user authentication for personalized history.
3. Enhance the UI/UX with better styling.
4. Add export functionality for interaction history.

---
