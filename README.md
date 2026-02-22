# OpenAI Using LangChain

A simple project that builds an `LLMChain` using LangChain and OpenAI. It takes user input and generates a suitable prompt based on predefined system instructions.

## Overview

This project demonstrates a clean way to start a small Prompt Engineering application by:
- Separating model initialization into its own file.
- Defining system instructions in a dedicated module.
- Using a simple CLI entry point for interaction.

## Features

- Clear and extensible project structure.
- Uses `PromptTemplate` for structured prompt building.
- Secure API key loading through a `.env` file.
- Easy customization of system instructions and model settings.

## Project Structure

- `main.py`: Main entry point and user input handling.
- `initialize.py`: Creates the `PromptTemplate` and builds the `LLMChain`.
- `prompt.py`: Contains the `SYSTEM_INSTRUCTIONS` variable.
- `.env`: Environment variables file (including `OPENAI_API_KEY`).

## Requirements

- Python 3.9 or later.
- A valid OpenAI API key.

## Installation

```bash
pip install langchain langchain-openai python-dotenv
```

## Configuration

Create a `.env` file in the project root and add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Run

```bash
python main.py
```

After running the script, enter what you want to generate a prompt for, and the app will print the result directly.

## Important Notes

- If you get an API key error, verify your `OPENAI_API_KEY` value.
- You can edit `prompt.py` to change how prompt generation behaves.
- You can adjust model parameters (such as `temperature`) in `initialize.py`.

## Contact Information

- Facebook Page: https://facebook.com/your-page
- LinkedIn Profile: https://linkedin.com/in/your-profile
