# 📱 WhatsApp Setup Guide

## 🚀 Quick Setup (5 minutes)

### 1. **Get Twilio Account (Free Trial)**
- Go to [https://www.twilio.com](https://www.twilio.com)
- Sign up for a free account
- Verify your email and phone number

### 2. **Get Your Credentials**
- Go to **Console** → **Account Info**
- Copy your **Account SID** and **Auth Token**

### 3. **Test WhatsApp**
- Go to **Messaging** → **Try it out** → **Send a WhatsApp message**
- Use the provided number: `+14155238886`
- Add your WhatsApp number to test

### 4. **Update Your App**
- Open `config.py`
- Replace the placeholder values:

```python
TWILIO_ACCOUNT_SID = 'AC1234567890abcdef...'  # Your actual Account SID
TWILIO_AUTH_TOKEN = '1234567890abcdef...'     # Your actual Auth Token
YOUR_WHATSAPP_NUMBER = 'whatsapp:+1234567890' # Your WhatsApp number
```

### 5. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 6. **Run Your App**
```bash
python app.py
```

## 💡 How It Works

1. **She uses your app** to select lunch preferences
2. **When she confirms**, you get an instant WhatsApp message
3. **Message includes**: Restaurant, cuisine, day, time, location
4. **You're notified immediately** on your phone

## 🔧 Troubleshooting

### **Message not sending?**
- Check your Twilio credentials
- Make sure your WhatsApp number is correct
- Verify your Twilio account is active

### **Free trial limits?**
- Twilio free trial: 1,000 messages
- Perfect for personal use
- Upgrade only if you need more

## 🎯 Benefits of WhatsApp

✅ **Instant notifications** - Get notified immediately  
✅ **No email setup** - Works out of the box  
✅ **Mobile friendly** - Perfect for on-the-go  
✅ **Free to use** - Twilio free trial included  
✅ **Reliable delivery** - WhatsApp's robust system  

## 🚨 Important Notes

- **Keep credentials private** - Don't share your Twilio tokens
- **Test first** - Use Twilio's test environment
- **Free trial** - Perfect for personal projects
- **WhatsApp Business** - Works with regular WhatsApp too

## 🎉 You're All Set!

Now when someone uses your lunch app, you'll get a beautiful WhatsApp message with all the details! 

**No more checking emails or missing notifications! 📱✨**
