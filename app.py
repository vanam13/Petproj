from flask import Flask, render_template, request, redirect, url_for, session
from twilio.rest import Client
import os

app = Flask(__name__)
app.secret_key = 'lunch-invitation-secret-key'

# Use environment variables in production, fallback to actual credentials for deployment
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', 'AC54a22f570fa81166ad8d167b40f88904')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', 'd015d6b26432480833c0122d231cace5')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER', 'whatsapp:+14155238886')
YOUR_WHATSAPP_NUMBER = os.environ.get('YOUR_WHATSAPP_NUMBER', 'whatsapp:+919490169690')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Restaurant data
RESTAURANTS = {
    'italian': [
        {
            'name': 'Bella Italia',
            'rating': '4.5',
            'price': '$$',
            'description': 'Authentic Italian cuisine with homemade pasta and wood-fired pizzas.'
        },
        {
            'name': 'Pasta Palace',
            'rating': '4.3',
            'price': '$',
            'description': 'Cozy Italian bistro serving classic dishes in a warm atmosphere.'
        }
    ],
    'chinese': [
        {
            'name': 'Golden Dragon',
            'rating': '4.4',
            'price': '$$',
            'description': 'Traditional Chinese dishes with modern twists and fresh ingredients.'
        },
        {
            'name': 'Wok & Roll',
            'rating': '4.1',
            'price': '$',
            'description': 'Quick and delicious Chinese takeout with dine-in options.'
        }
    ],
    'indian': [
        {
            'name': 'Spice Garden',
            'rating': '4.6',
            'price': '$$',
            'description': 'Rich Indian flavors with aromatic spices and fresh naan bread.'
        },
        {
            'name': 'Taj Mahal',
            'rating': '4.2',
            'price': '$',
            'description': 'Authentic Indian street food and traditional curries.'
        }
    ],
    'mexican': [
        {
            'name': 'El Mariachi',
            'rating': '4.5',
            'price': '$$',
            'description': 'Vibrant Mexican restaurant with fresh guacamole and margaritas.'
        },
        {
            'name': 'Taco Fiesta',
            'rating': '4.0',
            'price': '$',
            'description': 'Casual Mexican eatery with build-your-own tacos and burritos.'
        }
    ],
    'japanese': [
        {
            'name': 'Sakura Sushi',
            'rating': '4.7',
            'price': '$$$',
            'description': 'Premium sushi and sashimi with traditional Japanese presentation.'
        },
        {
            'name': 'Tokyo Express',
            'rating': '4.2',
            'price': '$$',
            'description': 'Quick Japanese cuisine with bento boxes and ramen bowls.'
        }
    ]
}

def send_whatsapp_notification(restaurant_name, cuisine, day):
    """Send WhatsApp notification with lunch details"""
    try:
        message_body = f"""🎉 *LUNCH DATE CONFIRMED!* 🎉

🍽️ *Restaurant:* {restaurant_name}
🍕 *Cuisine:* {cuisine.title()}
📅 *Day:* {day.title()}
⏰ *Time:* 12:00 PM
📍 *Location:* Downtown Area

💕 *She said YES to lunch with you!*

*Make sure to:*
• Confirm the reservation
• Dress nicely  
• Be on time
• Have fun!

Good luck! 🚀"""

        message = twilio_client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=message_body,
            to=YOUR_WHATSAPP_NUMBER
        )
        
        print(f"WhatsApp message sent! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"WhatsApp error: {e}")
        return False

def send_decline_notification():
    """Send WhatsApp notification when lunch is declined"""
    try:
        message_body = f"""😔 *LUNCH INVITATION DECLINED* 😔

💔 *She said NO to lunch with you*

*Don't worry, here are some tips:*
• It's not the end of the world
• Maybe she's busy or has other plans
• You can try again another time
• Focus on other opportunities

*Remember:* Rejection is just redirection! 🚀

Keep your head up! 💪"""

        message = twilio_client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=message_body,
            to=YOUR_WHATSAPP_NUMBER
        )
        
        print(f"Decline notification sent! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"WhatsApp decline notification error: {e}")
        return False

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/ask_lunch', methods=['GET', 'POST'])
def ask_lunch():
    if request.method == 'POST':
        response = request.form.get('lunch_response')
        if response == 'yes':
            session['lunch_agreed'] = True
            return redirect(url_for('select_cuisine'))
        else:
            # Send decline notification immediately when they say no
            send_decline_notification()
            return redirect(url_for('lunch_declined'))
    
    return render_template('ask_lunch.html')

@app.route('/select_cuisine')
def select_cuisine():
    if not session.get('lunch_agreed'):
        return redirect(url_for('index'))
    
    cuisines = list(RESTAURANTS.keys())
    return render_template('select_cuisine.html', cuisines=cuisines)

@app.route('/show_restaurants/<cuisine>')
def show_restaurants(cuisine):
    if not session.get('lunch_agreed'):
        return redirect(url_for('index'))
    
    if cuisine not in RESTAURANTS:
        return redirect(url_for('select_cuisine'))
    
    session['selected_cuisine'] = cuisine
    restaurants = RESTAURANTS[cuisine]
    return render_template('show_restaurants.html', restaurants=restaurants)

@app.route('/select_restaurant', methods=['POST'])
def select_restaurant():
    if not session.get('lunch_agreed'):
        return redirect(url_for('index'))
    
    restaurant_name = request.form.get('restaurant')
    if restaurant_name:
        session['selected_restaurant'] = restaurant_name
        return redirect(url_for('select_day'))
    
    return redirect(url_for('show_restaurants', cuisine=session.get('selected_cuisine', 'italian')))

@app.route('/select_day', methods=['GET', 'POST'])
def select_day():
    if not session.get('lunch_agreed') or not session.get('selected_restaurant'):
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        day = request.form.get('day')
        if day in ['tuesday', 'wednesday']:
            session['selected_day'] = day
            return redirect(url_for('lunch_confirmed'))
    
    return render_template('select_day.html')

@app.route('/lunch_confirmed')
def lunch_confirmed():
    if not all(key in session for key in ['lunch_agreed', 'selected_cuisine', 'selected_restaurant', 'selected_day']):
        return redirect(url_for('index'))
    
    # Get restaurant details
    cuisine = session['selected_cuisine']
    restaurant_name = session['selected_restaurant']
    day = session['selected_day']
    
    # Find restaurant object
    restaurant = None
    for r in RESTAURANTS[cuisine]:
        if r['name'] == restaurant_name:
            restaurant = r
            break
    
    if not restaurant:
        return redirect(url_for('index'))
    
    # Send WhatsApp notification
    send_whatsapp_notification(restaurant_name, cuisine, day)
    
    return render_template('lunch_confirmed.html', 
                         restaurant=restaurant, 
                         cuisine=cuisine, 
                         day=day)

@app.route('/lunch_declined')
def lunch_declined():
    return render_template('lunch_declined.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
