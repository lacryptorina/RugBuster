import discord
from discord.ext import commands
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import re
import requests
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///wallets.db')
db = SQLAlchemy(app)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Database model
class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String,