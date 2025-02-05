# Fortnite Discord Bot

This is a Discord bot that fetches Fortnite player stats, maps, and news using the Fortnite API. The bot is built with `py-cord` and interacts with the Fortnite API to provide real-time information.

## 🚀 Features
- Retrieve Fortnite player stats
- Fetch the current Fortnite map with or without points of interest (POIs)
- Display Fortnite news updates
- Uses Discord slash commands for interaction

## 📌 Requirements
- Python 3.x
- `discord.py`
- `fortnite-api`
- A Discord bot token
- A Fortnite API key

## 🛠 Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TitanProgrammer4480/Fortnite-Discord-bot
   cd Fortnite-Discord-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file and add the following:
     ```env
     TOKEN=your_discord_bot_token
     API_TOKEN=your_fortnite_api_key
     ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## 🎮 Commands

### Player Stats
- `/player_info <player_name>` - Retrieves and displays the Fortnite stats of a player.

### Map Information
- `/blank_map` - Sends the current blank Fortnite map.
- `/map` - Sends the current Fortnite map with points of interest.
- `/pois` - Lists all points of interest with their coordinates.

### News
- `/compact_news` - Displays a summarized version of the latest Fortnite news.
- `/news` - Sends Fortnite news updates with images.


## 📜 License
This project is licensed under the MIT License.
