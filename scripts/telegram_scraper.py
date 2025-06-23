import os
import csv
from telethon import TelegramClient
from dotenv import load_dotenv

# Load credentials
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Main scraping function
async def scrape_channels(channel_list, output_csv='../data/raw/telegram_data.csv', media_dir='data/raw/photos', download_images=False):
    os.makedirs(media_dir, exist_ok=True)

    client = TelegramClient('scraping_session', api_id, api_hash)
    await client.start()

    with open(output_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])

        for channel in channel_list:
            entity = await client.get_entity(channel)
            channel_title = entity.title

            async for message in client.iter_messages(entity, limit=10000):
                media_path = None

                # Optional image download
                if download_images and message.media and hasattr(message.media, 'photo'):
                    filename = f"{channel}_{message.id}.jpg"
                    media_path = os.path.join(media_dir, filename)
                    await client.download_media(message.media, media_path)

                writer.writerow([channel_title, channel, message.id, message.message, message.date, media_path])
            print(f"✅ Scraped data from {channel}")

    await client.disconnect()