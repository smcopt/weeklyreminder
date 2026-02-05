import smtplib
import os
import ssl
from email.message import EmailMessage
from datetime import datetime

# --- CONFIGURATION ---
SENDER_EMAIL = os.environ.get('EMAIL_USER')
APP_PASSWORD = os.environ.get('EMAIL_PASSWORD')
RECEIVER_EMAILS = ["sujanpaudel3@gmail.com", "sujanpaudel@iom.int"]

# --- BRANDING (Based on your Color Guide) ---
# Primary Header Background: Blue Sapphire
BRAND_COLOR = "#1B657C"
# Call to Action Button: Burnt Sienna
ACCENT_COLOR = "#EC6B4D"
# Main Text: Baltic Sea
TEXT_COLOR = "#2C2C2C"
# Email Background: Ecru White
BG_COLOR = "#F5F3E8"

# URL to your logo (Replace with your specific GitHub Raw URL)
LOGO_URL = "https://github.com/smcopt/weeklyreminder/blob/779c27bb539d55d1b4df136a86b7173adfe3e917/CountryLogo_Palestine_V01.png"
ORG_NAME = "Site Management Cluster - Palestine"

# --- EMAIL CONTENT ---
subject = "Weekly Team Reminder"

# 1. Plain Text Fallback
text_body = """
Hi Team,

This is your automated weekly reminder for Thursday at 4 PM.
Please remember:
To book the meeting room for the Cluster Meeting
To send the list of individuals joining the meeting to the security team. 

Best regards,
IM Team
"""

# 2. HTML Version (Branded)
html_body = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    /* Global Resets */
    body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; margin: 0; padding: 0; background-color: {BG_COLOR}; }}
    
    /* Container (The Card) */
    .container {{ 
        max-width: 600px; 
        margin: 40px auto; 
        background-color: #ffffff; 
        border-radius: 0px; /* Sharp corners often look more humanitarian/official */
        overflow: hidden; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
    }}

    /* Header */
    .header {{ 
        background-color: {BRAND_COLOR}; 
        padding: 30px 40px; 
        text-align: center; 
    }}
    .header img {{ 
        max-width: 200px; 
        height: auto; 
        filter: brightness(0) invert(1); /* Turns black logo to white if needed, remove if logo is already white */
    }}

    /* Content */
    .content {{ 
        padding: 40px; 
        color: {TEXT_COLOR}; 
        line-height: 1.6; 
    }}
    h2 {{
        color: {BRAND_COLOR};
        margin-top: 0;
        font-weight: 600;
    }}
    
    /* Button */
    .btn {{ 
        display: inline-block; 
        padding: 12px 28px; 
        background-color: {ACCENT_COLOR}; 
        color: #ffffff !important; 
        text-decoration: none; 
        border-radius: 4px; 
        font-weight: bold; 
        margin-top: 20px; 
    }}

    /* Footer */
    .footer {{ 
        background-color: {TEXT_COLOR}; 
        padding: 20px; 
        text-align: center; 
        font-size: 12px; 
        color: {BG_COLOR}; 
    }}
    .footer a {{ color: {ACCENT_COLOR}; text-decoration: none; }}
</style>
</head>
<body>

<div class="container">
    <div class="header">
        <img src="{LOGO_URL}" alt="Site Management Cluster Logo">
    </div>

    <div class="content">
        <h2>Weekly Action Required</h2>
        <p>Hi Team,</p>
        
        <p>This is your automated weekly reminder. Please ensure the following reporting tasks are completed by EOD:</p>
        
        <ul>
            <li><strong>Task 1:</strong> Book the meeting room (Dead Sea - Ground Floor, Building A, IOM) for the Cluster Meeting</li>
            <li><strong>Task 2:</strong> Share the list of in-person participants/attendees with the Security Team </li>
            <li><strong>Task 3:</strong> Ensure that all action points for this week have been addressed by the designated team members</li>
        </ul>

        <p>Cheers,</p>
        <p>SM Cluster IM Team</p>
    </div>

    <div class="footer">
        <p>&copy; {datetime.now().year} {ORG_NAME}.<br></p>
    </div>
</div>

</body>
</html>
"""

def send_email():
    if not SENDER_EMAIL or not APP_PASSWORD:
        print("Error: Missing environment variables.")
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(RECEIVER_EMAILS)

    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype='html')

    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
            print(f"Branded email sent successfully at {datetime.now()}.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise e

if __name__ == "__main__":
    send_email()
