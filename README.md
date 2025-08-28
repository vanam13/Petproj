# 🍽️ Lunch Invitation App

A fun and interactive Flask web application designed to help you ask someone special to lunch! This app guides you through the entire process of planning a lunch date with a conversational flow.

## ✨ Features

- 💝 **Interactive Lunch Invitation**: Step-by-step process to ask someone to lunch
- 🍕 **Cuisine Selection**: Choose from Italian, Chinese, Indian, Mexican, or Japanese
- 🏪 **Restaurant Options**: Browse through curated restaurant choices for each cuisine
- 📅 **Date Selection**: Pick between Tuesday or Wednesday
- 🎯 **Beautiful UI**: Modern, responsive design with smooth animations
- 📱 **Mobile Friendly**: Works perfectly on all devices
- 🔄 **Session Management**: Remembers choices throughout the conversation

## 🚀 How It Works

1. **Ask for Lunch** - Start by asking if they're interested in having lunch together
2. **Choose Cuisine** - Pick from 5 delicious cuisine types
3. **Browse Restaurants** - View 2 great restaurant options for the selected cuisine
4. **Select Date** - Choose between Tuesday or Wednesday
5. **Confirmation** - Get a complete summary of your lunch plans!

## 📱 Pages & Flow

- **Home** (`/`): Welcome page with app overview
- **Ask Lunch** (`/ask_lunch`): Initial lunch invitation
- **Select Cuisine** (`/select_cuisine`): Choose food type
- **Show Restaurants** (`/show_restaurants/<cuisine>`): Browse restaurant options
- **Select Day** (`/select_day`): Pick Tuesday or Wednesday
- **Lunch Confirmed** (`/lunch_confirmed`): Final confirmation with all details
- **Lunch Declined** (`/lunch_declined`): Graceful handling of declined invitations

## 🏗️ Project Structure

```
lunch-invitation-app/
├── app.py                 # Main Flask application with routes
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── run.py                # Alternative startup script
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── index.html        # Home page
    ├── ask_lunch.html    # Lunch invitation page
    ├── select_cuisine.html # Cuisine selection
    ├── show_restaurants.html # Restaurant display
    ├── select_day.html   # Day selection
    ├── lunch_confirmed.html # Final confirmation
    └── lunch_declined.html # Declined invitation
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Download Project

Download the project files to your local machine.

### Step 2: Navigate to Project Directory

```bash
cd path/to/your/lunch-invitation-app
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
# or
python run.py
```

The application will start on `http://localhost:5000`

## 🎮 Usage

1. **Start the App**: Open your browser and go to `http://localhost:5000`
2. **Begin Invitation**: Click "Start Lunch Invitation"
3. **Ask for Lunch**: Present the invitation to your special someone
4. **Follow the Flow**: Guide them through cuisine selection, restaurant browsing, and date picking
5. **Get Confirmation**: Receive a complete summary of your lunch plans!

## 🎨 Customization

### Adding New Cuisines

1. Add cuisine data to the `RESTAURANTS` dictionary in `app.py`:
```python
'french': [
    {'name': 'Le Bistro', 'rating': '4.6', 'price': '$$$', 'description': 'Authentic French cuisine'},
    {'name': 'Café Paris', 'rating': '4.3', 'price': '$$', 'description': 'Cozy French café'}
]
```

2. Add corresponding icons in `select_cuisine.html`

### Modifying Restaurant Data

Edit the `RESTAURANTS` dictionary in `app.py` to change restaurant names, ratings, prices, and descriptions.

### Changing Available Days

Modify the day selection logic in `select_day()` function to include different days.

## 🔧 Development

### Running in Development Mode

The app is configured to run in development mode by default:
- Debug mode is enabled
- Auto-reload on code changes
- Detailed error messages

### Session Management

The app uses Flask sessions to maintain state throughout the conversation flow. Each step validates that previous steps have been completed.

## 🚀 Production Deployment

### Security Considerations

1. Change the secret key in `app.py`:
```python
app.secret_key = 'your-production-secret-key'
```

2. Disable debug mode:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

### Deployment Options

- **Heroku**: Easy deployment with Git integration
- **AWS**: Use Elastic Beanstalk or EC2
- **DigitalOcean**: Deploy on App Platform or Droplets
- **VPS**: Traditional server deployment

## 🍽️ Cuisine Options

- **Italian**: Pasta, pizza, and authentic Italian flavors
- **Chinese**: Traditional Chinese dishes and dim sum
- **Indian**: Rich spices and aromatic curries
- **Mexican**: Tacos, enchiladas, and fresh Mexican cuisine
- **Japanese**: Sushi, ramen, and Japanese specialties

## 🛠️ Technologies Used

- **Backend**: Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript
- **CSS Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0.0
- **Python Version**: 3.8+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 💡 Ideas for Enhancement

- Add more cuisine types
- Include restaurant photos and menus
- Add time selection (not just 12 PM)
- Include dietary preference options
- Add location-based restaurant suggestions
- Include weather considerations for outdoor dining

## 🎯 Perfect For

- Asking someone on a first date
- Planning lunch with colleagues
- Organizing friend meetups
- Making lunch plans with family
- Any situation where you want to make lunch planning fun and interactive!

---

**Happy Lunch Planning! 🍽️💕**
