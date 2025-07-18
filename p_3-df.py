import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "user_details.xlsx")

try:
    
    name = input("Enter Your Name : ").strip()
    if not name:
        raise ValueError("Name can not be Empty")

    age_input =input("Enter your Age : ").strip()
    if not age_input.isdigit():
        raise ValueError ("Write Age in Integar")
    age = age_input

    email = input("Enter Your Email address : ").strip()
    if "@" not in email or "." not in email:
        raise ValueError("Inavlid Email Format")

    user_data ={
    
        "Name" : [name],
        "age" :[age],   
        "Email_Address" : [email]
    }

    df = pd.DataFrame(user_data)
    if os.path.exists(file_path):
        existing_df = pd.read_excel(file_path)
        combined_df = pd.concat([existing_df,df], ignore_index=True)
    else:
        combined_df = df

    combined_df.to_excel(file_path, index=False)
    print("File saved to:", file_path)

except ValueError as e:
    print(f" Error: {e}")
    
except Exception as e:
    print(f"\n Error:{e}")