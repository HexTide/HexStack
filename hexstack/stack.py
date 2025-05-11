import importlib

class HexStack:
    def __init__(self, sequence: list[str]):
        self.sequence = sequence

    def run(self):
        for bot_path in self.sequence:
            print(f"[HexStack] Loading: {bot_path}")
            module = importlib.import_module(bot_path)
            bot = module.Bot()
            print(f"[HexStack] Starting bot: {bot.name}")
            bot.start()
            print(f"[HexStack] Finished bot: {bot.name}\n")
