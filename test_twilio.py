#!/usr/bin/env python3
"""
Test script to verify Twilio credentials and WhatsApp functionality
"""

from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, YOUR_WHATSAPP_NUMBER

def test_twilio_credentials():
    """Test if Twilio credentials are valid"""
    try:
        print("Testing Twilio credentials...")
        print(f"Account SID: {TWILIO_ACCOUNT_SID}")
        print(f"Auth Token: {TWILIO_AUTH_TOKEN[:8]}...")  # Only show first 8 chars for security
        
        # Try to create a client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Try to fetch account info to verify credentials
        account = client.api.accounts(TWILIO_ACCOUNT_SID).fetch()
        print(f"✅ Credentials valid! Account name: {account.friendly_name}")
        print(f"Account status: {account.status}")
        
        return True
        
    except Exception as e:
        print(f"❌ Credential error: {e}")
        return False

def test_whatsapp_numbers():
    """Test WhatsApp number formatting"""
    print("\nTesting WhatsApp numbers...")
    print(f"From (Twilio): {TWILIO_PHONE_NUMBER}")
    print(f"To (Your number): {YOUR_WHATSAPP_NUMBER}")
    
    # Check if numbers have proper format
    if not TWILIO_PHONE_NUMBER.startswith('whatsapp:'):
        print("❌ Twilio phone number should start with 'whatsapp:'")
        return False
    
    if not YOUR_WHATSAPP_NUMBER.startswith('whatsapp:'):
        print("❌ Your WhatsApp number should start with 'whatsapp:'")
        return False
    
    print("✅ WhatsApp number format is correct")
    return True

def test_whatsapp_message():
    """Test sending a WhatsApp message"""
    try:
        print("\nTesting WhatsApp message sending...")
        
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        message_body = "🧪 Test message from your lunch app! If you receive this, WhatsApp integration is working."
        
        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=message_body,
            to=YOUR_WHATSAPP_NUMBER
        )
        
        print(f"✅ Test message sent successfully!")
        print(f"Message SID: {message.sid}")
        print(f"Status: {message.status}")
        
        return True
        
    except Exception as e:
        print(f"❌ WhatsApp message error: {e}")
        
        # Provide specific guidance based on error
        if "Authentication" in str(e):
            print("\n🔍 This looks like an authentication issue. Please check:")
            print("1. Your Account SID and Auth Token are correct")
            print("2. Your Twilio account is active (not suspended)")
            print("3. You're not using expired trial credentials")
        elif "not verified" in str(e).lower():
            print("\n🔍 Your WhatsApp number needs to be verified with Twilio first:")
            print("1. Go to Twilio Console > Messaging > Try it out")
            print("2. Send a message to your WhatsApp number")
            print("3. Reply with the verification code Twilio sends")
        elif "trial" in str(e).lower():
            print("\n🔍 Trial account limitations detected:")
            print("1. You can only send messages to verified numbers")
            print("2. Upgrade to a paid account for full functionality")
        
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("TWILIO CREDENTIALS TEST")
    print("=" * 50)
    
    # Test 1: Credentials
    creds_ok = test_twilio_credentials()
    
    # Test 2: Number format
    numbers_ok = test_whatsapp_numbers()
    
    # Test 3: WhatsApp message (only if credentials are valid)
    if creds_ok and numbers_ok:
        test_whatsapp_message()
    
    print("\n" + "=" * 50)
    print("TEST COMPLETE")
    print("=" * 50)
