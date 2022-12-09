# Simple OpenAI Discord Bot

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running pip install in the root directory.

>pip installs are specified as commands next to the imports for ease.

3. Create a new bot in the Discord Developer Portal and retrieve the bot token.
4. Create a .env file in the root directory and add the following:

```
OPENAI_TOKEN=<here>
OPENAI_ENGINE=<here>
DISCORD_TOKEN=<here>
DISCORD_GUILD=<here>
```
5. Replace the above with.. you know, whatever it wants.
6. Run the bot by executing your favourite methods.

### Usage

The bot will automatically respond to messages in the Discord server it is added to (and specified in the `DISCORD_GUILD`)
The response will be generated using OpenAI API based on the message recieved.

### License
This project is licensed under the MIT License.

### Have trouble trying to set it up?

Contact me on my Discord @ `Maple#3668`
