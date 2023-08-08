#ANON LEAKS ON TOP


from time import sleep
from Cloner import Guild, Restart, Copy


words = " this tool was created by [ P I N G U ] in AnonLeaks\n https://dsc.gg/anonleaks\n"
for char in words:
    sleep(0.1)
    print(char, end='', flush=True)
invisible_char = '\u200B'

token = input("Insert token here: ")

commands = {
    "restart": {
        ".restart",
    },
    "copy": {
        ".copy -all",
        ".copy -roles",
        ".copy -emojis",
        ".copy -settings"
    },
    "exit": {
        ".exit"
    }
}

#ANON LEAKS ON TOP


def main():
    stats = True  # per non dare errore se si usa il metodo exit()
    print("====================================================")
    print(".restart: reset server")
    print(".copy -all: copy all options from server")
    print(".copy -roles: copy roles")
    print(".copy -emojis: copy emojis")
    print(".copy -settings: copy settings example: icon, name, description, ...")
    print(".help: use it for help")
    
    print("====================================================")

    while stats:

        command = input("enter the command to execute  >>> ")

        if command.startswith(".exit"):  # per uscire dal tool 

            stats = False  # to not get error from stop wihle loop
            exit(-1)

        # per ottenere tutti i comandi e il creatore 
        elif command.startswith(".help"):

            print("Copyright: https://dsc.gg/anonleaks\n")
            z = ""
            for com, d in commands.items():  # creare comando help
                z += com + "\n"
                for i in d:
                    z += "  " + i + "\n"
            print(z)

         # per riavviare tutti gli oggetti della guild, ad esempio: ruoli, canali, emoji, ...
        elif command.startswith(".restart"):

            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)

            if guild.get_info.get("code"):
                print("\033 Invalid server id\033")
                continue
                
            print("restart roles...")
            restart = Restart(guild)
            restart.roles()

        # copiare i ruoli e aggiungerli alla memoria cache se è necessario copiare il server tow in run one si ottiene un errore
        elif command.startswith(".copy -roles") or command.startswith(".copy -r"):

            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)
            if guild.get_info.get("code"):
                print("\033 Invalid server id\033 ")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild(to_guild_id, token)
            if to_guild.get_info.get("code"):
                print("\033 Invalid server id\033")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            copy.create_roles()

        # just copy emojis
        elif command.startswith(".copy -emojis") or command.startswith(".copy -e"):
            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)

            if guild.get_info.get("code"):
                print("\033 Invalid server id\033")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild(to_guild_id, token)
            if to_guild.get_info.get("code"):
                print("\033 Invalid server id\033")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            copy.create_emojis()

        # to copy: icon, name, description, ...
        elif command.startswith(".copy -settings") or command.startswith(".copy -s"):
            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)

            if guild.get_info.get("code"):
                print("\033 Invalid server id\033")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild()
            if Guild(to_guild_id).get_info.get("code"):
                print("\033 Invalid server id\033")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            copy.update_settings_from_server()

        # this is a great command to copy all roles, channels, emojis, settings
        # the cache imprtant here because synchronization channel permissions with roles 
        elif command.startswith(".copy -all") or command.startswith(".copy -a"):

            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)
            if guild.get_info.get("code"):
                print("\033 Invalid server id\033")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild(to_guild_id, token)
            if to_guild.get_info.get("code"):
                print("\033 Invalid server id\033")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            restart = Restart(guild=to_guild)

            print("restart roles...")
            restart.roles()
            print("restart channels...")
            restart.channels()
            print("restart roles...")
            restart.roles()
            print("restart emojis...")
            restart.emojis()
            print("copy roles...")
            copy.create_roles()
            print("copy channels...")
            copy.create_channels()
            print("copy emojis...")
            copy.create_emojis()
            print("copy server settings...")
            copy.update_settings_from_server()

if __name__ == "__main__":
    main()




#ANON LEAKS ON TOP
