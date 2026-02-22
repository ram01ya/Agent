# import ollama
# import json

# tasks = []

# def add_task(task: str):
#     tasks.append(task)
#     return f"Task added: {task}"

# def list_tasks():
#     if not tasks:
#         return "No tasks added yet"
    
#     result = ""
#     for i, task in enumerate(tasks, 1):
#         result += f"{i}. {task}\n"
    
#     return result

# def delete_task(task):
#     if task not in tasks:
#         return "Task not found"
    
#     tasks.remove(task)
#     return f"{task} removed from the list"

# def run_agent(user_input):

#     system_prompt = """
# You are a task management agent.

# If the user wants to add a task:
# Return JSON like:
# {"tool":"add_task","task":"Study AI"}

# If the user wants to see all tasks:
# Return JSON like:
# {"tool":"list_tasks"}

# If the user wants to delete a task:
# Return JSON like:
# {"tool":"delete_task","task":"Study AI"}

# Return ONLY valid JSON.
# """

#     response = ollama.chat(
#         model="llama3",
#         messages=[
#             {"role":"system","content": system_prompt},
#             {"role":"user","content": user_input},
#         ],
#     )

#     message = response["message"]["content"]

#     print("DEBUG:", message)  # helps you see model output

#     try:
#         data = json.loads(message)

#         if data["tool"] == "add_task":
#             return add_task(data["task"])

#         elif data["tool"] == "list_tasks":
#             return list_tasks()

#         elif data["tool"] == "delete_task":
#             return delete_task(data["task"])

#     except:
#         return message

#     return message


# if __name__ == "__main__":
#     print("Task Management Agent Started (type 'exit' to quit)\n")

#     while True:
#         user_input = input("You: ")

#         if user_input.lower() == "exit":
#             print("Agent stopped.")
#             break

#         result = run_agent(user_input)
#         print("Agent:", result

import ollama
import json
appointments=[]

def book_appointment(doctor:str, date:str, time:str):
    appointments.append({"doctor":doctor,"date":date,"time":time})
    return f"Appointment booked with DR.{doctor} on {date} at {time}"

def list_appointments():
    if not appointments:
        return "No appointments booked."
    
    result = ""
    for i, appt in enumerate(appointments, 1):
        result += f"{i}. {appt['doctor']} - {appt['date']} at {appt['time']}\n"
    return result
     
def cancel_appointment(doctor):
    for appt in appointments:
        if appt["doctor"].lower() == doctor.lower():
            appointments.remove(appt)
            return f"Appointment with {doctor} cancelled."
    return "Appointment not found."

def run_Agent(user_input):
    system_prompt="""
You are an hospital appointment agent
if the user want to book an appointment return json like:
{"tool":"book_appointment","doctor":"Dr.Smith","date":"2024-01-01","time":"10:00"}

if the user want to see all the appointments return json like 

{"tool":"list_appointments"}

if the user wants to delete the apoointment return json like
{"tool":"cancel_appointment","doctor":"Dr.smith"}
Return ONLY valid JSON.

"""

    response=ollama.chat(
        model="llama3",
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":user_input},
        ],
    )

    message=response["message"]["content"]

    print("DEBUG:",message)

    try:
        data=json.loads(message)

        if data["tool"]=="book_appointment":
                doctor = data.get("doctor")
                date = data.get("date")
                time = data.get("time")

                if not doctor or not date or not time:
                    return "Missing information. Please provide doctor, date and time."

                return book_appointment(doctor, date, time)

        
        elif data["tool"]=="list_appointments":
            return list_appointments()
        elif data["tool"]=="cancel_appointment":
            return cancel_appointment(data["doctor"])
        
    except:
        return message
    

if __name__=="__main__":
    print("Hospital Appointment Agent Started (type 'exit' to quit)\n")
    while True:
        user_input=input("You: ")
        if user_input.lower()=="exit":
            print("Agent stopped.")
            break
        result=run_Agent(user_input)
        print("Agent:",result)