import gradio as gr
import subprocess
import openai

# Set your API key
openai.api_key = "your-api-key-here"

# Function to convert user request to Linux command
def get_command(user_prompt):
    messages = [
        {"role": "system", "content": "You are a Linux assistant. Convert the user's instruction into a one-line Linux command. Do not explain."},
        {"role": "user", "content": user_prompt}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    return response.choices[0].message["content"].strip()

# Function to execute command
def automate_linux(task):
    try:
        linux_cmd = get_command(task)
        result = subprocess.getoutput(linux_cmd)
        return f"💡 Command: `{linux_cmd}`\n\n📤 Output:\n{result}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio UI
iface = gr.Interface(
    fn=automate_linux,
    inputs=gr.Textbox(label="Enter your Linux Task (e.g., 'Create folder test')"),
    outputs=gr.Textbox(label="Result"),
    title="🛠️ Linux Automation Assistant",
    description="Give natural language commands like 'make directory test' or 'show me the calendar', and it will run on your Linux system."
)

iface.launch()
