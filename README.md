# Simple Flipkart Price Tracker(Deprecated)

**Flipkart Price Tracker** is a simple Python script that allows you to track the price of a product on Flipkart and sends you an email notification when the price falls below a certain threshold.

## Features

- **Price Tracking:** Monitor the price of a specific product on Flipkart.
- **Email Notifications:** Receive an email notification when the price drops below a set threshold.
- **Customizable:** Easily customize the product URL and email notification settings.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Creating a Build](#CreatingaBuild)
- [Contributing](#contributing)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourname/Amazon-Price-Tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Amazon-Price-Tracker
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script using the following command:

   ```bash
   python track.py
   ```

2. The script will start monitoring the price of the specified product on Flipkart.

3. You will receive an email notification if the price falls below the set threshold.

## Customization

You can easily customize the script according to your needs:

- **Product URL:** Change the URL of the product you want to track by modifying the `URL` variable in `track.py`.
- **Email Settings:** Update the sender's and receiver's email addresses, as well as the email subject and message in the `SendMail` function.
- **Price Threshold:** Adjust the price threshold at which you want to receive notifications by modifying the `threshold` variable in `track.py`.

## Creating a Build
- To create a build(.exe file) for this code, run the following command on your terminal:
- pyinstaller --add-data "priceTracker.py;." priceTracker.py

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.
