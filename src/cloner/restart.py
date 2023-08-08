from .guild import Guild


class Restart(object):
    def __init__(self, guild: Guild):
        self.guild = guild

    def channels(self):
        if self.guild.get_info.get("code") == 50001:
            print("\033 Invalid server id\033")
        for channel in self.guild.channels:
            o = self.guild.delete_channel(channel["id"])
            if "50013" in o:
                print(f"\033 Missing Permissions {channel['name']}\033")
                continue
            print(f"\33 Delete {channel['name']}\033[0m")

    def roles(self):
        if self.guild.get_info.get("code") == 50001:
            print("\033 Invalid server id\033")
        for role in self.guild.roles:
            o = self.guild.delete_role(role["id"])
            if "50013" in o:
                print(f"\033 Missing Permissions {role['name']}\033")
                continue
            print(f"\33 Delete {role['name']}\033")

    def emojis(self):
        if self.guild.get_info.get("code") == 50001:
            print("\033 Invalid server id\033")
        for emoji in self.guild.emojis:
            o = self.guild.delete_emoji(emoji["id"])
            if "50013" in o:
                print(f"\033 Missing Permissions {emoji['name']}\033")
                continue
            print(f"\33 Delete {emoji['name']}\033")
